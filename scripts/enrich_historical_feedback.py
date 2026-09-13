
import sys
from pathlib import Path

# Add project root to Python path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# Import existing application modules

from app.analyzer import feedback_analyzer
from app.database import (get_connection,get_unprocessed_feedback,insert_llm_enrichment)
from app.utils import generate_ticket_number


# Enrich historical feedback


def enrich_historical_feedback(batch_size=10):

    print("=" * 60)
    print("HISTORICAL FEEDBACK ENRICHMENT")
    print("=" * 60)


    # Get feedback that has not yet been processed

    rows = get_unprocessed_feedback()

    print(
        f"Unprocessed feedback records: {len(rows)}"
    )

    if not rows:

        print("No unprocessed feedback found.")

        return


    # Process feedback in batches

    for start in range(
        0,
        len(rows),
        batch_size
    ):

        batch = rows[
            start:start + batch_size
        ]

        print()
        print(
            f"Processing records "
            f"{start + 1} - "
            f"{start + len(batch)} "
            f"of {len(rows)}"
        )


        # Prepare input for LangChain
        

        inputs = []

        for feedback_id, feedback_text in batch:

            inputs.append(
                {
                    "feedback": feedback_text
                }
            )
        
        # Run your existing LangChain chain
        

        try:

            results = feedback_analyzer.batch(
                inputs
            )

        except Exception as e:

            print(
                f"LLM batch failed: {e}"
            )

            continue


        
        # Save each LLM result
        

        for (
            (feedback_id, feedback_text),
            analysis
        ) in zip(batch, results):

            try:

        
                # Extract structured LLM response
                
                sentiment = analysis.sentiment

                category = analysis.category

                priority = analysis.priority

                summary = analysis.summary

                recommended_action = (
                    analysis.recommended_action
                )

                customer_response = (
                    analysis.customer_response
                )


                
                # Generate ticket if required
                

                support_ticket_number = None

                if priority in ["High", "Critical"]:

                    support_ticket_number = (
                        generate_ticket_number()
                    )


                
                # Save to llm_enriched_feedback
                

                insert_llm_enrichment(

                    feedback_id=feedback_id,

                    sentiment=sentiment,

                    category=category,

                    priority=priority,

                    summary=summary,

                    recommended_action=
                        recommended_action,

                    support_ticket_number=
                        support_ticket_number,

                    customer_response=
                        customer_response
                )


                print(
                    f"{feedback_id} processed"
                )


            except Exception as e:

                print(
                    f"Failed to save "
                    f"{feedback_id}: {e}"
                )


    # Final count

    conn = get_connection()

    count = conn.execute(
        """
        SELECT COUNT(*)
        FROM llm_enriched_feedback
        """
    ).fetchone()[0]

    conn.close()


    print()
    print("=" * 60)
    print("ENRICHMENT COMPLETE")
    print("=" * 60)

    print(
        f"Total records in "
        f"llm_enriched_feedback: {count}"
    )



# Entry point


if __name__ == "__main__":

    enrich_historical_feedback(
        batch_size=10
    )


from langchain_core.runnables import RunnableLambda

from app.llm import structured_model
from app.prompts import feedback_prompt
from app.preprocessing import clean_feedback
from app.schemas import FeedbackAnalysis
from app.utils import ( generate_feedback_id, generate_ticket_number )

#chain formation

cleaner = RunnableLambda(clean_feedback)

feedback_analyzer = (
    cleaner
    | feedback_prompt
    | structured_model
)

#Generating response for single feedback

def analyze_feedback(feedback: str)-> FeedbackAnalysis:
    """
    Analyze customer feedback using LangChain.
    """

    result = feedback_analyzer.invoke(
        {
            "feedback": feedback
        }
    )

    return result


def main():

    print("=" * 60)
    print("AI CUSTOMER FEEDBACK ANALYZER")
    print("=" * 60)

    feedback = input(
        "\nEnter customer feedback:\n> "
    )

    if not feedback.strip():
        print("Please enter some feedback.")
        return

    result = analyze_feedback(feedback)

    print("\n--- Analysis ---")

    print(f"Sentiment          : {result.sentiment}")
    print(f"Category           : {result.category}")
    print(f"Priority           : {result.priority}")
    print(f"Summary            : {result.summary}")
    print(
        f"Recommended Action : "
        f"{result.recommended_action}"
    )
    print(f"Requires Support   : {result.requires_support}")
    print(f"Customer Response  : {result.customer_response}")


if __name__ == "__main__":
    main()

# Annual fees was charged even after meeting the minimum spend requirement for fees waive-off
# Card features are good related to dining but the annual fees is too high and not worth it
# Card features are good related to travel but the card activation process is too long
# Facing issues with the app log in and the customer support is not responsive

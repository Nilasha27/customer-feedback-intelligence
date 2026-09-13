
from app.analyzer import analyze_feedback
from app.database import (insert_customer_feedback, insert_llm_enrichment)
from app.utils import generate_feedback_id, generate_ticket_number


#Extracting feedback and storing it in the database, analyzing it using the LLM, 
# storing the enrichment and returning the result for Streamlit

def process_customer_feedback(
    customer_name,
    feedback_text,
    product
):
    """
    Store customer feedback, analyze it using the LLM,
    store the enrichment and return the result for Streamlit.
    """

    # 1. Generate feedback ID
    feedback_id = generate_feedback_id()

    # 2. Store raw customer feedback
    insert_customer_feedback(
        feedback_id=feedback_id,
        customer_name=customer_name,
        feedback_text=feedback_text,
        product=product,
        channel="App",
        source="Streamlit"
    )

    # 3. Analyze feedback
    analysis = analyze_feedback(feedback_text)

    # 4. Extract LLM output
    sentiment = analysis.sentiment
    category = analysis.category
    priority = analysis.priority
    summary = analysis.summary
    recommended_action = analysis.recommended_action
    requires_support = analysis.requires_support
    customer_response = analysis.customer_response

    # 5. Generate support ticket if required
    support_ticket_number = None

    if requires_support:
        support_ticket_number = generate_ticket_number()

    # 6. Store LLM enrichment
    insert_llm_enrichment(
        feedback_id=feedback_id,
        sentiment=sentiment,
        category=category,
        priority=priority,
        summary=summary,
        recommended_action=recommended_action,
        requires_support=requires_support,
        support_ticket_number=support_ticket_number,
        customer_response=customer_response
    )

    # 7. Return result to Streamlit
    return {
        "feedback_id": feedback_id,
        "sentiment": sentiment,
        "category": category,
        "priority": priority,
        "summary": summary,
        "recommended_action": recommended_action,
        "requires_support": requires_support,
        "support_ticket_number": support_ticket_number,
        "customer_response": customer_response
    }
from langchain_core.runnables import RunnableLambda
from app.llm import structured_model
from app.prompts import feedback_prompt
from app.preprocessing import clean_feedback


cleaner = RunnableLambda(clean_feedback)

feedback_analyzer = (
    cleaner
    | feedback_prompt
    | structured_model
)


def analyze_feedback(feedback: str):
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
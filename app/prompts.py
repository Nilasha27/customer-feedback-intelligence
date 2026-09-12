
from langchain_core.prompts import ChatPromptTemplate


feedback_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert customer experience analyst.

Analyze customer feedback accurately.

Your responsibilities:

1. Determine the overall sentiment.
2. Identify the primary category.
3. Assign an appropriate priority.
4. Summarize the feedback concisely.
5. Recommend a practical action.

Do not invent information that is not present
in the customer feedback.
"""
        ),
        (
            "human",
            """
Analyze the following customer feedback:

{feedback}

"""
        ),
    ]
)
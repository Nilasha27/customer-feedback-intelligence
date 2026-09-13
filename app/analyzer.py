from langchain_core.runnables import RunnableLambda

from app.llm import structured_model
from app.prompts import feedback_prompt
from app.preprocessing import clean_feedback
from app.schemas import FeedbackAnalysis

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


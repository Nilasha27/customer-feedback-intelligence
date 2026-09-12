from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GOOGLE_API_KEY
from app.schemas import FeedbackAnalysis


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=GOOGLE_API_KEY,
)


structured_model = model.with_structured_output(
    FeedbackAnalysis
)
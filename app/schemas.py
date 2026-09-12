from typing import Literal

from pydantic import BaseModel, Field


class FeedbackAnalysis(BaseModel):
    """Structured output for customer feedback analysis."""

    sentiment: Literal[
        "positive",
        "negative",
        "neutral",
        "mixed"
    ] = Field(
        description="Overall sentiment of the customer feedback."
    )

    category: Literal[
        "product",
        "delivery",
        "customer_service",
        "pricing",
        "payment",
        "technical",
        "other"
    ] = Field(
        description="Primary category of the feedback."
    )

    priority: Literal[
        "low",
        "medium",
        "high",
        "critical"
    ] = Field(
        description="Priority level based on customer impact."
    )

    summary: str = Field(
        description="A concise summary of the feedback."
    )

    recommended_action: str = Field(
        description="Recommended action for the company."
    )
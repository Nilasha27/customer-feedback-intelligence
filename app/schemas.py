from typing import Literal

from pydantic import BaseModel, Field


class FeedbackAnalysis(BaseModel):
    """Structured output for customer feedback analysis."""

    sentiment: Literal[
        "Positive",
        "Negative",
        "Neutral",
        "Mixed"
    ] = Field(
        description="Overall sentiment of the customer feedback."
    )

    category: Literal[
        "Product & Features",
        "Onboarding & Account Management",
        "Delivery",
        "Customer Service",
        "Payments, Transfers & Cash",
        "Technical & Digital Banking",
        "Fraud & Security",
        "Fees, Pricing & Rewards",
        "Financial Advice & Planning",
        "General & Others"
    ] = Field(
        description="Primary category of the feedback."
    )

    priority: Literal[
        "Low",
        "Medium",
        "High",
        "Critical"
    ] = Field(
        description="Priority level based on customer impact."
    )

    summary: str = Field(
        description="A concise summary of the feedback."
    )

    recommended_action: str = Field(
        description="Recommended action for the company."
    )

    requires_support: bool = Field(
            description=(
                "True if the issue requires human/support team intervention"
            )
        )
    
    customer_response: str = Field(
        description=(
            "Appropriate concise response that can be sent directly to the customer"
        )
    )


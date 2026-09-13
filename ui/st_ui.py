import streamlit as st
from app.feedback_process import process_customer_feedback


st.title("Customer Feedback Intelligence")

customer_name = st.text_input("Customer Name")


product = st.selectbox(
    "Product",
    ["Credit Card", "Deposits", "Payments & Transfers", "Loans", "ATM & Cash Services", "Foreign Exchange",
     "Wealth Management", "Mobile / Internet Banking", "General & Others"]
)

feedback_text = st.text_area(
    "Customer Feedback",
    placeholder="Tell us about your experience..."
)


if st.button("Submit Feedback"):

    if not customer_name.strip():
        st.warning("Please enter customer name.")

    elif not feedback_text.strip():
        st.warning("Please enter customer feedback.")

    else:

        with st.spinner("Analyzing your feedback..."):

            try:

                result = process_customer_feedback(
                    customer_name=customer_name,
                    feedback_text=feedback_text,
                    product=product
                )

                st.success("Feedback submitted successfully!")

                st.write(
                    result["customer_response"]
                )

                if result["support_ticket_number"]:

                    st.info(
                        f"Support ticket created: "
                        f"{result['support_ticket_number']}"
                    )

                with st.expander("Feedback Analysis"):

                    st.write(
                        "**Feedback ID:**",
                        result["feedback_id"]
                    )

                    st.write(
                        "**Sentiment:**",
                        result["sentiment"]
                    )

                    st.write(
                        "**Category:**",
                        result["category"]
                    )

                    st.write(
                        "**Priority:**",
                        result["priority"]
                    )

                    st.write(
                        "**Summary:**",
                        result["summary"]
                    )

                    st.write(
                        "**Recommended Action:**",
                        result["recommended_action"]
                    )

            except Exception as e:

                st.error(
                    f"Unable to process feedback: {str(e)}"
                )
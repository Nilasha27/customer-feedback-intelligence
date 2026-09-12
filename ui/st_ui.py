import streamlit as st
from app.main import analyze_feedback

# st.title("Customer Feedback Intelligence")

# feedback = st.text_area("Enter customer feedback")

# if st.button("Analyze"):
#     result = analyze_feedback(feedback)
#     st.write(result)

# import streamlit as st

# from feedback_analyzer import analyze_feedback


st.set_page_config(
    page_title="AI Customer Feedback Analyzer",
    page_icon="💬",
    layout="centered"
)

st.title("💬 AI Customer Feedback Analyzer")
st.write("Analyze customer feedback using an LLM.")

st.divider()

feedback = st.text_area(
    "Enter customer feedback",
    placeholder="Example: My credit card payment keeps getting declined even though I have sufficient balance.",
    height=150
)

if st.button("Analyze Feedback", type="primary"):

    if not feedback.strip():
        st.warning("Please enter some feedback.")

    else:
        with st.spinner("Analyzing feedback..."):

            try:
                result = analyze_feedback(feedback)

                st.divider()
                st.subheader("Feedback Analysis")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("#### Sentiment")
                    st.write(result.sentiment)

                with col2:
                    st.markdown("#### Priority")
                    st.write(result.priority)

                st.markdown("#### Category")
                st.write(result.category)

                st.markdown("#### Summary")
                st.write(result.summary)

                st.markdown("#### Recommended Action")
                st.write(result.recommended_action)

            except Exception as e:
                st.error(f"Error analyzing feedback: {e}")
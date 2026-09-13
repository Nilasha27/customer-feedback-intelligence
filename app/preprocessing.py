
def clean_feedback(data: dict) -> dict: 

    """ Basic preprocessing before sending feedback to the LLM. """ 

    feedback = data["feedback"] 
    # Remove leading/trailing spaces 
    feedback = feedback.strip() 
    # Normalize excessive whitespace 
    feedback = " ".join(feedback.split()) 
    return {"feedback": feedback}
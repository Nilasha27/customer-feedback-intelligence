import uuid


def generate_feedback_id():

    return f"FB-{uuid.uuid4().hex[:10].upper()}"


def generate_ticket_number():

    return f"TKT-{uuid.uuid4().hex[:8].upper()}"

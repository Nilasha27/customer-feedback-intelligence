
import sys 
from pathlib import Path 
import uuid 

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent 

if str(PROJECT_ROOT) not in sys.path: 
    sys.path.insert(0, str(PROJECT_ROOT))

#Defining multiple feedback analysis mode

def dataset_mode() -> None:
    """
    Analyze reviews from the local dataset.
    """
    # Get feedback that has not been analyzed yet
    feedback_rows = get_unprocessed_feedback() 
    print( f"Unprocessed feedback records: " f"{len(feedback_rows)}" ) 
    if not feedback_rows: 
        print("All feedback has already been processed.") 
        return
    
















































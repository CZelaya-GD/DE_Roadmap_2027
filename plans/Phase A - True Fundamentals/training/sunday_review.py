import logging 
from dataclasses import dataclass
import os 
import dotenv

dotenv.load_dotenv()

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def TemporaryServiceError(Exception):
    """Exception raised for temporary service errors."""
    pass

def PermanentServiceError(Exception):
    """Exception raised for permanent service errors."""
    pass

@dataclass
class settings:
    review_time: int
    anki_cards: int
    topic: str = "Sunday Review" 

material = settings(
                review_time=int(os.getenv("REVIEW_TIME")), 
                anki_cards=os.getenv("ANKI_CARDS"),
                topic=os.getenv("SUNDAY_TOPIC"))

def sunday_review(review_material: settings) -> None:
    logger.info(f"Starting Sunday review for topic: {review_material.topic}")

    try: 
        pass  # Placeholder for the actual review logic

    except TemporaryServiceError as e:
        logger.warning("Temporary failure: %s", e)

    except PermanentServiceError as e:
        logger.error("Permanent failure: %s", e)

    logger.info("Sunday review completed. Total time: %s seconds", 
                review_material.review_time)
    
if __name__ == "__main__": 
    sunday_review(material)
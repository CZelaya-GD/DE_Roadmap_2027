import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s | %(levelname)s | %(filename)s:%(funcName)s:%(lineno)d |%(message)s ')


logger = logging.getLogger(__name__)

def processing_order(order_id: int) -> None:
    """
    Simulates processing an order and Logs the processing steps. 
    """ 
    logger.info(f"Process started for order ID: %s",
                order_id)

    try: 
        pass

    except Exception as e: 
        logger.exception("Error occurred while processing order ID: %d. Error: %s",
                     order_id, 
                     str(e),)
        raise


if __name__ == "__main__": 
    processing_order(12345)


git init

git status   # untracked files: 

git diff

git add logging_git_training.py 

git status   # changes to be committed:

git diff --staged

git commit -m "Added logging and git training script"  

git status   # nothing to commit, working tree clean

git log --oneline   # example: 1a2b3c4 Added logging and git training script

git remote add origin <GITHUB_REPOSITORY_URL>

git remote -v

git push -u origin main

git pull 
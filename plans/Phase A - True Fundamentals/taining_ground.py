import random
import time

import outcome

MAX_ATTEMPTS = 3


class TemporaryServiceError(Exception):
    """The service failed temporarily."""
    pass


class PermanentServiceError(Exception):
    """The service failed permanently."""
    pass


def unreliable_service(order_id: int) -> str:
    """
    Simulates an external service that randomly fails.
    """
    outcome = random.random()

    if outcome < 0.20:
        raise TemporaryServiceError("Service temporarily unavailable.")

    if outcome < 0.30:
        raise PermanentServiceError("Order contains invalid data.")

    print(f"Order {order_id} processed successfully.")
    return f"Order {order_id} completed"


def process_order(order_id: int) -> str:
    """
    Your job: implement the reliability logic here.
    """

    for attempt in range(0, MAX_ATTEMPTS):

        try:
            return unreliable_service(order_id)

        except TemporaryServiceError as error:

            if attempt == MAX_ATTEMPTS - 1:
                print(
                    f'Order {order_id} failed' 
                    f"After {MAX_ATTEMPTS} retries."
                )
                raise

            base_delay = 1  # Base delay in seconds
            delay = base_delay * (2 ** attempt) # Exponential backoff
            jitter  = random.uniform(0, 0.5) # Random jitter between 0 and 0.5 seconds
            delay += jitter

            print(f'Order {order_id} attempt {attempt + 1}'
                  f'failed temporarily: {error}. '
                  f'Retrying in {delay:.2f} seconds...')
            time.sleep(delay)

        except PermanentServiceError as error:

            print(f'Order {order_id} failed permanently: {error}')
            raise


if __name__ == "__main__":
    result = process_order(12345)
    print(result)
import random
import uuid


def random_number(length: int = 6)-> int:
    return random.randint(0, pow(10, length) - 1)


def unique_id(length: int = 6)-> str:
    """
    returns alpha(lowecase) numberic string
    """
    return str(uuid.uuid4())[:length]

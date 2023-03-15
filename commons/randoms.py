import random
import uuid


def random_number(length: int = 6)-> int:
    return random.randint(0, pow(10, length) - 1)


def random_alphanumeric(length: int = 6)-> str:
    return str(uuid.uuid4())[:length]

from commons import random_number, random_alphanumeric


def test_randint():
    for i in range(1000):
        length = 4
        rand_int = random_number(length)
        assert 0 <= rand_int < pow(10, length)


def test_uuid4():
    for length in range(1, 11):
        rand_str = random_alphanumeric(length)
        assert len(rand_str) == length
        if "-" in rand_str:
            rand_str = rand_str.replace("-", "")
        assert rand_str.isalnum()

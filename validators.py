import re

MOBILE_NUMER = r'^(\+91)?[1-9][0-9]{9}$|^0[1-9][0-9]{9}$|^[1-9][0-9]{9}$'
GSTIN = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9]{1}[Z]{1}[0-9A-Z]{1}$'


def __pattern_match(regex_pattern: str, value: str) -> bool:
    pattern = re.compile(regex_pattern)
    return True if pattern.match(value) else False


def validate_mobile_number(number):
    return __pattern_match(MOBILE_NUMER, number)


def validate_gstin(gstin):
    return __pattern_match(GSTIN, gstin)

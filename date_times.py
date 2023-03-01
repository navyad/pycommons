from datetime import datetime, timezone, tzinfo


def _datetime_now(tz=None):
    return datetime.now(tz)

def now_local() -> datetime:
    return _datetime_now()

def now_with_timezone(tz: tzinfo) -> datetime:
    return _datetime_now(tz)

def now_utc_datetime() -> datetime:
    return datetime.utcnow()

def now_utc_datetime_with_timezone(tz: tzinfo) -> datetime:
    return _datetime_now(tz)

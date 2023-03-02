from datetime import datetime, tzinfo


def _datetime_now(tz=None) -> datetime:
    return datetime.now(tz)


def now_local() -> datetime:
    return _datetime_now()


def now_with_timezone(tz: tzinfo) -> datetime:
    return _datetime_now(tz)


def now_utc_datetime() -> datetime:
    return datetime.utcnow()


def now_utc_datetime_with_timezone(tz: tzinfo) -> datetime:
    return _datetime_now(tz)


def get_datetime_instance(datetime_string: str, date_format: str) -> datetime:
    return datetime.strptime(datetime_string, date_format)


def get_datetime_string(date_time: datetime, date_format: str) -> str:
    return date_time.strftime(date_format)

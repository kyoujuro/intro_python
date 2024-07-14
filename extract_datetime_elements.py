from datetime import datetime


datetime_strings = ["2024-07-14 08:17:02", "2024-12-31 23:59:59", "2025-01-01 00:00:00"]


def extract_datetime_elements(datetime_string):
    dt = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    return {
        "year": dt.year,
        "month": dt.month,
        "day": dt.day,
        "dayofweek": dt.weekday(),
        "iso_week": dt.isocalendar().week,
        "hour": dt.hour,
        "minute": dt.minute,
        "second": dt.second,
        "ym": dt.strftime("%Y-%m")
    }

for datetime_string in datetime_strings:
    elements = extract_datetime_elements(datetime_string)
    print(f"日時: {datetime_string} -> 要素: {elements}")

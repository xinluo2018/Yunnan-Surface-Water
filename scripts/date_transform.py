from datetime import datetime, timedelta

def date_to_decimal(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    year_start = datetime(date_obj.year, 1, 1)
    year_end = datetime(date_obj.year + 1, 1, 1)
    return date_obj.year + ((date_obj - year_start).total_seconds() / (year_end - year_start).total_seconds())

def decimal_to_date(decimal_year):
    year = int(decimal_year)
    decimal_part = decimal_year - year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    total_days = 366 if is_leap else 365
    total_seconds = decimal_part * total_days * 24 * 60 * 60
    start_date = datetime(year, 1, 1)
    delta = timedelta(seconds=total_seconds)
    result_date = start_date + delta
    return result_date.strftime("%Y-%m-%d %H:%M:%S")
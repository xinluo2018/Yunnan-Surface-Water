from datetime import datetime, timedelta

def date_to_decimal(date_str):
    '''
    convert date string to decimal year
        param: date_str: date string in format 'YYYY-MM-DDTHH:MM:SS'
        return: decimal year
    eg. date_to_decimal('2019-02-01T00:10:00') -> 2019.08469
    '''
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    year_start = datetime(date_obj.year, 1, 1)
    year_end = datetime(date_obj.year + 1, 1, 1)
    return date_obj.year + ((date_obj - year_start).total_seconds() / (year_end - year_start).total_seconds())

def decimal_to_date(decimal_year):
    '''
    convert decimal year to date string
        param: decimal_year: decimal year
        return: date string in format 'YYYY-MM-DDTHH:MM:SS'
    eg. decimal_to_date(2019.0) -> '2019-01-01T00:00:00'
    '''
    year = int(decimal_year)
    decimal_part = decimal_year - year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    total_days = 366 if is_leap else 365
    total_seconds = decimal_part * total_days * 24 * 60 * 60
    start_date = datetime(year, 1, 1)
    delta = timedelta(seconds=total_seconds)
    result_date = start_date + delta
    return result_date.strftime("%Y-%m-%dT%H:%M:%S")




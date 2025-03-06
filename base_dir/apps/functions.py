def price_calculator(time_delta):
    from datetime import datetime, timedelta

    if time_delta <= timedelta(minutes=30):
        price = 3.00
        return round(price, 2)

    elif time_delta > timedelta(minutes=30) and time_delta <= timedelta(hours=1):
        price = 4.00
        return round(price, 2)
    
    elif time_delta > timedelta(hours=1) and time_delta <= timedelta(hours=1, minutes=30):
        price = 7.00
        return round(price, 2)
    
    elif time_delta > timedelta(hours=1, minutes=30) and time_delta <= timedelta(hours=2):
        price = 8.00
        return round(price, 2)

    elif time_delta > timedelta(hours=2) and time_delta <= timedelta(hours=2, minutes=30):
        price = 11.00
        return round(price, 2)
    
    elif time_delta > timedelta(hours=2, minutes=30) and time_delta <= timedelta(hours=3):
        price = 12.00
        return round(price, 2)
    
    else:
        dif = time_delta - timedelta(hours=3)
        print(dif)
        dif_sec = dif.total_seconds()
        print(dif_sec)
        dif_hours = dif_sec / 3600
        print(dif_hours)
        price = 12 + (4 * dif_hours)
        return round(price, 2)

if __name__ == '__main__':
    from datetime import datetime

    date1 = datetime.now()
    date2 = datetime.strptime('6-3-2025 15:00', '%d-%m-%Y %H:%M')

    time_delta = date1 - date2
    print(time_delta)

    result = price_calculator(time_delta)

    print(result)
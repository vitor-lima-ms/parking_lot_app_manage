def price_calculator(time_delta):
    """Function to calculate the price to be paid"""

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

def cpf_validator(cpf):
    """Function to validate the CPF"""

    '''Collect the sum of the first 9 digits of the CPF, multiplying each of the values ​​by a countdown starting from 10, add all the results of this multiplication'''
    sum_9_digits = 0
    counter_1 = 10
    for digit_1 in cpf:
        if counter_1 == 1:
            break
        
        digit_X_counter_1 = int(digit_1) * counter_1

        sum_9_digits += digit_X_counter_1

        counter_1 -=1

    '''Multiply the previous result by 10'''
    sum_9_digits_X_10 = sum_9_digits * 10

    '''Get the remainder of the division by 11 of the previous account'''
    div_remainder_11_1 = sum_9_digits_X_10 % 11

    '''If previous result > 9 --> 0. Otherwise --> previous result'''
    if div_remainder_11_1 > 9:
        first_digit = 0
    else:
        first_digit = div_remainder_11_1

    '''To calculate the second digit, the process is practically the same, with the exception that the first digit has to be included in the calculations'''
    sum_10_digits = 0
    counter_2 = 11
    for digit_2 in cpf:
        if counter_2 == 1:
            break
        
        digit_X_conunter_2 = int(digit_2) * counter_2

        sum_10_digits += digit_X_conunter_2

        counter_2 -=1

    '''Multiply the previous result by 10'''
    sum_10_digits_X_10 = sum_10_digits * 10

    '''Get the remainder of the division by 11 of the previous account'''
    div_remainder_11_2 = sum_10_digits_X_10 % 11

    '''If previous result > 9 --> 0. Otherwise --> previous result'''

    if div_remainder_11_2 > 9:
        second_digit = 0
    else:
        second_digit = div_remainder_11_2

    '''Checking if the CPF is valid'''
    penultimate_digit_user_cpf = int(cpf[-2])
    last_digit_user_cpf = int(cpf[-1])

    first_condition = penultimate_digit_user_cpf == first_digit
    second_condition = last_digit_user_cpf == second_digit

    if first_condition and first_condition:
        if cpf.count(cpf[0]) == 11:
            return False
        else:
            return True
    return False

if __name__ == '__main__':
    ...
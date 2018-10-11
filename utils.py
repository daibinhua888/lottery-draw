
def inRange(fromNumber, endNumber, number1, number2, number3):
    numbers_sum = number1*100 + number2*10 + number3
    if numbers_sum >= fromNumber and numbers_sum <= endNumber:
        return True
    return False

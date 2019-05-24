from datetime import date

def period_is_late(last=None, today=None, cycle_length=None):
    
    """
    In this kata, we will make a function to test whether a period is late.

    Our function will take three parameters:

    last - The Date object with the date of the last period

    today - The Date object with the date of the check

    cycleLength - Integer representing the length of the cycle in days

    If the today is later from last than the cycleLength, the function should return true. We consider it to be late if the number of passed days is larger than the cycleLength. Otherwise return false.    
    """
    
    lastdate = last
    todaydate = today
    
    if (todaydate - lastdate).days > cycle_length:
        return True
    else:
        return False

if __name__ == "__main__":
    period_is_late()        
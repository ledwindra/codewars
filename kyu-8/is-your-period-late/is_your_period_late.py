from datetime import date

def is_late(last, today, cycle_length):
    
    lastdate = last
    todaydate = today
    
    return (todaydate - lastdate).days > cycle_length   
from datetime import datetime
from datetime import timedelta
now = datetime.now()

current_time = now.strftime("%c")
timechanger=timedelta(days=100,minutes=13,hours = 10)
timechanger1=timedelta(seconds=-60)
timechanger2=timedelta(weeks =-104)

changedtime1=((now+timechanger1).strftime("%c"))
changedtime2=((now+timechanger2).strftime("%c"))
changedtime3 =((now+timechanger).strftime("%c"))
print("Current Time  is", current_time)
print("Changed Time  is", changedtime1)
print("Changed Time  is", changedtime2)
print("Changed Time  is", changedtime3)
print(timechanger)
def addfni(feet,inches):
    current_datetime =datetime.now()
    print("Date and Time currrently is  ")
    tfeet=feet+(inches/12)
    print("Feet",tfeet)

addfni(8,10)
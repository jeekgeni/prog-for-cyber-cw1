#ask user for time in GMT and output PST and CET zones.
#prompting user to use 24 hour time
from datetime import datetime, timedelta

gmt = input("Enter GMT time(HH:MM):")   

#import datetime to let python understand it as a time
time = datetime.strptime(gmt, "%H:%M")
#imnported and using time delta to show difference in time between time zones
cet = time + timedelta(hours=1)
pst = time + timedelta (hours=8)
print("CET:", cet.strftime("%H:%M"))
print("PST:", pst.strftime("%H:%M"))

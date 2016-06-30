import time
from datetime import datetime

while (1):
  now = datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second

  day = datetime.today().weekday()

  if hour == 7 and minute = >= 0 and day < 5:
    print "It's 7:00 on a weekday"

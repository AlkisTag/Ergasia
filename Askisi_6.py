import calendar
def intCheck(mes):
  while True:
    try:
       Input = int(input(mes))       
    except ValueError:
       print("Come on all i'm asking is a legit number.")
       continue
    else:
       return Input 
       break

xronos=(intCheck("Gimme the year:\n"))
mhnas=(intCheck("Gimme a month:\n"))
print(calendar.month(xronos, mhnas))
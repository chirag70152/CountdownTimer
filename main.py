import time

a = int(input("How many seconds do you want the timer for?\n"))

while a:
    mins = a//60
    secs = a%60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer)
    time.sleep(1)
    a -= 1

print("Times Up!")
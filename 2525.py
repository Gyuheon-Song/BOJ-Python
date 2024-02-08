hour, minute = map(int, input(). split())
time = int(input())

if minute + time >= 60 :
    hour += ((minute + time)//60)
    minute = (minute + time)%60
    if hour < 24 :
        print(hour, minute)
    else :
        hour -= 24
        print(hour, minute)

else :
    print(hour, minute + time)
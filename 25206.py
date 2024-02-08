score_dict = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
}

multi = []
time_list = []
for i in range(20):
    subject, time, score = map(str, input(). split())
    time = float(time)
    if score in score_dict.keys() :
        mul = time*float(score_dict[score])
        multi.append(mul)
        time_list.append(time)
        
print(sum(multi)/sum(time_list))



 

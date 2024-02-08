king, stone, n = map(str, input(). split())

kingans = [ord(king[0]), int(king[1])]
stoneans = [ord(stone[0]), int(stone[1])]

d = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

for _ in range(int(n)) :
    cmd = input()
    if cmd == "T" :
        tmp = d[0]
    elif cmd == "RT" :
        tmp = d[1]
    elif cmd == "R" :
        tmp = d[2]
    elif cmd == "RB" :
        tmp = d[3]
    elif cmd == "B" :
        tmp = d[4]
    elif cmd == "LB" :
        tmp = d[5]
    elif cmd == "L" :
        tmp = d[6]
    else :
        tmp = d[7]

    kingans[0] += tmp[1]
    kingans[1] += tmp[0]

    if kingans[0] < 65 or kingans[0] > 72 or kingans[1] < 1 or kingans[1] > 8 :   
        kingans[0] -= tmp[1]
        kingans[1] -= tmp[0]
    
    elif kingans[0] == stoneans[0] and kingans[1] == stoneans[1] :
        stoneans[0] += tmp[1]
        stoneans[1] += tmp[0]
        if stoneans[0] < 65 or stoneans[0] > 72 or stoneans[1] < 1 or stoneans[1] > 8 :
            stoneans[0] -= tmp[1]
            stoneans[1] -= tmp[0]
            kingans[0] -= tmp[1]
            kingans[1] -= tmp[0]

print(chr(kingans[0]), kingans[1], sep = "")
print(chr(stoneans[0]), stoneans[1], sep = "")


n,c=map(int,input().split())
conflict_lst=[]
for i in range(c):
    temp=tuple(map(int,input().split()))
    conflict_lst.append(temp)

exp_lst=list(map(int,input().split()))

d={}
for i in range(len(exp_lst)):
    d[exp_lst[i]]=i+1
#print(conflict_lst)
#print(d)

exp_lst.sort(reverse=True)
#print(exp_lst)
sum=exp_lst[0]
team=[d[exp_lst[0]]]
#print(team)

for i in range(1,len(exp_lst)):
    len_t=len(team)
    #print(len_t)
    flag=True
    ch=0
    while ch<len_t:
        #print((d[exp_lst[i]],team[ch]),(team[ch],d[exp_lst[i]]))
        if(d[exp_lst[i]],team[ch]) not in conflict_lst:
            if((team[ch],d[exp_lst[i]]) not in conflict_lst):
                ch+=1
                Flag=True
                continue
                # sum+=exp_lst[i]
                # team.append(d[exp_lst[i]])
                # print(team)
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag:
        sum+=exp_lst[i]
        team.append(d[exp_lst[i]])
        #print(team)

#print(team)
print(sum)
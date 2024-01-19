n,c=map(int,input().split()) 
conflict_lst=[]
for i in range(c):
    temp=tuple(map(int,input().split()))
    conflict_lst.append(temp)

exp_lst=list(map(int,input().split())) 
if n>=1 and n<=1000:
    if c>=0 and c<=100:
        if len(conflict_lst)>=1 and len(conflict_lst)<=10**4:
            

            d={} 
            for i in range(len(exp_lst)):
                d[exp_lst[i]]=i+1


            exp_lst.sort(reverse=True)
            sum=exp_lst[0]
            team=[d[exp_lst[0]]] 


            for i in range(1,len(exp_lst)): 
                len_t=len(team)
                flag=True
                ch=0
                while ch < len_t:
                    if (d[exp_lst[i]], team[ch]) not in conflict_lst and (team[ch], d[exp_lst[i]]) not in conflict_lst:
                        ch += 1
                    else:
                        flag = False
                        break
                if flag:
                    sum += exp_lst[i]
                    team.append(d[exp_lst[i]])

            sumstr=str(sum)        
            print(sumstr.strip())
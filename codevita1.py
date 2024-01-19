def compute_valency(ele):
    num=ord(ele)
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num



def balance_compound(compound, equivalent_point):
    element1, element2 = compound[0], compound[1]
    
    valency1 = compute_valency(element1)
    valency2 = compute_valency(element2)
    
    flag=True
    end=(equivalent_point//valency2)+1
    for i in range(1,end):
        x=valency2*i
        remaining=equivalent_point-x
        
        if remaining%valency1 == 0:
            y = remaining//valency1
            if y!=0:
                print(f"{element1}{y} {element2}{i}")
                flag=False 
    if flag:
        print("Not Possible") 

compound = input().strip()
equivalent_point = int(input().strip())

# Output
balance_compound(compound, equivalent_point)

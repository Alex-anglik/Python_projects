list=[1,6,8,22,54,77,82,99]

def binary_search(list, num, low, high ):
    
    if high>=low:
        middle=low + (high-low)//2
        if list[middle]==num:  
            return middle

        elif num > list[middle]:
            return binary_search(list, num, middle+1, high)
        
        elif num< list[middle]:
            return binary_search(list, num, low, middle-1)
    else:
        return -1
            
num=int(input("what numbers' index do you want to find?"))
index = binary_search(list, num, 0, len(list)-1 )

if index==-1:
    print("number not in list")
else:
    print("the number", str(num), "is at index", str(index))
import array
def insertElement(arr,x,pos):
    n=len(arr)
    
    if pos<0 or pos>n:
        
        raise IndexError("position our of range")
    new_arr=array.array(arr.typecode,[0]*(n+1))
        
    for i in range(pos):
         new_arr[i+1]=arr[i]
    new_arr[pos]=x
    for i  in range (pos,n):
         new_arr[i+1]=arr[i]
    
    return new_arr
    
arr=array.array['i',[1,2,34,5,7,8]]                            
x=12
pos=2

arr=insertElement(arr,x,pos)
print(arr.tolist())



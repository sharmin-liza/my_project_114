class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
    
if __name__=='__main__':
    head=Node(10)
    a=Node(40)
    head.next =a 
    print(head.val)
    print(head.next.val)
    print(a.val)
    
    

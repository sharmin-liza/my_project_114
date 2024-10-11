class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
if __name__=="__main__":
    head=Node(20)
    a=Node(34)
    b=Node(45)
    c=Node(30)
    d=Node(78)

    head.next=a
    a.next=b
    b.next=c
    c.next=d
    temp=head
    while temp is not None:
        print(temp.val)
        temp=temp.next
        

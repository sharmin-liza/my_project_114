class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
if __name__=="__main__":
    a=Node(34)
    b=Node(55)
    a.next=b
    b.next=None

    print(a.val)
    print(b.val)
    print(a.next.val)

def func():
    c=input()
    n,d=map(int,c.split())
    list1=[""]*n
    e=input()
    list1=list(map(int,e.split()))
    list1=(list1[d:] + list1[:d]) 
    print(*list1,sep=' ')
func()
# right rotation
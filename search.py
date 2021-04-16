def poisk(a, n): #итеративный подход
    first=0
    last=len(a)-1
    mid=len(a)//2
    while first<=last:
        if element>a[mid]:
            first=mid+1
        elif element<a[mid]:
            last=mid-1
        elif element==a[mid]:
            return mid
        mid=(last+first)//2
    if first > last:
        return None
def recursion_poisk(a, first, last): #рекурсивный подход
    mid = (first+last) // 2
    while first!=last and first<=last:
        if element>a[mid]:
            return recursion_poisk(a, mid+1, last)
        elif element==a[mid]:
            return mid
        return recursion_poisk(a, first, mid-1)
    return None
a = list(map(int, input().split()))
n=len(a)
element=int(input())
print(poisk(a,n))
first=0
last=len(a)-1
print(recursion_poisk(a, first, last))

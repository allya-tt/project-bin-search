import time
start_time = time.time()
def poisk(a): #итеративный подход
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
    mid = first+(last-first) // 2
    while first<=last:
        if element>a[mid]:
            return recursion_poisk(a, mid+1, last)
        elif element==a[mid]:
            return mid
        return recursion_poisk(a, first, mid-1)
    return None
a = list(map(int, input().split())) #список чисел
element=int(input()) #элемент, который нужно найти
print(poisk(a))
first=0
last=len(a)-1
print(recursion_poisk(a, first, last))
print("%s seconds " % (time.time() - start_time))

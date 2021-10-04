def lsearch(list, number):
    for i in range(0, len(list)):
        if list[i] == number:
            return i
    return None



def verify(result):
    if result is not None:
        print("Number is found at", result+1)
    else:
        print("Number is not in list ")



def main():
    num=int(input("Enter the number to be searched"))
    list=[]

    n=int(input("Enter the number of elements"))
    for i in range(0,n):
        e=int(input())
        list.append(e)
    result = lsearch(list, num)
    verify(result)

if __name__=="__main__":
    main()

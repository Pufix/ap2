import random
def clean():
    for w in range(200):
        print('\n')
list=[-1]
step =1
crtstep=0
def genlist():
    n=int(input("Plese scecify how big the size is: "))
    size=len(list)
    for i in range (n):
        if i>= size:
            list.append(random.randint(1,99))
        else:
            list[i]=random.randint(1,99)
    while len(list)>n:
        list.pop()
def showstep():
    print(list)
def sort1():
    global step
    showstep()
    stepcrt=0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                c=list[i]
                list[i]=list[j]
                list[j]=c
                stepcrt+=1
                if stepcrt%step==0:
                    showstep()
                    stepcrt=0

def sort2(mylist):
    global step
    global crtstep
    if len(mylist)>1:
        mid=int(len(mylist)/2)
        left=mylist[:mid]
        right=mylist[mid:]
        sort2(left)
        sort2(right)
        i=0
        j=0
        k=0
        crtstep+=1
        if crtstep%step==0:
            print(mylist,end =" -> ")
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                mylist[k]=left[i]
                i+=1
            else:
                mylist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            mylist[k]=left[i]
            i+=1
            k+=1    
        while j<len(right):
            mylist[k]=right[j]
            j+=1
            k+=1
        if crtstep%step==0:
            print(mylist)
            crtstep=0
def interface():
    global step
    print("1.Generate a random list.")
    if list[0]!=-1:
        print("Curent list is:")
        print(list)
    print("2.Sort the list using 2 For Sorting")
    print("3.Sort the list using Merge Sort")
    print("4.Change step (current step size="+str(step)+")")
    print("0.Exit program")
    nr = int(input("Type the letter of the desired opperation followed by an enter to select it"+'\n'))
    if nr!=0:
        if nr==1:
            genlist()
            clean()
        elif nr==2:
            if list[0]!=-1:
                clean()
                sort1()
                print('\n')
            else:
                clean()
                print("Please generate list first!")
        elif nr==3:
            if list[0]!=-1:
                clean()
                sort2(list)
                print('\n')
            else:
                clean()
                print("Please generate list first!")
        elif nr==4:
            step= int(input("Please enter step size: "))
            clean()
        else:
            print("Please enter a valid number!")
        interface()
clean()
interface()

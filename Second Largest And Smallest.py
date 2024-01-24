def find_len(listA):
    length = len(listA)
    listA.sort()
    
    print("Second Largest element is:", listA[length-2])
    print("Second Smallest element is:", listA[1])
 
listA = []

n = int(input("Enter number of elements in the list : "))

listA = list(map(int,input("Enter the numbers : ").strip().split(',')))[:n]
print("The entered list is: \n",listA)
Largest = find_len(listA)
 

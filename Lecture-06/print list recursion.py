def print_list(list,idx=0):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list,idx+1)
list=[]
size=int(input("Enter the size of the list: "))
for i in range(size):
    list.append(input("Enter the element: "))
print_list(list)
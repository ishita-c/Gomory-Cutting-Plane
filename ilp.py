all_input=[]
def read_input(filename):
    file = open(filename, 'r')
    Lines = file.readlines()
    for line in Lines:
        l=list(map(int, line.split()))
        if(l!=[]):
            all_input.append(l)

def gomory(filename):
    read_input(filename)
    if(len(all_input)==0):
        print("Error: Empty Input File!")
        return -1
    n=all_input[0][0]
    if(len(all_input[0])!=2):
        print("Error: Provide m and n in the same line!")
        return -1
    m=all_input[0][1]
    if(n<0 or m<0 or n>18 or m>18):
        print("Error: m or n out of bound!")
        return -1
    if(len(all_input[1])!=m):
        print("Error: Provide m elements for b!")
        return -1
    b=all_input[1]
    if(len(all_input[2])!=n):
        print("Error: Provide n elements for c!")
        return -1
    c=all_input[2]
    if(len(all_input)!=m+3):
        print(len(all_input))
        print("Error: Provide m rows for a!")
        return -1
    row=3
    while row<m+3:
        if(len(all_input[3])!=n):
            print("Error: Provide n elements for ",row,"th row")
            return -1
        row+=1
    a=all_input[3:]
    print("input recieved successfully")
    

filename=input()
gomory(filename)


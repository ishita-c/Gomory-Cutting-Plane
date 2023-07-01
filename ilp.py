import numpy as np
import sys



def read_input(filename, all_input):
    file = open(filename, 'r')
    Lines = file.readlines()
    for line in Lines:
        l=list(map(int, line.split()))
        
        if(l!=[]):
            all_input.append(l)

def gomory(filename):
    all_input=[]
    read_input(filename, all_input)
    if(len(all_input)==0):
        #print("Error: Empty Input File!")
        return -1
    n=all_input[0][0]
    if(len(all_input[0])!=2):
        #print("Error: Provide m and n in the same line!")
        return -1
    m=all_input[0][1]
    if(n<0 or m<0 or n>18 or m>18):
        #print("Error: m or n out of bound!")
        return -1
    if(len(all_input[1])!=m):
        #print("Error: Provide m elements for b!")
        return -1
    b=all_input[1]
    if(len(all_input[2])!=n):
        #print("Error: Provide n elements for c!")
        return -1
    c=all_input[2]
    #if(len(all_input)!=m+3):
        #print(len(all_input))
    #    print("Error: Provide m rows for a!")
    #    return -1
    row=3
    while row<m+3:
        if(len(all_input[3])!=n):
            #print("Error: Provide n elements for ",row,"th row")
            re
            turn -1
        row+=1
    a=all_input[3:]
    

    return form_tableau(b,c,a,m,n)
   

def form_tableau(b, c, A, m, n):
    num_var=n
    tableau = [] 
    basic_var = []
    y = n+1
    for x in range(m):
        basic_var.append(y)
        y+=1
    initial_soln = b

    cost_row = []
    cost_row.append(0)                 # -CbT Ab(-1) b
    for x in range(n):                 # Cj^
        #y = c[x]
        cost_row.append(c[x])
        #y+=1
    for x in range(m):
        cost_row.append(0)

    tableau.append(cost_row)
    for x in range(m):
        row = []
        row.append(initial_soln[x])
        for y in range(n):
            row.append(A[x][y])
        Identity_mat = np.identity(m, dtype = float)
        for y in range(m):
            row.append(Identity_mat[x][y])

        tableau.append(row)

    return primal_tableau(tableau, basic_var, num_var)
    #return tableau and basic_var

def primal_row_ops(tableau, row_pivot, col_pivot):
    divide_by = float(tableau[row_pivot][col_pivot])
    for i in range(len(tableau[0])):
        tableau[row_pivot][i] = (float(tableau[row_pivot][i]))/divide_by
        #tableau[row_pivot][i] = round(tableau[row_pivot][i] , 3)
    itr = 0
    while(itr<len(tableau)):
        if(itr != row_pivot):
            subtract = tableau[itr][col_pivot]
            for i in range(len(tableau[0])):
                tableau[itr][i] = tableau[itr][i] - (subtract*tableau[row_pivot][i])
        itr +=1
    return tableau


def primal_tableau(tableau, basic_var, num_var):
    while(True):
        row_pivot = -1
        col_pivot = -1
        m = len(tableau)
        n = len(tableau[0])
        for x in range(1,n):
            if (tableau[0][x] > 0):             #coz maximization prob
                col_pivot = x
                break

        if(col_pivot != -1):
            mini = float('inf')
            min_elem = float('inf')
            for y in range(1,len(tableau)):
                if(tableau[y][col_pivot]>0):
                    ratio = float(tableau[y][0]/tableau[y][col_pivot])
                    if(ratio < mini):
                        mini = ratio
                        min_elem = y
            row_pivot = min_elem            #index in tableau
        else:
            soln = [0 for element in range(n - 1)]
            for y in range(m - 1):
                soln[basic_var[y]-1] = tableau[y+1][0]
            is_fractional=False
            for basic_index in basic_var:
              
                if round(soln[basic_index-1],3)-int(soln[basic_index-1])!=0:
               
                    is_fractional=True
                    return gomory_cut(tableau, basic_var, num_var)
                    
            if is_fractional==False:
                return soln[:num_var]
              
                
        
        if (row_pivot != -1):
            basic_var[row_pivot - 1] = col_pivot
            tableau = primal_row_ops(tableau, row_pivot, col_pivot)
        
    
def gomory_cut(tableau, basic_var, num_var):

    r=len(tableau)
    c=len(tableau[0])
    max_fr=0
    max_row=-1
    for row in range(1, r):
        if tableau[row][0]-int(tableau[row][0])>max_fr:
            max_fr=tableau[row][0]-int(tableau[row][0])
            max_row=row
    new_row=[]
    for col in range(0, c):
        fr=tableau[max_row][col]-int(tableau[max_row][col])
        if fr<0:
            fr+=1
        new_row.append(-1*fr)
    new_row.append(1)
    for row in range (len(tableau)):
        tableau[row].append(0)
    tableau.append(new_row)
    basic_var.append(len(tableau[0])-1)
   
    return dual_primal(tableau, basic_var, num_var)

def dual_find_leaving_basis(tableau):
    rows=len(tableau)
    min_xb=0
    min_row=-1
    for r in range (1, rows):
        if tableau[r][0]<min_xb:
            min_xb=tableau[r][0]
            min_row=r
    return min_row

def dual_find_entering_basis(tableau, row):
    cols=len(tableau[0])
    pivot_col=-1
    is_pos=False
    for c in range (1, cols):
        if tableau[row][c]!=0 and -1*tableau[0][c]/float(tableau[row][c])>0:
            is_pos=True
    if is_pos==False:
        min_pos=-999999
        for c in range (1, cols):
           
            if tableau[row][c]!=0 and -1*tableau[0][c]/float(tableau[row][c])<0 and -1*tableau[0][c]/float(tableau[row][c])>min_pos and -1*tableau[0][c]/float(tableau[row][c])!=min_pos:
                min_pos=-1*tableau[0][c]/float(tableau[row][c])
                pivot_col=c
    else:
        min_pos=999999
        for c in range (1, cols):
           
            if tableau[row][c]!=0 and -1*tableau[0][c]/float(tableau[row][c])>0 and -1*tableau[0][c]/float(tableau[row][c])<min_pos and -1*tableau[0][c]/float(tableau[row][c])!=min_pos:
                min_pos=-1*tableau[0][c]/float(tableau[row][c])
                pivot_col=c


    return pivot_col

def dual_primal(tableau, basic_var, num_var):
    
    leaving_row=dual_find_leaving_basis(tableau)
    pivot_col=dual_find_entering_basis(tableau, leaving_row)
   
    
    basic_var[leaving_row-1]=pivot_col
   
    primal_row_ops(tableau, leaving_row, pivot_col)
    

    for r in range (1, len(tableau)):
        if basic_var[r-1]<=num_var and basic_var[r-1]>=0 and (round(tableau[r][0], 3)-int(tableau[r][0])!=0):
            return gomory_cut(tableau, basic_var, num_var)

    for r in range (1, len(tableau)):
        if tableau[r][0]<0:
           
            leaving_row=r
            pivot_col=dual_find_entering_basis(tableau, leaving_row)
            basic_var[leaving_row-1]=pivot_col
            primal_row_ops(tableau, leaving_row, pivot_col)

    

    solution=[]
    row=1
    for basic_index in basic_var:
        solution.append([basic_index, int(tableau[row][0])])
        row+=1
    ans=[0]*num_var
    
    for item in solution:
        if item[0]<=num_var and item[0]>=1:
            ans[item[0]-1]=item[1]
    #print(ans)
    return ans


#filename=sys.argv[-1]
#print(gomory(filename))

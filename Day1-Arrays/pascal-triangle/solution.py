# Program to generate Pascal’s Triangle


# variation 1: gives number of rows and asks to print the pascal triangle

def printPascalTriangle(rows):
    if rows==0:
        return []
    triangle = [[1]]
    for i in range(1,rows):
        row = []
        row.append(1)
        for j in range(1,i):
            row.append(triangle[i-1][j-1]+triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle



#variation 2: gives row and column position print the value

def nCr(n,r):
    res =1 
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res 

def pascalTriangle(row,col):

    return nCr(col-1,row-1)


#variation 3: gives a row and print the entire row elements

def pascalTriangleRow(row):
    res = 1
    print(res,end=" ")
    for i in range(1,row):
        res = res * (row-i)
        res = res // (i)
        print(res,end=" ")
    print()

# pascalTriangleRow(5)



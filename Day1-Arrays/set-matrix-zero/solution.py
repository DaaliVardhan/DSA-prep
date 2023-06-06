# Set Matrix Zero

# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output: [[1,0,1],[0,0,0],[1,0,1]]


# Solution 1: Brute Force Approach


def setMatrixZero(matrix):
    rows=[-1 for i in range(len(matrix))]
    cols=[-1 for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==0):
                rows[i]=0
                cols[j]=0
    # print(rows,cols)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            if rows[i]==0 or cols[j]==0:
                matrix[i][j]=0
    print(matrix)
    return matrix 

def setMatrixZeroOptimized(matrix):
    temp = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0]=0

                if j!=0:
                    matrix[0][j] = 0
                else:
                    temp = 0 
    
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if(matrix[i][0] == 0 or matrix[0][j]==0):
                matrix[i][j]=0
    # print(matrix)
    if matrix[0][0]==0:
        for i in range(len(matrix[0])):
            matrix[0][i]=0
    if temp==0:
        for j in range(len(matrix)):
            matrix[j][0]=0 
    
    return matrix 

matrix = [[1,1,1],[1,0,1],[1,1,1]]
# output = [[1,0,1],[0,0,0],[1,0,1]]

setMatrixZeroOptimized(matrix)


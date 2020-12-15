'''
QUESTION:
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.

SOLUTION:
'''
####### OUR IMPLEMENTATION BEGINS HERE ##############

def setZeros(matrix):
    row = [False]*len(matrix)
    col = [False]*len(matrix[0])
    
    # store the row and col index with 0 value
    for row_ in range(len(matrix)):
        for col_ in range(len(matrix[0])):
            if matrix[row_][col_]==0:
                row[row_]=True
                col[col_]=True
                
    #nullify rows
    for i in range(len(row)):
        if row[i]: nullifyRow(matrix,i)
            
    #nullify cols
    for j in range(len(col)):
        if col[j]: nullifyCol(matrix,j)
            
    return matrix
    
def nullifyRow(matrix,row):
    for j in range(len(matrix[0])): # keep row constant and modify cols
        matrix[row][j]=0
        
def nullifyCol(matrix,col):
    for i in range(len(matrix)): # keep col constant and modify rows
        matrix[i][col] = 0
        
 ####### OUR IMPLEMENTATION ENDS HERE ##############   

#Driver Code
matrix = [[1,0,3],[4,5,6],[7,8,0]]
setZeros(matrix)
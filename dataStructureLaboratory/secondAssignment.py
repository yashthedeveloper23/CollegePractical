matrix1 = [[34, 13, 15], [41, 25, 36], [127, 238, 2339]]

inputMatrix1 = []

def enterValuesInMatrix(mat):
    r = int(input("enter the number of rows: "))
    c = int(input("Enter the number of cols: "))
    
    for i in range(rows):
        mat.append(i)

    



matrix2 = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]

result1 = [[0,0,0],
        [0,0,0],
        [0,0,0]]


result2 = [[0,0,0],
        [0,0,0],
        [0,0,0]]



for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result1[i][j] = matrix1[i][j] + matrix2[i][j]

print("addition of two matrix!")
for r in result1:
    print(r)



for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result2[i][j] = matrix1[i][j] - matrix2[i][j]

print("subtraction of two matrix!")
for r in result2:
    print(r)
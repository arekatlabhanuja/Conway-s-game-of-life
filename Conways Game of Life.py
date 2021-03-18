import numpy as np
#Gets the valid neighbours of a particular index in the matrix
def getNeighbours(r, c, i, j):
    #initialising the 8 neighbouring nodes
    neighbours = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                  (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
    neighbours1 = []
    #checking if the neighbours are in the range of the matrix 
    for k in neighbours:
        if k[0] in range(0, r) and k[1] in range(0, c):
            neighbours1.append(k)
    return neighbours1

#Checks the neighbours of all the cells and updates the grid 
def getCurrentState(arr):
    #Creating the shape of the array
    arr1 = np.zeros(arr.shape[0] * arr.shape[1]).reshape(arr.shape[0], arr.shape[1])
    #For each cell gets the neighbours and checks the conditions to decide whether to 
    #activate or deactivate or leave the cell in the same condition
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            neighbours = getNeighbours(arr.shape[0], arr.shape[1], i, j)
            cnt = 0
            for k in neighbours:
                if arr[k[0]][k[1]] == 1:
                    cnt += 1
            if arr[i][j] == 0 and cnt == 3:
                arr1[i][j] = 1
            elif arr[i][j] == 1 and cnt < 2:
                arr1[i][j] = 0
            elif arr[i][j] == 1 and cnt > 3:
                arr1[i][j] = 0
            elif arr[i][j] == 1 and (cnt == 2 or cnt == 3):
                arr1[i][j] = 1
    return arr1


if __name__ == "__main__":
    try:
        n = int(input('Enter square matrix size (default will be 5) :'))
    except ValueError:
        print("Invalid input value 5 is taken")
        n = 5
    arr = np.zeros(n * n).reshape(n, n)

    try:
        num_replaced = int(input('Enter the random number of cells to be activated at first (default will be 15) :'))
    except ValueError:
        print("Invalid input value 15 is taken")
        num_replaced = 15
    
    #Generating the random number of cells.
    indices_x = np.random.randint(0, arr.shape[0], num_replaced)
    indices_y = np.random.randint(0, arr.shape[1], num_replaced)

    arr[indices_x, indices_y] = 1

    print(f"The Input array is :\n{arr}")

    try:
        iterations = int(input('Enter the number of iterations (default will be 1) :'))
    except ValueError:
        iterations = 1

    #Calculating the new grid and priting it
    for i in range(iterations):
        arr = getCurrentState(arr)
        print(f'The iteration number {i + 1} is :\n{arr}')

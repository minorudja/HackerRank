def checkIfWithinImage(x, y, image):
    if (0 <= x < len(image)) and (0 <= y <= len(image[0])):
        return True
    else:
        return False

def morphErosion(elemS, elemSOrigin, image, rows, cols):
    erosionImg = [[0 for i in range(cols)] for j in range(rows)]
    elemSRelCoords = []
    for r in range(len(elemS)):
        for c in range(len(elemS[0])):
            if (r,c) != elemSOrigin:
                elemSRelCoords.append([r-elemSOrigin[0],c-elemSOrigin[1]])
    
    for i in range(rows):
        for j in range(cols):
            if image[i][j] == 1:
                containFlag = True
                for coord in elemSRelCoords:
                    if not containFlag:
                        break

                    if checkIfWithinImage(i+coord[0],j+coord[1],image):
                        if image[i+coord[0]][j+coord[1]] != elemS[elemSOrigin[0]+coord[0]][elemSOrigin[1]+coord[1]]:
                            containFlag = False
                    else:
                        containFlag = False

                if containFlag:
                    erosionImg[i][j] = 1
                else:
                    erosionImg[i][j] = 0

    return erosionImg


## Main Program
image = [[0,0,0,0,0,0,0,0,0,0],
         [0,1,1,1,1,1,1,1,0,0],
         [0,0,0,0,1,1,1,1,0,0],
         [0,0,0,0,1,1,1,1,0,0],
         [0,0,0,1,1,1,1,1,0,0],
         [0,0,0,0,1,1,1,1,0,0],
         [0,0,0,1,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0]]
         
elemS = [[1,1,1],
         [1,1,1],
         [1,1,1]]

elemSOrigin = (1,1)
rows, cols = (len(image),len(image[0]))

erosionImg = morphErosion(elemS, elemSOrigin, image, rows, cols)

noPixelOnes = 0
for ind in range(rows):
    # print(erosionImg[ind])
    noPixelOnes += erosionImg[ind].count(1)

print(noPixelOnes)
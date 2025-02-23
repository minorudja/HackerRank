def checkWithinImage(i,j,image):
    if (0 <= i < len(image)) and (0 <= j < len(image[0])):
        return True
    else:
        return False
        
def findMax2D(arr):
    return(max([max(arr[i]) for i in range(len(arr))]))

def reassignObjID(objID, ind_arr, segImage):
    for ind in ind_arr:
        segImage[ind[0]][ind[1]] = objID

    return segImage

def reconfigureSegImage(largerObjID, segObj, segImage):
    maxObjID = findMax2D(segImage)
    for id in range(largerObjID+1, maxObjID+1):
        ptsList = segObj[id-1]
        for pts in ptsList:
            segImage[pts[0]][pts[1]] -= 1

    return segImage

def segImage4Connectivity(i,j,image,segImage,segObj):
    incrementArr = [[0,1],[1,0],[0,-1],[-1,0]]
    
    for ind in range(len(incrementArr)):
        nb_r = i + incrementArr[ind][0]
        nb_c = j + incrementArr[ind][1]
        if checkWithinImage(nb_r, nb_c, image):
            if segImage[nb_r][nb_c] > 0:
                if (segImage[i][j] > 0) and (segImage[i][j] != segImage[nb_r][nb_c]):
                    largerObjID = max(segImage[i][j],segImage[nb_r][nb_c])
                    smallerObjID = min(segImage[i][j],segImage[nb_r][nb_c])

                    largerObjList = segObj[largerObjID-1]

                    segImage = reconfigureSegImage(largerObjID, segObj, segImage)
                    segObj.remove(segObj[largerObjID-1])

                    segImage = reassignObjID(smallerObjID, largerObjList, segImage)
                    for pts in largerObjList:
                        if pts not in segObj[smallerObjID-1]:
                            segObj[smallerObjID-1].append(pts)
                else:
                    segImage[i][j] = segImage[nb_r][nb_c]
                    if (i,j) not in segObj[segImage[nb_r][nb_c]-1]:
                        segObj[segImage[nb_r][nb_c]-1].append((i,j))
                    
    if segImage[i][j] == 0:
        segImage[i][j] = findMax2D(segImage)+1
        segObj.append([(i,j)])
        
    return segImage

## Main Program
image = [[0,0,0,1,1,0,0,0,1,0,1,0],
         [1,1,1,0,1,1,1,1,0,0,0,1],
         [1,1,1,0,1,0,0,1,0,0,1,0],
         [1,0,0,0,0,0,0,0,0,1,0,0]]

rows, cols = (len(image),len(image[0]))
segImage = [[0 for i in range(cols)] for j in range(rows)]
segObj = []

for i in range(rows):
    for j in range(cols):
        if image[i][j] == 1:
            segImage = segImage4Connectivity(i,j,image,segImage,segObj)

# for imgInd in range(len(segImage)):
#     print(segImage[imgInd])

print(findMax2D(segImage))
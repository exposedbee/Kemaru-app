WIDTH = 600
HEIGHT = 600
STARTTEXTSIZE = 40
FINISHTEXTSIZE = 20

#colors
LIGHTGRAY = (105,105,105)
WHITE = (255,255,255)
BLACK = (0,0,0)
COLORSTART = (0,0,0)
DARKBLUE = (0,0,139)
LIGHTBLUE = (96,216,232)
LOCKEDCELLCOLOUR = (189,189,189)
INCORRECTCELLCOLOUR = (192,121,121)


#Position and sizes
gridPos = (75,100)
cellSize = [50,75]
gridSize =450
val = [50,75]

cellSize2= 75
gridSize2 = cellSize2*6

#start buttons
s1 =100
s2 =40

# Bords

hardBoard1 = [[0,0,0,0,0,0,0,0,3], [2,4,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,3], [0,4,0,0,3,0,0,0,0], [0,0,2,0,0,0,0,4,0],[0,0,0,0,5,0,0,0,0], [0,0,0,0,0,2,0,0,3],[0,0,0,0,4,0,0,0,0],  [0,5,4,0,1,0,0,0,3]]
hardshape1 = [[00,10,1,11],[20,30,21,31,41],[40,50,60,70,80],[2,12,22,32],[42,52,51,61],[71,81,72,82],[62,63,73],[3,4,5,15],[13,23,33,14,24],[34,44,54,53,43],[83,84,85,75,74],[25,35,26,36],[46,45,55,65,64],[6,7,8,16],[17,18,27,37,28], [38,48],[58,68,78,88],[47,57,67,66,56],[76,86,77,87]]

hardfinishedBoard1 =[[3,1,2,4,2,1,5,4,3], [2,4,3,1,5,4,3,1,2], [3,1,2,3,2,1,2,4,3], [2,4,3,1,3,5,3,1,2], [1,5,2,4,2,1,2,4,3],  [4,3,1,3,5,4,3,5,1], [1,2,4,2,1,2,1,4,3], [4,5,1,3,4,5,3,2,1], [3,2,4,2,1,2,1,4,3]]

hardBoard2 = [[0,5,0,0,0,0,0,0,5], [0,3,0,0,0,0,4,0,0], [0,5,0,0,4,1,0,0,2], [0,0,0,0,0,0,0,0,0], [1,5,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,5], [2,0,0,0,0,0,0,0,0],  [0,0,0,0,0,0,0,0,4], [0,0,0,4,5,0,1,0,0]]

hardshape2 = [[1,00,10,20,30],[40,50,60,70,80],[11,21,31,41,51],[61,71,62,72,52],[81,82,83,84,85],[2,12,22,32,42],[3,4,5,15],[14,13,23,33,43],[53,63,73,74],[24,34,25,35],[44,45,55,54,64],[75,65,66,67,68],[78,88],[77,87,76,86],[58,57,56,47,48],[38,37,27,28],[7,17,8,18],[6,16,26,36,46]]

hardfinishedBoard2=[[1,5,2,3,4,3,1,2,5],    [4,3,4,1,2,5,4,3,1],[1,5,2,3,4,1,2,5,2],[2,3,4,1,2,3,4,1,3],[1,5,2,3,4,1,5,2,4],[4,3,4,1,2,3,4,3,5],[2,1,5,3,4,1,2,1,2],[3,4,2,1,2,3,5,3,4],    [2,1,3,4,5,4,1,2,1]]

hardBoard3 = [[1,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,3,1], [0,0,2,0,0,0,2,0,2], [2,0,0,0,0,0,0,0,0], [0,0,2,3,0,0,0,0,0], [0,0,0,0,0,0,0,3,0], [2,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,4], [2,1,0,0,0,0,1,0,0]]

hardshape3 = [[1,00,10,20,30],[40,50,60,70,80],[11,21,31,41,51],[61,71,62,72,52],[81,82,83,84,85],[2,12,22,32,42],[3,4,5,15],[14,13,23,33,43],[53,63,73,74],[24,34,25,35],[44,45,55,54,64],[75,65,66,67,68],[78,88],[77,87,76,86],[58,57,56,47,48],[38,37,27,28],[7,17,8,18],[6,16,26,36,46]]

hardfinishedBoard3=[[1,5,2,3,4,3,1,2,5],[4,3,4,1,2,5,4,3,1],[1,5,2,3,4,1,2,5,2],[2,3,4,1,2,3,4,1,3],[1,5,2,3,4,1,5,2,4], [4,3,4,1,2,3,4,3,5],[2,1,5,3,4,1,2,1,2],[3,4,2,1,2,3,5,3,4],[2,1,3,4,5,4,1,2,1]]



hardBoard4 = [[0,0,0,0,2,1,0,0,0,], [0,0,3,0,0,0,0,0,0,], [0,0,0,0,0,0,0,0,0,], [0,4,0,0,3,0,0,0,0,], [0,0,2,0,0,0,0,0,0,],  [0,0,0,0,5,0,0,0,0,],  [0,0,0,0,0,0,1,0,0,],  [0,0,0,3,0,5,0,0,0,],  [3,0,0,0,0,2,0,0,0,]]

hardshape4 = [[00,10,1,11],[20,30,21,31,41],[40,50,60,70,80],[2,12,22,32],[42,52,51,61],[71,81,72,82],[62,63,73],[3,4,5,15],[13,23,33,14,24], [34,44,54,53,43],[83,84,85,75,74],[25,35,26,36],[46,45,55,65,64],[6,7,8,16],[17,18,27,37,28],[38,48],[58,68,78,88],[47,57,67,66,56],[76,86,77,87]]

hardfinishedBoard4 =[[3,1,2,4,2,1,5,4,3,],  [2,4,3,1,5,4,3,1,2,],  [3,1,2,3,2,1,2,4,3,],  [2,4,3,1,3,5,3,1,2,],  [1,5,2,4,2,1,2,4,3,],  [4,3,1,3,5,4,3,5,1,],  [1,2,4,2,1,2,1,4,3,],  [4,5,1,3,4,5,3,2,1,], [3,2,4,2,1,2,1,4,3,]]

testBoard1=  [[2,0,0,0,5,0],  [0,0,4,3,0,0],  [3,0,0,0,0,0],  [0,0,0,0,0,3],  [0,0,5,0,0,0],  [5,0,0,0,0,1]]

testshape1= [[00,1,2,12,13],[10,20,11,21],[30,31,40,41,50],[51,52,42,43,33],[32,22,23],[3,4,5,15,14],[24,25,35,45,55],[34,44,54,53]]

finishedBoard1 =[[2,3,2,1,5,2],     [4,1,4,3,4,3],     [3,5,2,1,2,1],     [2,1,3,4,5,3],     [3,4,5,1,2,4],     [5,1,2,4,3,1]]

testBoard2=  [[5,1,0,0,0,0], [0,0,0,0,3,0], [0,5,0,2,0,0], [0,0,0,0,0,0], [0,0,0,0,1,0], [2,0,0,0,0,0]]

testshape2= [[00,10,20,30,40],[50,51],[1,11,2,12,22],[21,31,41,42,32],[52,53,43,33],[23,24],[3,13,4,14],[5,15,25,35,34],[44,54,45,55]]

finishedBoard2 =[[5,1,3,2,4,1],[4,2,4,1,3,2],[1,5,3,2,5,1], [2,4,1,4,3,2], [1,3,2,5,1,4], [2,4,1,3,2,3]]

testBoard3=  [[0,0,0,0,0,0],  [0,0,0,2,0,0],  [0,5,0,0,5,0],  [0,0,0,0,0,0],  [0,5,0,3,4,1],  [3,0,0,0,2,0]]


testshape3= [[00,10,20,30],[40,50],[1,11,2,3],[21,22,23,13,12],[31,41,51,42,52],[32,33,43],[4,5,15],[14,24,34,35,25],[44,45,55,54,53]]

finishedBoard3 =[[1,2,4,3,1,2], [4,3,1,2,4,3], [2,5,4,3,5,1], [1,3,2,1,2,3], [2,5,4,3,4,1], [3,1,2,1,2,5]]

testBoard4 = [[5,0,0,4,0,0], [0,0,1,0,0,0], [0,0,0,0,0,3], [0,1,0,0,0,0], [0,0,0,0,0,4], [0,3,4,0,0,0]]

testshape4 = [[00,1,2,3,4],[10,20,30,11,21],[40,50,51,41],[31,32,33,34,24],[23,22,12,13],[52,42,43,53,54],[55,45,44,35,25],[5,15,14]]

finishedBoard4 =[[5,2,5,4,2,3], [1,3,1,3,1,4], [2,4,2,4,2,3], [3,1,3,1,5,1], [4,2,5,2,3,4], [1,3,4,1,5,2]]

testBoard5 = [[5,0,0,0,0,0], [0,0,0,0,0,0],[4,0,0,4,0,0], [0,0,0,0,0,3], [0,0,0,0,1,0], [0,3,5,0,0,2]]

testshape5 = [[00,10,20,21,11],[30,40,41,31],[50,51],[1,2,12,22,23],[32,33,34,44,43],[42,52,53,54,55],[3,13,4,14,24],[5,15,25,35,45]]

finishedBoard5 =[[5,1,4,1,4,1], [3,2,3,2,3,2], [4,5,1,4,1,4], [2,3,2,5,2,3], [5,4,1,3,1,5], [1,3,5,2,4,2]]




mod1=[1,2,3,4,5]
mod2=[1,2,3,4]

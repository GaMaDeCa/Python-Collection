def getAllX(matrix,x):
    if len(matrix)==0:
        return None
    tm=type(matrix[0])
    if tm!=list and tm!=tuple:
        if x<len(matrix[0]):
            return [matrix[0][x]]
        else:
            return []
    X=[]
    for y in range(len(matrix)):
        my=matrix[y]
        if x<len(my):
            X.append(my[x])
    return X

def getDiagonalData(matrix,startY,startX,rightDirection=True,rotate=True):
    sY=startY
    sX=startX
    dd=[]
    direction=1 if rightDirection else -1
    for y in range(sY,len(matrix)):
        my=matrix[y]
        if sX>=0 and sX<len(my):
            dd.append(my[sX])
            sX+=direction
        if not(sX>=0 and sX<len(my)):
            if rotate:
                sX=0 if rightDirection else len(my)-1
            else:
                return dd
    return dd

def sortX(matrix):
    for y in range(len(matrix)):
        try:
            matrix[y].sort()
        except:
            continue
    return matrix

def sortY(matrix,lenght=None):
    x=0
    if lenght==None:lenght=len(matrix[0])
    while x<lenght:
        sortedData=[]
        for y in range(len(matrix)):
            sortedData.append(matrix[y][x])
        sortedData.sort()
        for y in range(len(sortedData)):
            matrix[y][x]=sortedData[y]
        x+=1
    return matrix

def transpose(matrix):
    transposed=[]
    for data in matrix:
        maxLen=-1
        lenght=len(data)
        if lenght>maxLen:maxLen=lenght
    for ml in range(maxLen):
        data=[]
        for i in range(len(matrix)):
            if ml<len(matrix[i]):
                data.append(matrix[i][ml])
        transposed.append(data)
    return transposed

def matrixIndexer(matrix):
    maxLen=0
    for y in range(len(matrix)):
        lm=len(matrix[y])
        if lm>maxLen:maxLen=lm
        matrix[y].insert(0,y+1)
    xIndex=[i for i in range(maxLen+1)]
    matrix.insert(0,xIndex)
    return matrix

def gerarMatrixOrdenada(z,largura,altura):
    matrix=[]
    for y in range(z,altura+z):
        w=0
        dados=[]
        for x in range(largura):
            dados.append(y+w)
            w+=1
        matrix.append(dados)
    return matrix

def printMatrix(matrix,comBrackets=True,espaco=' '):
    if comBrackets:print('[')
    for y in range(len(matrix)):
        my=matrix[y]
        if comBrackets:print('\t[',end='')
        for x in range(len(my)):
            myx=my[x]
            print(myx,end=(',' if x<len(my)-1 else'')if comBrackets else espaco)
        print((']'+(',' if y<len(matrix)-1 else ''))if comBrackets else'')
    if comBrackets:print(']')

#Inicio dos testes
matrix=[
    [9,3,6],
    [5,4,7],
    [8,2,1]
]

print('\nMatrix:')
printMatrix(matrix)

print('\nTodos os dados da horizontal 1:')
print(getAllX(matrix,1))

print('\nTodos os dados da diagonal y 0, x 2, direcao esquerda:')
print(getDiagonalData(matrix,0,2,False))

print('\nMatrix Transposta:')
printMatrix(transpose(matrix))

print('\nMatrix Ordenada na Horizontal')
sortX(matrix)
printMatrix(matrix)

print('\nMatrix Ordenada na Vertical')
sortY(matrix)
printMatrix(matrix)

print('\nMatrix com Indices:')
matrixIndexer(matrix)
printMatrix(matrix)

print('\nMatrix gerada de 1 ate 5(largura) e 5(altura):')
printMatrix(gerarMatrixOrdenada(1,5,5),False)

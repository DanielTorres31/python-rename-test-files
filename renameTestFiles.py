import os

folderPath = './login'
# folderPath = 'd:/repo/fabs/app/src'

def isDir(name):
    return len(name.split('.')) == 1

def getFilesName(path):
    return os.listdir(path)

def getAllFilePaths(path):
    allFilePaths = []
    for name in getFilesName(path):
        if isDir(name):
            allFilePaths.extend(getAllFilePaths(path + '/' + name))
        else:
            allFilePaths.append(path + '/' + name)
    
    return allFilePaths

def filterTestFiles(filePaths):
    return filter(lambda filePath: filePath.endswith('-test.js'), filePaths)

def mountFilePath(peaces):
    filePath = ''
    for peace in peaces:
        filePath = filePath + peace + '/'
    
    return filePath

def renameTestFile(filePath, rename):
    peaces = filePath.split('/')

    fileNameIndex = len(peaces) - 1
    fileName = peaces[fileNameIndex]
    fileName = fileName.replace('-test.js', '.test.js')
    peaces[fileNameIndex] = fileName
    
    newFilePath = mountFilePath(peaces)

    if rename:
        os.rename(filePath, newFilePath)
        return
    
    print(f'Arquivo {filePath} renomeado para {newFilePath}')

def init(folderPath, rename):
    allFilePaths = getAllFilePaths(folderPath)
    testFilePaths = filterTestFiles(allFilePaths)

    for testFilePath in testFilePaths:
        renameTestFile(testFilePath, rename)
    
    print('Concluído com sucesso!')
    
init(folderPath, False)
import os
import shutil

from src.printstd import PRINT_STD


def deleteFile(path , isSil):
    delList = []
    delDir = path
    delList = os.listdir(delDir)
    for f in delList:
        filePath = os.path.join( delDir, f )
        if os.path.isfile(filePath):
            os.remove(filePath)
            PRINT_STD.P(filePath + " was removed!"+"\n")
        elif os.path.isdir(filePath):
            shutil.rmtree(filePath,True)
            PRINT_STD.P("Directory: " + filePath +"was removed!"+"\m")

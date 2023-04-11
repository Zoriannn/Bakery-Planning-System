#FileName   : TextFileConn.py
#Created by : Kou Zi Hong
#Purpose    : To modify text file
#Date       : 10/12/2021


import json
#Reading list
def fileReadDD(path,fileName):
    
    fObj=open(path+fileName,"r")
    ddStr=fObj.read()
    dd=json.loads(ddStr)
    return ddStr,dd

def fileRead(path,fileName):
    fObj=open(path+fileName,"r")        #cursor will be positioned at the beginning
    lines=fObj.readlines()              #read(), readline(), readlines()
                                        #read() -> strings (cursor@end)
                                        #readline() -> stringsread 1 line (cursor@nextline)
                                        #readlines() -> list (cursor@back)
    fObj.close()                        #close immediately after retrieving data
    rec=[]
    keyLst=[]
    for line in lines:
        trec=line.strip("\n").split("|")#trec in the form of a list
        keyLst.append(trec[0])
        rec.append(trec)
    return keyLst,rec


def fileAppend(path,fileName,line):
    fObj=open(path+fileName,"a")  #cursor immediate go to the back of the file
    wStr="|".join(line)+"\n"
    fObj.write(wStr)
    fObj.close()
    return
    
def fileSave(path,fileName,rec):
    fObj=open(path+fileName,"w")
    wStr=""
    for line in rec:
        wStr +="|".join(line)+"\n"
    fObj.write(wStr)
    fObj.close()
    return


        

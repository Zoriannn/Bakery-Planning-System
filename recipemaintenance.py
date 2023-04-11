#program name: Recipe maintenance

#created by: Seah Chee Tou

#modified by: Kou Zi Hong


#date: 12/16/2021
import TextFileConn as Lib


def getRcp(rcp):
    rcpRec=[]
    ingreRec=[]
    recKey,recLines=Lib.fileRead("","recipe.txt")
    for line in recLines:
        if line[0] == rcp:
            rcpRec.append(line)
            ingreRec.append(line[1])
    return rcpRec,ingreRec

def displayRcp(rcpRec):
    print("\t=============================================")
    print("\tIngredients            Unit            Amount")
    print("\t=============================================")
    for i in rcpRec:
        print("\t%-11s            %3s         %10.1f"%(i[1],i[2],float(i[3])))
    print("\t=============================================")
    
def MM():
    rcpLst=["breadL100","breadL150S","breadL200","breadL125"]
    loop=True
    while loop:
        print("""
        List of recipes ---> <breadL100     >   <breadL200     >
                             <breadL150S    >   <breadL125     >""")
        print("\t========================================================")
        rcp=input("\tEnter recipe <Q>uit  >>")
        if rcp.upper() == "Q":
            loop=False
        elif rcp in rcpLst:
            rcpRec,ingreRec=getRcp(rcp)
            step=1
            loop2=True
            while loop2:
                if step == 1:
                    displayRcp(rcpRec)
                    opt=input("\t<A>dd  <E>dit  <D>elete  <S>ync  <Q>uit >>").upper()
                    if opt == "Q":
                        step=99
                    elif opt not in ["A","E","D","S"]:
                        print("\tError with option entered\n")
                    elif opt == "S":
                        step=8
                    else:
                        step+=1
                if step == 2:
                    ingre=input("\tEnter ingredient <Q>uit  >>").upper()
                    if ingre.upper() == "Q":
                        step=1
                    elif opt in ["A","E"]:
                        if opt == "A":
                            if ingre in ingreRec:
                                print("\tError: Ingredient already added")
                            else:
                                step+=1
                        elif opt == "E":
                            if ingre not in ingreRec:
                                print("\tError: Ingredient not exist")
                            else:
                                step+=1
                    else:
                        step=7
                if step == 3:
                    amt=input("\tEnter amount <Q>uit  >>")
                    if amt.upper() == "Q":
                        step=1
                    elif not amt.isdigit():
                        print("\tError with amount entered")
                    else:
                        step+=1
                if step == 4:
                    unit=input("\tEnter unit(g/kg/l/ml) <Q>uit  >>")
                    if unit == "Q":
                        step=1
                    elif unit not in ["g","kg","l","ml"]:
                        print("\tError with unit entered")
                    else:
                        if opt == "A":
                            rcpRec.append([rcp,ingre,unit,amt])
                            ingreRec.append(ingre)
                        elif opt == "E":
                            i=0
                            maxln=len(rcpRec)
                            while i < maxln:
                                if rcpRec[i][0] == rcp and\
                                   rcpRec[i][1] == ingre:
                                    rcpRec[i][2]=unit
                                    rcpRec[i][3]=amt
                                    i=maxln
                                else:
                                    i+=1
                        print("\tSuccessfully updated...\n")
                        step=1
                if step == 7:
                    i=0
                    maxln=len(rcpRec)
                    while i < maxln:
                        if rcpRec[i][0] == rcp and\
                           rcpRec[i][1] == ingre:
                            rcpRec.pop(i)
                            i=maxln
                        else:
                            i+=1
                    print("\tSuccesfully deleted...\n")
                    step=1
                if step == 8:
                    recKey,recLines=Lib.fileRead("","recipe.txt")
                    saveRec=[]
                    for i in recLines:
                        if i[0] != rcp:
                            saveRec.append(i)
                    saveRec.extend(rcpRec)
                    Lib.fileSave("","recipe.txt",saveRec)
                    print("\tSuccessfully saved\n")
                    step=1
                if step == 99:
                    loop2=False
        else:
            print("\tNo such recipe\n")
    


if __name__ == "__main__":
    MM()









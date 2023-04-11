#Program Name    : IMmaintain.py

from datetime import datetime
time = datetime.now()
time = time.strftime("%d/%m/%y   %H:%M/%S")

def InputA():
    print()
    chk = []
    f = open("IM.txt","r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lst = lines[i].strip("\n").split("|")
        chk.append(lst[0])
    step = 0
    loop = True
    while loop:
        if step == 0:
            print("Enter Ingredient Adding    <Q>uit")
            IA   = input("I   >> ")
            IAchk = IA.replace(" ","",2)
            if IAchk.upper() == "Q":
                step = 99
            elif IAchk.upper() in chk:
                print("Ingredient already exists.")
                print()
            elif IAchk.isdigit():
                print("Invalid Entered")
                print()
            else:
                step +=1
        if step == 1 :
            print("Enter UOM (g/kg/ml/l)      <Q>uit")
            UOMA = input("UOM >> ")
            if UOMA.upper() == "Q":
                print()
                step = 0
            elif UOMA.lower() == "g":
                step += 1
            elif UOMA.lower() == "kg":
                step += 1
            elif UOMA.lower() == "ml":
                step += 1
            elif UOMA.lower() == "l":
                step += 1
            else:
                print("Invalid Entered")
                print()
        if step == 2 :
            print("Enter Qty                  <Q>uit")
            QA   = input("Qty >> ")
            QAchk = QA.replace(".","",1)
            if QA.upper() == "Q":
                print()
                step = 0
            elif not QAchk.isdigit():
                print("Invalid Entered")
                print()
            elif QA == "NA":
                print("Please input in 0 instead of NA.")
            else:
                print("Successfully Added.")
                step += 1
        if step == 3 :
            IAnew = ""
            for i in IA:
                if (i.isupper()) == True:
                    IAnew += i
                elif (i.islower()) == True:
                    IAnew += (i.upper())
                elif (i.isspace()) == True:
                    IAnew += i
            step += 1
        if step == 4 :
            if UOMA == "kg":
                UOMA = "g"
                QA = float(QA)*1000
            elif UOMA == "g":
                QA = float(QA)
            elif UOMA == "l":
                UOMA = "ml"
                QA = float(QA)*1000
            elif UOMA == "ml":
                QA = float(QA)
            if QA == 0:
                QA = "NA"
            step += 1
        if step == 5 :
            fStr = ""
            f=open("IM.txt","a")
            Insert = ("%s|%s|%.2f\n"%(IAnew,UOMA,QA))
            f.write(Insert)
            f.close()
            print()
            Display()
            step = 0
        if step == 99:
            print("going back to option...")
            print()
            loop = False
            
def InputM():
    print()
    IChk = []
    UOMMod = []
    QtyMod = []
    f=open("IM.txt","r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        Check = lines[i].strip("\n").split("|")
        IChk.append(Check[0])
        UOMMod.append(Check[1])
        QtyMod.append(Check[2])
    step = 0
    loop = True
    while loop:
        if step == 0:
            print("Enter Ingredient Modding      <Q>uit")
            IM   = input("I    >> ")
            if IM in IChk :
                step += 1
            elif IM.upper() == "Q":
                step = 99
            else:
                IMWC = ""
                for a in IM:
                    if (a.isupper()) == True:
                        IMWC += a
                    elif (a.islower()) == True:
                        IMWC += (a.upper())
                    elif (a.isspace()) == True:
                        IMWC += a
                if IMWC in IChk:
                    IM = IMWC
                    step += 1
                else:
                    print("Unable to find ingredient")
        if step == 1:
            print("Enter UOM Mod To (g/kg/ml/l)  <Q>uit")
            UOMM = input("UOM >> ")
            if UOMM.lower() == "g":
                step += 1
            elif UOMM.lower() == "kg":
                step += 1
            elif UOMM.lower() == "ml":
                step += 1
            elif UOMM.lower() == "l":
                step += 1
            elif UOMM.upper() == "Q":
                print()
                step = 0
            else:
                print("Invalid Entered")
                print()
        if step == 2:
            print("Enter Qty Mod To              <Q>uit")
            QM   = input("Qty >> ")
            QtyMChk = QM.replace(".","",1)
            if QM.upper() == "Q":
                print()
                step = 0
            elif QtyMChk.isdigit():
                step += 1
            elif QM == "NA":
                print("Please input in 0 instead of NA.")
            else:
                print("Invalid Entered")
                print()
        if step == 3 :
            if UOMM == "kg":
                UOMM = "g"
                QM = float(QM)*1000
            elif UOMM == "g":
                QM = float(QM)
            elif UOMM == "l":
                UOMM = "ml"
                QM = float(QM)*1000
            elif UOMM == "ml":
                QM = float(QM)
            if QM == 0:
                QM = "NA"
            step += 1
        if step == 4 :
            Iidx = IChk.index(IM)
            UOMMod[Iidx] = UOMM
            QtyMod[Iidx] = QM
            f=open("IM.txt","w")
            FStr = ""
            for i in range(len(IChk)):
                Insert = ("%s|%s|%.2f\n"%(IChk[i],UOMMod[i],float(QtyMod[i])))
                FStr += Insert
            f.write(FStr)
            f.close()
            print()
            Display()
            step = 0
        if step == 99:
            print("going back to option...")
            print()
            loop = False

def InputD():
    ILst   = []
    UOMLst = []
    QtyLst = []
    f=open("IM.txt","r")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        Check = lines[i].strip("\n").split("|")
        ILst.append(Check[0])
        UOMLst.append(Check[1])
        QtyLst.append(Check[2])
    step = 0
    loop = True
    while loop:
        if step == 0:
            print("Enter Ingredient to Delete <Q>uit")
            ID   = input("I    >> ")
            if ID in ILst :
                step += 1
            elif ID.upper() == "Q":
                step = 99
            else:
                IDWC = ""
                for a in ID:
                    if (a.isupper()) == True:
                        IDWC += a
                    elif (a.islower()) == True:
                        IDWC += (a.upper())
                    elif (a.isspace()) == True:
                        IDWC += a
                if IDWC in ILst:
                    ID = IDWC
                    step += 1
                else:
                    print("Unable to find ingredient")
        if step == 1 :
            Iidx = ILst.index(ID)
            UOMLst.pop(Iidx)
            QtyLst.pop(Iidx)
            ILst.pop(Iidx)
            f=open("IM.txt","w")
            FStr = ""
            for i in range(len(ILst)):
                Insert = ("%s|%s|%.2f\n"%(ILst[i],UOMLst[i],float(QtyLst[i])))
                FStr += Insert
            f.write(FStr)
            f.close()
            print()
            Display()
            step = 0
        if step == 99:
            print("going back to option...")
            print()
            loop = False
             
def Display():
    print("="*60)
    print(time)
    print("="*60)
    print("Ingredient   Unit/UOM                       Qty")
    print("="*60)
    f=open("IM.txt","r")
    disp= f.readlines()
    f.close()
    for i in range(len(disp)):
        display = disp[i].strip("\n").split("|")
        if display[2] !="0":
            print("%-15s   %-28s   %3s"%(display[0],display[1],display[2]))
    print("="*60)

def InputType():
    loop = True
    while loop:
        Display()
        ipt = input("<A>dd   <M>od   <D>el   <R>eload        <Q>uit >>").upper()
        if ipt == "Q":
            print("going back to Main Menu...")
            print()
            loop = False
        elif ipt == "M":
            InputM()
        elif ipt == "A":
            InputA()
        elif ipt == "D":
            InputD()
        elif ipt == "R":
            print()
        else:
            print("INVALID ENTERED")
            print()



if __name__ == "__main__":
    InputType()


import Group2
import datetime
time = datetime.datetime.now()
time = time.strftime("%Y-%m-%d")
text1 = ""
text2 = ""

#for main screen display
def displayMRP():
    print()
    print("\t"+"="*60)
    print("\tMaterial Requirements Plan (%s)"%time)
    print("\t"+"="*60)
    txt1 = "Production Plan\n"
    dis1 = txt1.center(76)
    print(dis1)
    print("\tRecipe         Description                    Qty\n")
    f = open("list of order.txt","r")
    lines = f.readlines()
    for i in range(len(lines)):
        lineLst = lines[i].strip("\n").split("|")
        if lineLst[2] != "0":
            text = "\t%-12s   %-28s   %3s"%(lineLst[0],lineLst[1],lineLst[2])
            print(text)
            global text1
            text1 = text1 + text + "\n"
            
    f.close()
    print("\t"+"="*60)
    txt2 = "Ingredients Requirements\n"
    dis2 = txt2.center(77)
    print(dis2)
    print("\tIngredient         StockLevel        Demand       Shortfall")
    print()
    
    total = []
    sfall = []
    stk = []
    everyING = []
    


    f = open("IM.txt","r")
    lines = f.readlines()
    for i in range(len(lines)):
        total.append(0)
        sfall.append(0)
        stk.append(0)
        lineLst = lines[i].strip("\n").split("|")
        everyING.append(lineLst[0])



    #for demand
    f = open("recipe.txt","r")
    f2 = open("list of order.txt","r")
    lines = f.readlines()
    lines2 = f2.readlines()
    for i in range(len(lines)):
        lineLst = lines[i].strip("\n").split("|")
        if lineLst[0] == "breadL100":
            for p in range(len(everyING)):
                if lineLst[1] == everyING[p]:
                    for y in range(len(lines2)):
                        lineLst2 = lines2[y].strip("\n").split("|")
                        if lineLst[0] == lineLst2[0]:
                            total[p] += int(lineLst2[2]) * int(lineLst[3])
        
        elif lineLst[0] == "breadL125":
            for p in range(len(everyING)):
                if lineLst[1] == everyING[p]:
                    for y in range(len(lines2)):
                        lineLst2 = lines2[y].strip("\n").split("|")
                        if lineLst[0] == lineLst2[0]:
                            total[p] += int(lineLst2[2]) * int(lineLst[3])

        elif lineLst[0] == "breadL150S":
            for p in range(len(everyING)):
                if lineLst[1] == everyING[p]:
                    for y in range(len(lines2)):
                        lineLst2 = lines2[y].strip("\n").split("|")
                        if lineLst[0] == lineLst2[0]:
                            total[p] += int(lineLst2[2]) * int(lineLst[3])
                            
        elif lineLst[0] == "breadL200":
            for p in range(len(everyING)):
                if lineLst[1] == everyING[p]:
                    for y in range(len(lines2)):
                        lineLst2 = lines2[y].strip("\n").split("|")
                        if lineLst[0] == lineLst2[0]:
                            total[p] += int(lineLst2[2]) * int(lineLst[3])




    #for stock level
    f3 = open("IM.txt","r")
    lines3 = f3.readlines()
    for i in range(len(lines3)):
        lineLst3 = lines3[i].strip("\n").split("|")
        for h in range(len(everyING)):
            if everyING[h] == lineLst3[0]:
                stk[h] = float(lineLst3[2])




    #for shortfall
    for i in range(len(total)):
        check = total[i] - stk[i]
        if check < 0:
            sfall[i] = "NA  "
        else:
            sfall[i] = check
            
    
    for i in range(len(sfall)):
        if sfall[i] != "NA  ":
            sfall[i] = str(sfall[i])+" g"

    
    for i in range(len(total)):
        text = "\t%-12s   %14s    %10s     %11s"%(everyING[i],stk[i],total[i],sfall[i])
        print(text)
        global text2
        text2 = text2 + text + "\n"

    print()
    print("\t"+"="*60)
    inputsMRP()

#for inputs display
def inputsMRP():
    loop = True
    while loop:
        ipt = input("\t"+"<S>ave2File     <Q>uit   >> ").upper()
        if ipt == "Q":
            loop = False
        elif ipt.isdigit():
            print("\tInvalid Input")
        elif ipt == "S":
            f = open("MRPrun.txt","w")
            output = "\t                Production Plan\n" + "\tRecipe         Description                    Qty\n" +"\n"+\
                     text1 + "\n" + "\t                    Ingredients Requirements\n" + \
                     "\tIngredient         StockLevel        Demand       Shortfall\n"+"\n"+\
                     text2
            f.write(output)
            f.close()
            
            print("\tMRP Run results are saved in file named MRPrun.txt")
            ent = input("\tPress ENTER to return to Menu...")
            Group2.inputs()
            loop= False
        else:
            print("\tInvalid Input")
            


if __name__=="__main__":
    displayMRP()
    


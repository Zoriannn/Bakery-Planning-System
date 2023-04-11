#FileName     : AssignCreateOrder2.py
#Created by   : Kou Zi Hong
#Created Date : 10/12/2021
#Library      : TextFileConn.py



import TextFileConn as Lib

def ModDel(g_order,opt,rcp,qty,g_rcpOrder):
    i=0
    maxlen=len(g_order)
    while i < maxlen:
        if rcp == g_order[i][0]:
            if opt == "M":
                g_order[i][2]=qty
                i=maxlen
            else:
                g_order.pop(i)
                g_rcpOrder.pop(i)
                i=maxlen
        else:
            i+=1
    return g_order

def displayOrder(g_order):
    print("""
        List of recipes ---> <breadL100     >   <breadL200     >
                             <breadL150S    >   <breadL125     >""")
    print("\t--------------------------------------------------------")
    print("\tRecipe       Description                    Qty")
    print("\t--------------------------------------------------------")
    print()
    for i in g_order:
        print("\t%-10s   %-28s   %3s"%(i[0],i[1],i[2]))
    print()
    print("\t--------------------------------------------------------")

def createOrder():
    rcpLst=["breadL100","breadL150S","breadL200","breadL125"]
    descLst=["Basic Loaf 1 KG","Chef's special 1.5 KG",
             "Basic Loaf 2 KG","Basic Loaf 1.25 KG"]
    g_rcpOrder,g_order=Lib.fileRead("","list of order.txt")
    step=1
    loop=True
    while loop:
        if step == 1:
            displayOrder(g_order)
            opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  <S>yncFile <R>esetFile >>").upper()
            if opt == "Q":
                step=99
            elif opt not in ["A","M","D","S","R"]:
                print("\tError with option entered")
            elif opt in ["S","R"]:
                step=8
            else:
                step+=1
        if step == 2:
            rcp=input("\tEnter recipe      <Q>uit >>")
            if rcp.upper() == "Q":
                step=1
            elif rcp not in rcpLst:
                print("\tInvalid recipe")
            elif opt in ["A","M"]:
                if opt == "A":
                    if rcp in g_rcpOrder:
                        print("\tError: Record already added")
                    else:
                        step+=1
                elif opt == "M":
                    if rcp not in g_rcpOrder:
                        print("\tError: No order record")
                    else:
                        step+=1
            else:
                step=7
        if step == 3:
            qty=input("\tEnter qty to bake <Q>uit >>")
            if qty.upper() == "Q":
                step=1
            elif not qty.isdigit():
                print("\tError with quantity entered")
            else:
                idx=rcpLst.index(rcp)
                if opt == "A":
                    g_order.append([rcp,descLst[idx],qty])
                    g_rcpOrder.append(rcp)
                elif opt == "M":
                    g_order=ModDel(g_order,opt,rcp,qty,"")
                print("\tSuccessfully updated...")
                input("\tPress enter to continue")
                step=1
        if step == 7:     
            g_order=ModDel(g_order,opt,rcp,"",g_rcpOrder)
            print("\tSuccessfully deleted...")
            input("\tPress enter to continue")
            step=1
        if step == 8:
            if opt == "R":
                g_order.clear()
                g_rcpOrder.clear()
            Lib.fileSave("","list of order.txt",g_order)
            print("\tSuccessfully updated.")
            input("\tPress enter to continue")
            step=1
        if step == 99:
            loop=False


if __name__ == "__main__":
    createOrder()







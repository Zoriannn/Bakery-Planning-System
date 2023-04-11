import datetime as dt
import AssignCreateOrder2 as CO
import IMmaintain as IM
import recipemaintenance as RM
import MRP

def displayMenu():
    g_currD=dt.date.today()
    print("\n")
    print("\t","="*60,sep="")
    txt1 = "Bakery 123"
    dis1 = txt1.center(75)
    print(dis1)
    txt2 = "\tMaterial Planning System (Datetime:%s)"%g_currD
    dis2 = txt2.center(73)
    print(dis2)
    print("\t","="*60,sep="")
    print("\t<1> Ingredients/Materials Maintenance")
    print("\t<2> Maintain Recipes")
    print("\t<3> Create Requirements/Orders")
    print("\t<4> Generate Material Requirements Plan")
    print()
    print("\t<Q>uit")
    print("\t","="*60,sep="")
    return      
    


def inputs():
    loop = True
    while loop:
        displayMenu()
        opt= input("\tOption >> ").upper()
        if opt=="Q":
            print("\tExiting system")
            loop = False
        elif opt.isalpha():
            print("\tInvalid Option")
        elif opt == "1":
            IM.InputType()
        elif opt == "2":
            RM.MM()
        elif opt == "3":
            CO.createOrder()
        elif opt == "4":
            MRP.displayMRP()
        else:
            print("\tInvalid Option")

if __name__=="__main__":
    inputs()






    
    



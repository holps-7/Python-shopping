#Python programm made for a Shop
#This was a fun project made by us overnight, please feel free give your precious commentc
#Made by:-
#           Ramesh Sachan- Vellore Institute of Technology, Vellore
#           Gaurang Dwivedi- Dehradun Institute of Technology, Dehradun


# function to add the product in stock
def func_stockadd():
    prod_name = input("Enter the Product name:\n").upper()
    print("Enter the price of the",prod_name,": ")
    price = int(input())
    stock[prod_name] = price
    print("The latest updated stock list is : \n")
    func_stockview()



# function for updating product in stock
def func_update():
    p = input("Enter the product name you want to update: ").upper()
    ctr=0;
    #searching p in keys of the dictionary
    for i in stock.keys():
        if i.upper() == p:
            ctr=1
            break

    if ctr == 1:
        upd_price = int(input("Enter the updated price of product: "))
        stock[p] = upd_price
        print(p," is updated successfully")
        print("The latest updated stock is : \n")
        func_stockview()
    else:
        print(p," does not exists in the stock")



# function to remove the product from stock
def func_stockremove():
    r = input("Enter the product to be removed: ").upper()
    ctr=0;
    #searching p in keys of the dictionary
    for i in stock.keys():
        if i.upper() == r:
            ctr=1
            break

    if ctr == 1:
        del stock[r]
        print(r," is removed successfully")
        print("The latest updated stock is : \n")
        func_stockview()
    else:
        print(r," does not exists in the stock")



# function to view the products in stock
def func_stockview():
    for i in stock.keys():
        print('%-15s: %i'%(i,stock[i]))



# function to add the product in basket
def func_bsktadd(cons_pro):
    print("Enter the quantity of ",cons_pro," to be added: ")
    qty = int(input())
    basket[cons_pro] = qty



# function to view the products in basket
def func_bsktview():
    for i in basket.keys():
        print('%-15s: %i'%(i,basket[i]))



# function to search product in stock
def func_search() :
    srch = input("Enter the Product to be searched \n").upper()
    if srch in stock.keys():
        print("The product is available \n")
        print("Price of ",srch," is: ",stock[srch])
    else:
        print(srch," is not present in stock")



# function to remove product from basket
def func_bsktremove() :
    r = input("Enter the product to be removed: ").upper()
    ctr=0;
    #searching p in keys of the dictionary
    for i in basket.keys():
        if i.upper() == r:
            ctr=1
            break

    if ctr == 1:
        del basket[r]
        print(r," is removed successfully")
        print("The latest updated basket is : \n")
        func_bsktview()
    else:
        print(r," does not exists in the basket")



 # function for billing invoice
def func_bill_invoice() :
    from datetime import datetime
    now = datetime.now()
    dt_tm = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Billing Invoice\n")
    print("_"*15)
    print("Date of purchase: ", dt_tm[0:10])
    print("Time of purchase: ", dt_tm[11:19])
    print("\n\n")
    gtotal=0
    s=" "
    str="Grand Total: "
    print('%-15s%-15s%-15s%-15s'%("Product Name","Unit Price","Quantity","Total"))
    for i in basket.keys():
        total = int(stock[i])*int(basket[i])
        gtotal += total
        print('%-18s%-16i%-11i%i'%(i,stock[i],basket[i],total))
    print('%-30s%-15s%i'%(s,str,gtotal))





if __name__=="__main__":
    #empty dictionary
    stock = {"MOUSE":400, "KEYBOARD":300, "MONITOR":400, "CPU":800, "UPS":200}
    print("Mini Project : Online Retail Shopping \n\n")
    print('-'*100)
    print("\n\n")

    #Primary infinte loop
    while True:
        print("1)Admin Module\n2)Consumer Module\n3)End the program\nEnter your choice: ")
        x=int(input())#choice is in x

        #admin module
        if x == 1:
            print("Welcome to the Admin Module\n")

            #Secondry infinite loop for admin module
            while True:
                # dictionary for options
                opt = {1:"Add Product", 2:"Update Product in Stock", 3:"Remove Product from Stock" ,4:"View all Products in Stock" ,5:"Logout Admin"}

                print(" Menu\n")
                print(" 1-Add Product\n 2-Update Product in Stock\n 3-Remove Product from Stock\n 4-View all Products in Stock\n 5-Logout Admin\n\n ")

                n = int(input("Enter an option to opt for: "))

                if  n == 1:
                    func_stockadd()
                elif n == 2:
                    func_update()
                elif n == 3:
                    func_stockremove()
                elif n == 4:
                    func_stockview()
                elif n == 5:
                    print("Logging out of Admin Module")
                    break
                else :
                    print("***Invalid input***\t\tTry again\n")


        #user module
        elif x == 2:
            basket={}
            print("\n\n Dear Costumer\n Welcome! to Consumer module\n")
            print("-"*100)
            opt_2 = {1:"View All Products in Stock", 2:"Add to Basket", 3:"View All Products in Basket", 4:"Search Product in Stock", 5:"Remove Product from Basket", 6:"Print Invoice", 7: "Sign out"}
            while True :
                print(" _Menu_ \n\n")
                print("\n\n\t1:View All Products in Stock\n\t2:Add to Basket\n\t3:View All Products in Basket\n\t4:Search Product in Stock\n\t5:Remove Product from Basket \n\t6:Print Invoice\n\t7: Sign out")

                n2 = int(input("Enter The Number Corresponding To The Service , To Perform A Task "))

                if n2 == 1 :
                    func_stockview()

                elif n2 == 2 :
                    while True :
                        cons_pro = input("Enter the Product to Add to the Basket\n")
                        cons_pro = cons_pro.upper()
                        if cons_pro in stock.keys():
                            func_bsktadd(cons_pro)
                        else :
                            print("Sorry for the inconvenience , Product is out of stock \nTry for another Product")
                        ext = int(input("Enter 0 to exit the basket else press 1 to continue"))
                        if ext == 0 :
                            func_bsktview()
                            break
                        elif ext == 1 :
                            continue
                elif n2 == 3 :
                    func_bsktview()

                elif n2 == 4 :
                    func_search()

                elif n2 == 5 :
                    func_bsktremove()

                elif n2 == 6 :
                    func_bill_invoice()

                elif n2 == 7 :
                    print("Consumer Signed out successfully")
                    re = int(input("If You Wish To Shop Again\n\n Press 1 else Press 0 "))
                    if re == 1:
                        basket={}
                        continue
                    elif re == 0 :
                        break
                else:
                    print("***Invalid input***\t\tTry again\n")

        #Exit the program
        elif x == 3:
            #func_finish ()
            print("Software Is Terminating\n\nDeveloped By: Ramesh Sachan and Gaurang Dwivedi")
            break

        #Invalid input
        else:
            print("***Invalid input***\t\tTry again\n")

i={1:"Margernita",2:"Farmhouse",3:"Periperi",4:"Hotpizza"}
price={1:100,2:200,3:300,4:400}

print("-"*85)
print("\t\t\t\tDominos")
print("-"*85)

print("""
      1.Margernita
      2.Farmhouse
      3.Periperi
      4.Hotpizza""")

P=[]
q=[]

while True:
    x=int(input("Enter your choise pizza:"))
    y=int(input("Enter your Quantity of pizza:"))
    P.append(x)
    q.append(y)
    ch=input("Do you wat to add more pizza?:Y/N:")
    if ch == "N":
        print("-"*85)
        print("{:^15} {:^15} {:^15} {:^15} {:^15}".format("sr No.","Name of the product","Quantity","Price","Total"))
        print("-"*85)
        s=1
        for l in range(len(P)):

            print("{:^15} {:^15} {:^15} {:^15} {:^15}".format(s,i[P[l]],q[l],price[P[l]],q[l]*price[P[l]]))
            s=s+1

        break


     
    


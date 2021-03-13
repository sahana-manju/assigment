i=0
while i==0:
    budget=input('Enter Your budget :')
    try:
        b=int(budget)
        i=1
    except:
        print('Please enter a valid number')
        i=0
p1=list()
p2=list()
p3=list()

d1={'product':p1,'quantity':p2,'price':p3}
choice=1
while b!=0:
    print('1.Add an item')
    print('2.Exit')
    try:
        choice = int(input())

    except ValueError:
        choice=3

    if not(choice==1 or choice==2):
        print('Please enter a valid choice')

    else:

        if choice==2:
            if b > 0:
                for i in range(len(p3)):
                    if b >= p3[i]:
                        print('you can buy', p1[i])
            break
        product=input('Enter Product : ')
        quantity=input('Enter quantity : ')
        try:
            price=int(input('Enter price : '))
            c=0
        except ValueError:
            print('Print a valid price')
            c=1

        if c!=1:
            if b-price<0:
                print("Can't buy the product because budget left is",b)
            else:
                if product in p1:
                    n1=p1.index(product)
                    b=b+p3[n1]-price
                    p2[n1]=quantity
                    p3[n1]=price

                else:
                    b = b - price
                    d1['product'] = p1.append(product)
                    d1['quantity'] = p2.append(quantity)
                    d1['price'] = p3.append(price)
                print("Amount left : ",b)


print('Product      Quantity        Price')
for i in range(len(p1)):
    print(p1[i],'\t\t',p2[i],'\t\t',p3[i])






product1=float(input())
product2=float(input())

discount1=product1/10
discount2=product2/10

price1=round(product1-discount1,2)
price2=round(product2-discount2,2)

print(price1,price2)

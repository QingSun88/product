products = []
while True:
	name = input('please input the product name:')
	if name == 'q':
		break
	price = input('please input the product price:')
	products.append([name,price])
#简写之后两大步
#	p=[name,price],同之后三步p =[],	p.append(name),	p.append(price)
#	products.append(p)
print(products)

for p in products:
	print(p[0], 'its price is', p[1])
	
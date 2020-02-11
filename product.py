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

with open('products.txt', 'w') as f: 
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  
# w是写入模式，所以products文档存不存在不重要，有则覆盖无则新建
# open只是打开档案
#字串可以直接做加法和乘法运算
#f.write才是写入动作，\n是换行的意思



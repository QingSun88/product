#读取档案
products = []
with open('product.csv','r',encoding = 'utf-8') as f:
	for line in f:
		if '商品，价格' in line:
			continue 
			#继续，遇到条件字串就自动跳过并从新来一次，不再执行回圈中下列指令。
			#continue不会跳出回圈，不像break
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)

#让使用者输入
while True:
	name = input('please input the product name:')
	if name == 'q':
		break
	price = input('please input the product price:')
	#此时price是字串，需要转换为整数
	price = int(price)
	products.append([name,price])
#简写之后两大步
#	p=[name,price],同之后三步p =[],	p.append(name),	p.append(price)
#	products.append(p)
print(products)

#打印所有购买记录
for p in products:
	print(p[0], 'its price is', p[1])

#写入档案
with open('products.txt', 'w',encoding = 'utf-8') as f: 
	f.write('商品, 价格 \n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  
	# w是写入模式，所以products文档存不存在不重要，有则覆盖无则新建
	# open只是打开档案
	#字串可以直接做加法和乘法运算
	#f.write才是写入动作，\n是换行的意思
	#因为只能字串相加，所以需要把整数p[]转换为字串,str(p[1])



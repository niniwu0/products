#二維清單 : 清單中還有清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

#for loop : 一個一個取出清單中的東西
for p in products:
	print(p[0], '的價格是', p[1])#清單裡面的小清單位置
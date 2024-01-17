items = [
    {
        'product':'camisa',
        'price':200
    },
    {
        'product':'pantalon',
        'price':100
    }
]

prices = list(map(lambda item: item['price'],items))
print(prices)

def addIva(item):
   newItem= item.copy()
   newItem['iva'] = newItem['price'] * 0.16
   return item

newItems = list(map(addIva,items))
print(newItems);
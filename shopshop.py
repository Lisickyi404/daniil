##класс который бы описывал магазин
from items import items

def getSumm(itemsList):
    s = 0
    for item in itemsList:
        s+=item.price
    return s

class Item():
    def __init__(self,title,color,price,sale,id):
        self.title = title
        self.color = color
        self.price = price
        self.sale = sale
        self.id = id

class Shop():
    def __init__(self,catalog):
        self.title = 'GreenTutrle'
        self.profOrientaion = ['tech','furniture']
        self.balans = 9999
        self.catalog = catalog
        self.historty = []

    ##метод оплаты покупки
    def dealCompleted(self,deal):
        self.balans += 0.9 * deal.price
        self.historty.append(deal)
        print('Оплата прошла. Баланс {0}'.format(self.balans))

class Deal():
    def __init__(self,itemsList,time,bonusCode):

        self.itemsList = itemsList
        self.time = time
        self.bonusCode = bonusCode
        self.price = getSumm(itemsList)



menu = ['1 - каталог','2 - корзина 3-закрыть' ]
menu2 = ['0 - вернуться назад, id товара - открыть товар']
menu3 = ['0 - вернуться в каталог 1-добавить в корзину']
busket = []
open=True
while open:
    ##прохожу по списку items и вывожу по очереди все товары
    print(menu)
    action = int(input('куда перейти?'))
    if action == 1:
        for item in items:
            print(item)
        print(menu2)
        a = int(input('куда?'))
        if a==0:
            print('возврат в главное мену')
            continue
        else:
            print(items[a-1])
            print(menu3)
            a = int(input('куда?'))
            if a==1:
                busket.append(items[a-1])
                print('товар успешно добавлен в коризину')
            continue

    if action ==2:
        print('!!!ВАША КОРЗИНА ВЫГЛЯДИТ ТАК!!!')
        print(busket)
    if action==3:
        break

s=0
for item in busket:
    s+=item.get('price')

print('Сумма вашей покупки составила {0}'.format(s))
##создадим объект магазина
magazine = Shop([])

lays = Item('lays','pink',100,0,0)
computar1 = Item('PC','white',789,0,1)
smarttv = Item   ('smartTv','black',1999,0,2)
laptop1 = Item('Mac Book','white',1500,0,3)
laptop2 = Item('HP','color',720,0,4)
redbull = Item('red bull','blue',2,0,5)
redbullPack = Item('redBull pack','blue',11,0,6)





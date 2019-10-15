"""
You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.
"""

class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{menu} menu available from {start_time} to {end_time}.".format(menu = self.name, start_time = self.start_time, end_time = self.end_time)

  def calculate_bill(self,purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

#create a brunch menu
brunch_item = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu('Brunch',brunch_item,11,16)

#create an early bird menu
early_item = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_menu = Menu('Early Bird',early_item,15,18)

#create a dinner menu
dinner_item = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu('Dinner',dinner_item,17,23)

#create a kids menu
kids_item = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('Kids',kids_item,11,21)

#print(brunch_menu)
#print(brunch_menu.calculate_bill(['pancakes','coffee','home fries']))
#print(early_menu.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

class Franchise():
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus

 #to tell the address
  def __repr__(self):
    return "The address is {address}".format(address = self.address)

  def available_menus(self,time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time: #注意这里menu.start_time,start_time不是available_menus的attributes
        available_menus.append(menu)
    return available_menus

flagship_store = Franchise("1232 West End Road",[brunch_menu,early_menu,dinner_menu,kids_menu])

new_installment = Franchise("12 East Mulberry Street",[brunch_menu,early_menu,dinner_menu,kids_menu])
#这一长串的menu list可以单写一个menus来代替
#print(new_installment)
#print(flagship_store.available_menus(12))
#print(flagship_store.available_menus(17))

class Business():
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

bn1 = Business("Basta Fazoolin' with my Heart",['flagship_store','new_installment'])

arepas_item = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu('Take a Arepa',arepas_item,10,20)
arepas_place = Franchise("189 Fitzgerald Avenue",[arepas_menu])
#注意是arepas_menu, the second parameter Franchise takes in is a list
arepas = Business('Take a Arepa',[arepas_place])

print(arepas.franchises[0].menus[0])

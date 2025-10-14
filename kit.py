 # shopping card code
class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_item(self,items_name,gty):
        item = (item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):

      for item in self.items:
          if item[0]==item_name:
              self.items.remove(item)
              break


    def calculate_total(self):
        total = 0
      for item in self.items:
          total += item[1]
      return total

cart = ShoppingCart()

cart.add_item("Papaya",100)
cart.add_item("Guva",200)
cart.add_item("Orange",65)

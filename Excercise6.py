class Store:
    def __init__(self,name,items = []):
    self.name = name
    self.items = []
# You'll need 'name' as an argument to this method.
# Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
def add_item(self, name, price):
# Create a dictionary with keys name and price, and append that to self.items
my_dict = {'name': name, 'price': price}
self.items.append(my_dict)


def stock_price(self):
# Add together all item prices in self.items and return the total.
return sum(item["price"] for item in self.items)
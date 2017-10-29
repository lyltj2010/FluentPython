"""
>>> joe = Customer('John Doe', 0)
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banana', 4, 0.5),
...         LineItem('apple', 20, 1.5),
...         LineItem('watermello', 5, 5.0)]
>>> Order(joe, cart, fidelity_promo)
<Order total: 57.00 due: 57.00>
>>> Order(ann, cart, fidelity_promo)
<Order total: 57.00 due: 54.15>
>>> Order(joe, cart, bulk_item_promo)
<Order total: 57.00 due: 54.00>
>>> best_promo(Order(joe, cart))
3.0
"""

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.__total - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# Some plain functions
# Shared object that can be used in multiple contexts simultaneously

def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * 0.05
    else:
        return 0

def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * 0.07
    return 0

promos = [fidelity_promo, bulk_item_promo, large_order_promo]
def best_promo(order):
    """select best discount available"""
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

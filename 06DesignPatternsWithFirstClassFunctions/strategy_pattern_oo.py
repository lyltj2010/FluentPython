"""
>>> joe = Customer('John Doe', 0)
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banana', 4, 0.5),
...         LineItem('apple', 20, 1.5),
...         LineItem('watermello', 5, 5.0)]
>>> Order(joe, cart, FidelityPromo())
<Order total: 57.00 due: 57.00>
>>> Order(ann, cart, FidelityPromo())
<Order total: 57.00 due: 54.15>
>>> Order(joe, cart, BulkItemPromo())
<Order total: 57.00 due: 54.00>
"""


from abc import abstractmethod, ABC
from collections import namedtuple

# Customer class
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price  # unit price

    def total(self):
        return self.quantity * self.price


class Order: # the context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart) # copy it
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'): # by calling getattr and catch
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# The strategy, an Abstract Base Class
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return discount as positive dollar amount"""

# Series of Concrete Strategy
class FidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self, order):
        if order.customer.fidelity >= 1000:
            return order.total() * 0.05
        else:
            return 0

class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order):
        discount_ = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount_ += item.total() * 0.1
        return discount_

class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order):
        if(len(order.cart)) >= 10:
            return order.total() * 0.07
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()

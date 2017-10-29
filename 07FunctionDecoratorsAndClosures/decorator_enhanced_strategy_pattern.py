"""
Use a registration decorator to enhance the strategy pattern
More friendly implementation of best_promo
    * No need for the annoying _promo suffix
    * No warry forgetting add new promotion strategy to promos
    * Highlights the purpose and easy to disable a promotion temporaily
"""

promos = []

def promotion(promo_func):
    """Simple registration"""
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * 0.05
    else:
        return 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * 0.07
    return 0

def best_promo(order):
    """select best discount available"""
    return max(promo(order) for promo in promos)

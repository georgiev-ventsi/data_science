import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
# print(visits.head())
# print(cart.head())
# print(checkout.head())
# print(purchase.head())

visit_cart = pd.merge(visits, cart, how='left')
visit_cart_len = len(visit_cart)
# print(visit_cart_len)
null_visits = len(visit_cart[visit_cart.cart_time.isnull()])
# print(null_visits)

percent_null_visits = float(null_visits) / visit_cart_len
print(percent_null_visits)

cart_checkout = pd.merge(cart, checkout, how='left')
# print(cart_checkout)
cart_len = len(cart_checkout)
null_carts = len(cart_checkout[cart_checkout.checkout_time.isnull()])
percent_null_cart = float(null_carts) / cart_len
print(percent_null_cart)

checkout_purchase = pd.merge(checkout, purchase, how='left')
len_checkout_purchase = len(checkout_purchase)
null_checkout_purchase = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
percent_checkout_null = float(null_checkout_purchase) / len_checkout_purchase
print(percent_checkout_null)


all_data = visits\
  .merge(cart, how='left')\
  .merge(checkout, how='left')\
  .merge(purchase, how='left')
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print(all_data.head())
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())

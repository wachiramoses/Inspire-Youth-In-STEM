ledger = {}
def register():
    product_name=input("What is your product name:   ")
    product_price=eval(input("What is the price of the product:     "))
    ledger["product name"]=product_name
    ledger["product price"]=product_price

def get_ledger():
    print(ledger)

register()
get_ledger()
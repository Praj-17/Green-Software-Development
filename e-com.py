class Product:
    def __init__(self, id:int, name:str, price: int) -> None:
        self.id = id
        self.name = name
        self.price = price
    def __repr__(self) -> str:
        return f"Product Id {self.id} | Product Name: {self.name} | Product Price ${self.price}"

class ShoppingCart:
    def __init__(self,) -> None:
        self.cart = []
    def AddProduct(self, prod:Product):
        self.cart.append(prod)
        print("Product Added: ", prod)
    
    def DeleteProduct(self, id):
        for i in self.cart:
            if i.id == int(id):
                prod = i
                self.cart.remove(i)
                print("Product Deleted: ", prod)
                break
        else:
            print("Product not in cart")
        
    def CalculateTotal(self):
        return sum([int(i.price) for i in self.cart])
    def Displaycart(self):
        if not self.cart:
            print("The cart is Empty!")
        else:
            print("Cart contains following items..")
            for index, i in enumerate(self.cart):
                print(int(index) +1, i)
            print("Total: ", self.CalculateTotal())

class Customer():
    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
        self.shoppingcart = ShoppingCart()
    def add_to_cart(self, product):
        self.shoppingcart.AddProduct(product)
    def remove_from_cart(self, product_id):
        self.shoppingcart.DeleteProduct(product_id)
    def Checkout(self):
        self.shoppingcart.Displaycart()

if __name__ == "__main__":
    prod1 = Product(1, "IPhone", 100)
    prod2 = Product(2, "HeadPhone",10)
    prod3 = Product(3, "ipad", 60)

    cust = Customer("Prajwal", "pwaykos1@gmail.com")
    cust.shoppingcart.AddProduct(prod1)
    cust.shoppingcart.AddProduct(prod2)
    cust.shoppingcart.AddProduct(prod3)
    while True:
            inp =int( input("""Please provide your input: \n 
              1. Add product
              2. Display Cart
              3. Remove product
              4. Checkout\n :"""))
            if inp ==1:
                # print("select a product to add")
                id, name, price = input("Enter product details separated with a comma: ").split(",")

                # #create a product 
                p = Product(id, name,price)
                cust.add_to_cart(p)
            elif inp == 2:
                cust.shoppingcart.Displaycart()
            elif inp == 3:
                id = input("Enter product id to delete")
                cust.remove_from_cart(id)
            elif inp == 4:
                cust.Checkout()
                exit()
            else:
                print("Invalid Input")


            


        


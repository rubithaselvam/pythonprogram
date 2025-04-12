class product:

    def __init__(self,name,price,quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ₹{self.price} (Quantity: {self.quantity})"


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_cart(self,product):
        for item in self.cart:
            if item.name == product.name:
                item.quantity += product.quantity
                print(f"{item.name}, {item.quantity} added successfully")
                item.price += product.price
                print(f"{item.name}, {item.price} added sucessfully")
                return
        self.cart.append(product)
        print(f"{product.name} added in the cart")

    def view_cart(self):
        if not self.cart:
            print("cart is empty.")
        else:
            print("\nitems in your cart:")
            for item in self.cart:
                print(item)

    def remove_cart(self, product_name):
        for product in self.cart:
            if product.name == product_name:
                self.cart.remove(product)
                print(f"Removed {product.name} from cart.")
                return
        raise ValueError(f"{product_name} is not in your cart.")

    def init_add_products(self):
        p = product("pen", 20, 10)
        self.add_cart(p)
        p = product("eraser", 5, 20)
        self.add_cart(p)
        p = product("notebook", 35, 50)
        self.add_cart(p)



def main():
    cart = ShoppingCart()
    cart.init_add_products()

    while True:
        print("\nOptions:")
        print("1. view Products")
        print("2. add to Cart")
        print("3. remove from Cart")
        print("4. view Cart")
        print("5. exit")

        choice = input("enter your choice: ")

        try:
            if choice == "1":
                cart.view_cart()

            elif choice == "2":
                name = input("enter product name: ")
                price = int(input("enter price: "))
                quantity = int(input("enter quantity: "))
                p = product(name, price, quantity)
                cart.add_cart(p)

            elif choice == "3":
                name = input("enter product name to remove: ")
                cart.remove_cart(name)

            elif choice == "4":
                cart.view_cart()

            elif choice == "5":
                print("thank you for shopping!")
                break

            else:
                print("invalid option. try again.")

        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("Something went wrong:", e)

if __name__ == "__main__":
    main()

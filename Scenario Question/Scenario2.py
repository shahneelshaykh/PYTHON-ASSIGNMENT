class Product:
    """Base class for all products."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class PhysicalProduct(Product):
    """Subclass for physical products, such as books and electronics."""

    def __init__(self, name, price, weight, dimensions):
        super().__init__(name, price)
        self.weight = weight
        self.dimensions = dimensions

    def get_shipping_cost(self):
        """Calculate the shipping cost based on the weight and dimensions."""
        # TODO: Implement this method
        pass


class DigitalProduct(Product):
    """Subclass for digital products, such as e-books and software."""

    def __init__(self, name, price, download_url):
        super().__init__(name, price)
        self.download_url = download_url

    def get_shipping_cost(self):
        """Digital products have no shipping cost."""
        return 0


class ShoppingCart:
    """Class to represent a shopping cart."""

    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                return item
        return None

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_price()
        return total_price

    def checkout(self):
        """Process the checkout and place the order."""
        # TODO: Implement this method
        pass

    def display_cart(self):
        for item in self.items:
            print(item)

def main():
    """Main function."""

    shopping_cart = ShoppingCart()

    while True:
        # Display the menu
        print("**Shopping Cart Menu**")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Calculate total price")
        print("4. Checkout")
        print("5. Display cart")
        print("6. Exit")

        # Get the user's choice
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Add an item to the cart
            product_name = input("Enter the name of the product: ")
            product_price = float(input("Enter the price of the product: "))


            product = Product(product_name, product_price)
            shopping_cart.add_item(product)

            print("Item added to cart.")

        elif choice == 2:
            # Remove an item from the cart
            product_name = input("Enter the name of the product to remove: ")

            removed_product = shopping_cart.remove_item(product_name)

            if removed_product:
                print(f"{removed_product.name} removed from cart.")
            else:
                print("Product not found in cart.")

        elif choice == 3:
            # Calculate the total price
            total_price = shopping_cart.calculate_total_price()

            print("Total price: ${:.2f}".format(total_price))

        elif choice == 4:
            # Checkout
            shopping_cart.checkout()
            print("Thank you for shopping with us!")

        elif choice == 5:
            # Display the cart
            shopping_cart.display_cart()

        elif choice == 6:
            exit()

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

class OrderProcessor:
    def __init__(self, tax_rate, inventory):
        self.tax_rate = tax_rate  # float
        self.inventory = inventory  # dict: {product_id: quantity}
        self.cart = []

    def add_to_cart(self, product_id, quantity):
        if product_id not in self.inventory:
            raise ValueError("Product not found.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if self.inventory[product_id] < quantity:
            raise ValueError("Not enough stock.")
        self.cart.append((product_id, quantity))

    def calculate_total(self, prices):
        subtotal = 0
        for product_id, qty in self.cart:
            if product_id not in prices:
                raise ValueError("Missing price for product.")
            subtotal += prices[product_id] * qty
        return round(subtotal * (1 + self.tax_rate), 2)

    def checkout(self):
        for product_id, qty in self.cart:
            self.inventory[product_id] -= qty
        self.cart.clear()
        return "Order processed"

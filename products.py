class Product:
    def __init__(self, name: str, price: float, category: str, stock: int, brand: str, rating: float) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.brand = brand
        self.rating = rating


products = [
    Product("Laptop", 1200.00, "Electronics", 15, "Dell", 4.5),
    Product("Smartphone", 800.00, "Electronics", 30, "Samsung", 4.7),
    Product("Headphones", 150.00, "Audio", 50, "Sony", 4.3),
    Product("Monitor", 300.00, "Electronics", 20, "LG", 4.4),
    Product("Keyboard", 70.00, "Accessories", 100, "Logitech", 4.6),
    Product("Mouse", 50.00, "Accessories", 120, "Logitech", 4.5),
    Product("Webcam", 90.00, "Accessories", 35, "Razer", 4.2),
    Product("Printer", 200.00, "Office", 10, "HP", 4.1),
    Product("Tablet", 400.00, "Electronics", 25, "Apple", 4.8),
    Product("Smartwatch", 250.00, "Wearables", 40, "Fitbit", 4.4),
    Product("Speaker", 130.00, "Audio", 60, "JBL", 4.5),
    Product("Hard Drive", 110.00, "Storage", 80, "Seagate", 4.3),
    Product("SSD", 140.00, "Storage", 90, "Samsung", 4.7),
    Product("Router", 95.00, "Networking", 45, "TP-Link", 4.2),
    Product("Microphone", 120.00, "Audio", 70, "Blue", 4.6),
    Product("Charger", 35.00, "Accessories", 200, "Anker", 4.5),
    Product("Camera", 600.00, "Photography", 8, "Canon", 4.4),
    Product("Flash Drive", 25.00, "Storage", 300, "SanDisk", 4.6),
    Product("Power Bank", 45.00, "Accessories", 150, "Xiaomi", 4.3),
    Product("Projector", 550.00, "Office", 5, "Epson", 4.1),
]


product_names = []
for product in products:
 product_names.append(product.name)
print(product_names)

total_price = 0

for product in products:
    total_price += product.price
print(total_price)

expensive_product = max(products, key=lambda product: product.price)
print(expensive_product.price)

chippest_product = min(products, key=lambda product: product.price)
print(chippest_product.price)

categories_list = []
for product in products:
    categories_list.append(product.category)
print(categories_list)

brands = []
for product in products:
    brands.append(product.brand)
print(brands)

top_product = max(products, key=lambda product: product.rating)
print(f"{top_product.name} — reytingi: {top_product.rating}")

last_top_product = min(products, key=lambda product: product.rating)
print(f"{last_top_product.name} — reytingi: {last_top_product.rating}")


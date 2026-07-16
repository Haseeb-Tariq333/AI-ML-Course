class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
        
    def get_info(self):
        print(f"The name of the product is {self.name} and the price of the product is {self.price}")
        
    @classmethod  
    def get_count(cls):
        print(f"The total number of product are {cls.count}")
    
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount/100 * price)
        print(f"The price after {discount} % discount is {final_price}")
        
    
prod_1 = Product("Mobile", 12_000)
prod_2 = Product("Laptop", 40_000)

prod_1.get_info()
prod_2.get_info()
Product.get_count()

Product.calc_discount(40_000, 10)
from datetime import date

class Price:
    def __init__(self, price: float, date: date, amount: float, unity: str) -> None:
        self.price = price
        self.date = date
        self.amount = amount
        self.unity = unity
        
    def __str__(self) -> str:
        return f'Price: {self.price}, Amount: {self.amount}, Unity: {self.unity}, Date: {self.date}'
class Product:
    def __init__(self, image: str, name: str, description: str, brand: str) -> None:
        self.image = image
        self.name = name
        self.description = description
        self.brand = brand
        
    def __str__(self) -> str:
        return f'name: {self.name}, brand: {self.brand}'
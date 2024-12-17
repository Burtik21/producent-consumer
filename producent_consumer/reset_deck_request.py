from .request import Request  # Importujeme třídu Request

# Třída pro reset balíčku
class ResetDeck(Request):
    def __init__(self):
        super().__init__(priority=3)

    def process(self):
        print(f"Shuffling cards")

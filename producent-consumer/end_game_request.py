from request import Request  # Importujeme třídu Request

class EndGameRequest(Request):
    def __init__(self):
        super().__init__(priority=1)

    def process(self):
        print("Ending the game immediately!")

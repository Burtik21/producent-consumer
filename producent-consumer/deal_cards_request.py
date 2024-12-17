from .request import Request

class DealCardsRequest(Request):
    def __init__(self, player_id):
        super().__init__(priority=2)
        self.player_id = player_id

    def process(self):
        print(f"Dealing card to player {self.player_id}")

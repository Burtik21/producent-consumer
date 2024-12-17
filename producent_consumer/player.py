class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
        self.hand = []  # Seznam karet hráče

    def receive_card(self, card):
        """Přidání karty do ruky hráče."""
        self.hand.append(card)

    def play_card(self):
        """Odebere první kartu z ruky a vrátí ji."""
        if self.hand:
            return self.hand.pop(0)
        return None

    def show_hand(self):
        """Vrátí seznam karet hráče."""
        return self.hand

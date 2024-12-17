from producent_consumer.deal_cards_request import DealCardsRequest
from producent_consumer.end_game_request import EndGameRequest
from producent_consumer.reset_deck_request import ResetDeck


class RequestFactory:
    @staticmethod
    def create_request(input_str):
        if input_str.startswith("deal"):
            _, player = input_str.split()
            return DealCardsRequest(player_id=int(player))
        elif input_str == "end":
            return EndGameRequest()
        else:
            raise ValueError("Unknown request type")

import json
import os
from threading import Thread
from producent_consumer.linked_list_queue import LinkedListQueue
from producent_consumer.producer import Producer
from producent_consumer.consumer import Consumer
from producent_consumer.player import Player


class GameManager:
    def __init__(self, config_file="config.json", log_file="game_log.txt"):
        self.queue = LinkedListQueue()
        self.players = []  # Seznam hráčů

        # Nastavení cesty pro logovací soubor
        logs_folder = os.path.join(os.path.dirname(__file__), '..', 'logs')
        os.makedirs(logs_folder, exist_ok=True)
        self.log_file = os.path.join(logs_folder, log_file)

        # Vytvoření nebo vymazání logovacího souboru
        with open(self.log_file, 'w') as f:
            f.write("=== Game Log ===\n")

        # Načtení konfigurace
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config', config_file)
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        # Inicializace hráčů
        self.initialize_players()

        # Vytvoření producenta a konzumenta
        self.producer = Producer(self.queue, self.log)
        self.consumer = Consumer(self.queue, self.log)

    def initialize_players(self):
        """Vytvoření hráčů podle konfigurace."""
        number_of_players = self.config.get("number_of_players", 4)
        for i in range(1, number_of_players + 1):
            player = Player(player_id=i, name=f"Player {i}")
            self.players.append(player)
        self.log(f"Initialized {number_of_players} players.")

    def log(self, message):
        """Zapisuje zprávy do logovacího souboru."""
        with open(self.log_file, 'a', buffering=1) as f:
            f.write(message + "\n")

    def show_players(self):
        """Zobrazí hráče a jejich ruce."""
        for player in self.players:
            print(f"{player.name}: {len(player.hand)} card(s)")

    def run(self):
        """Spustí producenta a konzumenta."""
        self.show_players()  # Zobrazení hráčů na začátku hry
        producer_thread = Thread(target=self.producer.run)
        consumer_thread = Thread(target=self.consumer.run)

        producer_thread.start()
        consumer_thread.start()

        producer_thread.join()
        consumer_thread.join()

import requests

class ScryfallSDK:
    def __init__(self, base_url="https://api.scryfall.com"):
        self.base_url = base_url

    def search_cards(self, query):
        url = f"{self.base_url}/cards/search?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve cards: {response.status_code}")

    def get_card_by_name(self, name):
        url = f"{self.base_url}/cards/named?exact={name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")

    def get_card_by_id(self, card_id):
        url = f"{self.base_url}/cards/{card_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")

    def autocomplete_card_name(self, query):
        url = f"{self.base_url}/cards/autocomplete?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to autocomplete card name: {response.status_code}")

    def get_random_card(self, query=None):
        url = f"{self.base_url}/cards/random"
        if query:
            url += f"?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve random card: {response.status_code}")

    def get_cards_by_identifiers(self, identifiers):
        url = f"{self.base_url}/cards/collection"
        response = requests.post(url, json={'identifiers': identifiers})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve cards: {response.status_code}")

    def get_card_by_code_and_number(self, code, number):
        url = f"{self.base_url}/cards/{code}/{number}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")

    def get_card_by_multiverse_id(self, multiverse_id):
        url = f"{self.base_url}/cards/multiverse/{multiverse_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")

    def get_card_by_mtgo_id(self, mtgo_id):
        url = f"{self.base_url}/cards/mtgo/{mtgo_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")

    def get_card_by_arena_id(self, arena_id):
        url = f"{self.base_url}/cards/arena/{arena_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")

    def get_card_by_tcgplayer_id(self, tcgplayer_id):
        url = f"{self.base_url}/cards/tcgplayer/{tcgplayer_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")

    def get_card_by_cardmarket_id(self, cardmarket_id):
        url = f"{self.base_url}/cards/cardmarket/{cardmarket_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve card: {response.status_code}")
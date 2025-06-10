import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from scryfall import ScryfallSDK

class TestScryfallSDK(unittest.TestCase):
    def setUp(self):
        self.sdk = ScryfallSDK()

    def test_search_cards(self):
        result = self.sdk.search_cards("is:commander")
        self.assertIsNotNone(result)
        self.assertIn('data', result)

    def test_get_card_by_name(self):
        result = self.sdk.get_card_by_name("Black Lotus")
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Black Lotus')

    def test_get_card_by_id(self):
        # Search for a card and use its ID
        search_result = self.sdk.search_cards("is:commander")
        card_id = search_result['data'][0]['id']
        result = self.sdk.get_card_by_id(card_id)
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], card_id)

    def test_autocomplete_card_name(self):
        result = self.sdk.autocomplete_card_name("Blac")
        self.assertIsNotNone(result)
        self.assertIn('data', result)
        self.assertIn('Black Lotus', result['data'])

    def test_get_random_card(self):
        result = self.sdk.get_random_card()
        self.assertIsNotNone(result)
        self.assertIn('name', result)

    def test_get_cards_by_identifiers(self):
        identifiers = [{"id": "683a5707-cddb-494d-9b41-51b4584ded69"}]
        result = self.sdk.get_cards_by_identifiers(identifiers)
        self.assertIsNotNone(result)
        self.assertIn('data', result)

    def test_get_card_by_code_and_number(self):
        result = self.sdk.get_card_by_code_and_number("xln", "96")
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Costly Plunder')

    def test_get_card_by_multiverse_id(self):
        result = self.sdk.get_card_by_multiverse_id(409574)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Strip Mine')

    def test_get_card_by_mtgo_id(self):
        result = self.sdk.get_card_by_mtgo_id(54957)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Ghost Quarter')

    def test_get_card_by_arena_id(self):
        result = self.sdk.get_card_by_arena_id(67330)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Yargle, Glutton of Urborg')

    def test_get_card_by_tcgplayer_id(self):
        result = self.sdk.get_card_by_tcgplayer_id(162145)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Rona, Disciple of Gix')

    def test_get_card_by_cardmarket_id(self):
        result = self.sdk.get_card_by_cardmarket_id(379041)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Embodiment of Agonies')

if __name__ == '__main__':
    unittest.main()
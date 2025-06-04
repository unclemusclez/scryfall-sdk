# Scryfall SDK

Scryfall SDK is a Python package for interacting with the Scryfall API.

## Installation

pip install scryfall-sdk

## Usage

from scryfall_sdk import ScryfallSDK

sdk = ScryfallSDK()
cards = sdk.search_cards("lightning bolt")

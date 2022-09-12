"""Importing modules"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# API and URL declaration
APIKEY = os.environ['apikey']
URL = os.environ['url']

# Initiating translation
authenticator = IAMAuthenticator(APIKEY)

language_translator = LanguageTranslatorV3(
    version='2022-09-11',
    authenticator=authenticator
)

# setting url for translation
language_translator.set_service_url(URL)


def english_to_french(english_text):
    """Function to translate from English to French"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """Function to translate from French to English"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text

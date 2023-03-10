"""This module provides functions for translating text from English to French and vice versa"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# IBM Watson Language Translator API credentials
apikey = os.environ['apikey']
url = os.environ['url']

# Set up Language Translator client
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(text):
    """Translates English text to French"""
    if text is None:
        return None
    if not text.strip():
        return ''
    translation = language_translator.translate(
        text=text,
        source='en',
        target='fr').get_result()
    return translation['translations'][0]['translation']


def french_to_english(text):
    """Translates French text to English"""
    if text is None:
        return None
    if not text.strip():
        return ''
    translation = language_translator.translate(
        text=text,
        source='fr',
        target='en').get_result()
    return translation['translations'][0]['translation']

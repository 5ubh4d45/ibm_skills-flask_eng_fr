"""
translator module which uses IBM Watson Language Translator API \
    to translate text from one language to another.
"""

import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

# load the environment variables
load_dotenv()
API_KEY = os.environ['API_KEY']
URL = os.environ['URL']

# setup ibm watson language translator
authenticator = IAMAuthenticator(apikey=API_KEY)
translator_service = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

translator_service.set_service_url(URL)


# translator_service.set_disable_ssl_verification(True)


def english_to_french(english_text):
    # write the code here
    # switch case for NONE input
    if english_text is None:
        return ""

    # strip the text for empty string
    english_text = english_text.strip()

    # switch case for empty string
    if english_text == "":
        return ""

    # translate the text
    french_text = translator_service.translate(
        text=english_text,
        model_id='en-fr').get_result()

    # filter the translated text
    french_text = french_text['translations'][0]['translation']

    return french_text


def french_to_english(french_text):
    # write the code here
    # switch case for NONE input
    if french_text is None:
        return ""

    # strip the text for empty string
    french_text = french_text.strip()

    # switch case for empty string
    if french_text == "":
        return ""

    # translate the text
    english_text = translator_service.translate(
        text=french_text,
        model_id='fr-en').get_result()

    # filter the translated text
    english_text = english_text['translations'][0]['translation']

    return english_text

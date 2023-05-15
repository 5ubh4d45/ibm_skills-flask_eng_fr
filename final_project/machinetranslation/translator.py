"""
translator module which uses IBM Watson Language Translator API \
    to translate text from one language to another.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

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


def englishToFrench(englishText):
    #write the code here
    # switch case for NONE input
    if englishText is None:
        return ""
    
    # strip the text for empty string
    englishText = englishText.strip()

    # switch case for empty string
    if englishText == "":
        return ""
    
    # translate the text
    frenchText = translator_service.translate(
        text=englishText,
        model_id='en-fr').get_result()
    
    # filter the translated text
    frenchText = frenchText['translations'][0]['translation']

    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    # switch case for NONE input
    if frenchText is None:
        return ""
    
    # strip the text for empty string
    frenchText = frenchText.strip()

    # switch case for empty string
    if frenchText == "":
        return ""
    
    # translate the text
    englishText = translator_service.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    
    # filter the translated text
    englishText = englishText['translations'][0]['translation']
    
    return englishText
"""
translator module which uses IBM Watson Language Translator API \
    to translate text from one language to another.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv()
apikey = os.environ['API_KEY']
url = os.environ['URL']

def englishToFrench(englishText):
    #write the code here
    return "frenchText"

def frenchToEnglish(frenchText):
    #write the code here
    return "englishText"
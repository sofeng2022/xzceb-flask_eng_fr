"""Module providing language translation."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
ak = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

ak.set_service_url(url)

translation = ak.translate(text='Hola, cómo eres?',model_id='es-en').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

def english_to_french(english_text):
    """
    This function translates the text from english to french
    """
    english_text = translation['translations'][0]['translation']
    french_text = ak.translate(text = english_text,model_id ='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    This function translates the text from french to english
    """
    english_text = ak.translate(text=french_text,model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
    
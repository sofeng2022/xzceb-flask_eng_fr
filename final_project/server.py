from .. import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder="static")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = ak.translate(text = english_text,model_id ='en-fr').get_result()
    return "Translated text to French"

print(englishToFrench())

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = ak.translate(text=french_text,model_id='fr-en').get_result()
    return "Translated text to English"

print(frenchToEnglish())

@app.route("/index")
def renderIndexPage():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

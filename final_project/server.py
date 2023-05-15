from flask import Flask, request

from machinetranslation import translator

# from testpack import translator

app = Flask("Web Translator")


@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('text')
    # Write your code here
    return translator.english_to_french(text_to_translate)


@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('text')
    # Write your code here
    return translator.french_to_english(text_to_translate)


@app.route("/")
def render_index_page():
    # Write the code to render template
    return "Translated text to English"


# print(translator.englishToFrench("Hello"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

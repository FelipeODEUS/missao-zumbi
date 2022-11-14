from flask import Flask, render_template, request, jsonify
from model_prediction import *

app = Flask(__name__)

text=""
predicted_emotion=""
predicted_emotion_img_url=""

#renderize a página HTML
@app.route("/")
def home():
    entries = show_entry()
    return render_template("index.html", entries=entries)
    
#preveja a emoção
@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    input_text = request.json.get("text")
    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Digite um texto para prever a emoção!"
        }), 400
    else:
        predicted_emotion, predicted_emotion_img_url = predict(input_text)                         
        return jsonify({
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emotion_img_url": predicted_emotion_img_url
            },
            "status": "success"
        }), 200
        
# Proteja a entrada   
@app.route("/Proteja_a_entrada", methods=["POST"])
def elimine_os_zumbis():
    dia_da_infecssao = request.json.get("date")
    transformassao = request.json.get("emotion")
    frase = request.json.get("text")
    frase = frase.replace("\n"," ")
    cura = f'{dia_da_infecssao},{frase},{transformassao}\n'
    with open("./static/assets/data_files/data_entry.csv","a")as var:
        var.write(cura)
    return jsonify("Success")
if __name__ == "__main__":
    app.run(debug=True)




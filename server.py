from flask import Flask, send_file, request, jsonify
from flask_cors import CORS, cross_origin
from predict import get_emotion
from database import cursor
import random
import base64

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=["POST", "GET"])
@cross_origin()
def index():
    if request.method == "POST":
        data = request.get_json()
        image_str = data.get('imageSrc')
        li = image_str.split(',',1)
        image_data = base64.b64decode(li[1])
        with open("input.jpg", "wb") as fh:
            fh.write(image_data)
        emo = get_emotion('./input.jpg')
        if emo == "sad" or emo == "angry" or emo == "disgust":
            cursor.execute("SELECT * FROM sad;")
        elif emo == "happy" or emo == "surprise" or emo == "neutral" or emo == "fear":
            cursor.execute("SELECT * FROM happy;")
        else:
            return  jsonify(emotion=emo)
        
        data = cursor.fetchall()
        music = random.choice(data)
        print(music)
        return jsonify(
            emotion = emo,
            id = music[0],
            name = music[1]
        )

    if request.method == "GET":
        emotion = request.args.get('emo')
        print(emotion)
        id = request.args.get('id')
        if emotion == "sad" or emotion == "angry" or emotion == "disgust":
            cursor.execute(f"SELECT * FROM sad WHERE id='{id}';")
        elif emotion == "happy" or emotion == "surprise" or emotion == "neutral" or emotion == "fear":
            cursor.execute(f"SELECT * FROM happy WHERE id='{id}';")
        data = cursor.fetchall()
        music = data[0]
        return send_file(music[2], as_attachment=True)



if __name__ == "__main__":
    app.run(debug=False)

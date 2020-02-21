from flask import Flask, request, render_template, send_from_directory
import config
import audio_helper
import random

app = Flask(__name__)

# Home
@app.route("/")
def index():
    return render_template("index.html")


# Share page
@app.route("/share/<int:sound_id>")
def share_page(sound_id):
    return render_template("share.html", sound_id=sound_id)

# API route
@app.route("/create", methods=["POST"])
def api_create():
    file_name = random.randint(1, 1000000)
    temp_path = f"./temp_sounds/{file_name}.wav"
    f = open(temp_path, "wb")
    f.write(request.data)
    f.close()
    sound = audio_helper.create_sound(temp_path)
    sound.export(f"./static/sounds/{file_name}.mp3", format="mp3")
    return str(file_name)

if config.DEBUG:
    # Static Files
    @app.route("/static/<path:path>")
    def send_js(path):
        return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=config.DEBUG)
from flask import Flask, request, render_template, send_from_directory
import config
import audio_helper
import os
import str_helper

app = Flask(__name__)

# Home
@app.route("/")
def index():
    return render_template("index.html")


# Share page
@app.route("/share/<sound_id>")
def share_page(sound_id):
    return render_template("share.html", sound_id=sound_id)

# API routes
@app.route("/create/<prefix>", methods=["POST"])
def api_create(prefix):
    not_new = True
    while not_new:
        file_name = str_helper.random_string()
        temp_path = f"./temp_sounds/{file_name}.wav"
        if not os.path.exists(f"./static/sounds/{file_name}.mp3"):
            not_new = False
    f = open(temp_path, "wb")
    f.write(request.data)
    f.close()
    sound = audio_helper.create_sound(temp_path, prefix=f"sounds/{prefix}_prefix.wav")
    sound.export(f"./static/sounds/{file_name}.mp3", format="mp3")
    os.remove(temp_path)
    return str(file_name)


if config.DEBUG:
    # Static Files
    @app.route("/static/<path:path>")
    def send_js(path):
        return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=config.DEBUG)

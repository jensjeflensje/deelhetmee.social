from flask import Flask, request, render_template, send_from_directory, jsonify
import config
import server_helper

app = Flask(__name__)

# Home
@app.route("/")
def index():
    return render_template("index.html", prefixes=prefix_list)

# Share page
@app.route("/share/<sound_id>")
def share_page(sound_id):
    return render_template("share.html", sound_id=sound_id)

# API routes
@app.route("/getserver")
def api_getserver():
    server = server_helper.get_server()
    return jsonify(server)

@app.route("/savesound", methods=["POST"])
def api_savesound():
    if request.args.get("token") == config.TOKEN:
        sound_file = request.files.get("sound")
        sound_name = request.args.get("name")
        if sound_file:
            sound_file.save(f"./static/sounds/{sound_name}.mp3")
            return "success"
        else:
            return "no sound file"
    else:
        return "invalid token"

if config.DEBUG:
    # Static Files
    @app.route("/static/<path:path>")
    def send_js(path):
        return send_from_directory('static', path)

if __name__ == "__main__":
    prefixes = server_helper.get_prefixes()
    prefix_list = [{"name": config.PREFIX_NAMES[prefix], "prefix": prefix} for prefix in prefixes]
    app.run(host="0.0.0.0", debug=config.DEBUG)

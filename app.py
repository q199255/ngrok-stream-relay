from flask import Flask, Response, stream_with_context
import requests
import os

app = Flask(__name__)
SOURCE_URL = os.environ.get("NGROK_URL")

@app.route("/stream.mp3")
def proxy_stream():
    def generate():
        with requests.get(SOURCE_URL, stream=True) as r:
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    yield chunk
    return Response(stream_with_context(generate()), mimetype="audio/mpeg")

@app.route("/")
def index():
    return "<h1>Stream is running</h1>"

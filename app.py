from flask import Flask, Response
import requests
import os

app = Flask(__name__)

NGROK_URL = os.getenv("https://a42ee3cb9fb5.ngrok-free.app/stream.mp3")

@app.route('/')
def stream():
    def generate():
        with requests.get(NGROK_URL, stream=True) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
    return Response(generate(), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

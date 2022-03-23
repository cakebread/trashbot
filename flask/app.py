import random

from flask import Flask, Response
from flask_cors import CORS, cross_origin
import redis

app = Flask(__name__)
app.config["CORS_HEADERS"] = "Content-Type"
cors = CORS(app)

r = redis.StrictRedis(
    host="redis", port=6379, db=0, charset="utf=8", decode_responses=True
)


def event_stream():
    pubsub = r.pubsub()
    pubsub.subscribe("kxlu")
    for message in pubsub.listen():
        if message["data"] == 1:
            recent = r.lrange("playlist", 0, 0)
            if len(recent) == 0:
                playing = "KXLU... tuning in..."
            else:
                playing = recent[0]
            yield "data: %s\n\n" % playing
        else:
            yield "data: %s\n\n" % message["data"]
            yield "id: %s\n\n" % random.randint(1, 65000)


@app.route("/stream")
@cross_origin()
def stream():
    return Response(event_stream(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True)

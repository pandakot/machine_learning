from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    q = request.args.get('query', None)

    return jsonify(dict(img_name='some_name.jpg', query=q))


if __name__ == '__main__':
    app.run()
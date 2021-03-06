from flask import Flask, request, jsonify
import pickle as pickle

import predict_nn

model_folder = 'model_5m_fr10'
app = Flask(__name__)
mapping = pickle.load(open(model_folder + '/mapping.pkl', 'rb'))


@app.route('/')
def hello_world():
    q = request.args.get('query', None)

    img_id = predict_nn.predict(q, model_folder + '/model_nn.pkl', model_folder + '/dict.txt')
    img_name = mapping[str(img_id)]

    return jsonify(dict(img_id=img_id, img_name=img_name, query=q))


if __name__ == '__main__':
    app.run()

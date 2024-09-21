import numpy as np
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

model = pickle.load(open('myshallownetwork.pickle', 'rb'))


class ShallowNetwork(object):
    def __init__(self):
        self.weigths = model.get('weigths')
        self.bias = model.get('bias')

    def sigmoid_function(self, x):
        return 1/(1 + np.exp(-x))

    def neuralnet(self, x_input):
        result = np.dot(x_input, self.weigths) + self.bias
        return self.sigmoid_function(result)

    def predict(self, x_input):
        x_input = np.array(x_input)
        pred = self.neuralnet(x_input)
        pred = list(pred)
        if pred:
            pred = round(pred[0])
        else:
            pred = 0    
        return {"output": pred}

# laoding my network
N_N = ShallowNetwork()

@app.route('/api/test', methods=['GET', 'POST'])
def myneuralnetwork():
    if request.method == 'GET':
        return jsonify('This is own trained network')
    else:
        input_json = request.json
        input_arr = input_json['input_arr']
        output = N_N.predict(input_arr)
        return jsonify(output)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8999)

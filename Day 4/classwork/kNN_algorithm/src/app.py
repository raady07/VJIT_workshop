from flask import Flask, request, jsonify
from my_knn import MyKnn

app = Flask(__name__)

# i have determined my kNN works best for k value = 5
mykNN = MyKnn(5)


@app.route('/api/myknn', methods=['GET', 'POST'])
def myknn():
    if request.method == 'GET':
        return jsonify("This is my first kNN.")
    else:
        input_json = request.json
        sl = input_json['sepal_lenght']
        sw = input_json['sepal_width']
        pl = input_json['petal_lenght']
        pw = input_json['petal_width']
        pred = mykNN.prediction([sl, sw, pl, pw])
        return jsonify(
            {"petal": pred}
        )


if __name__ == '__main__':
    app.run('0.0.0.0', port=9999)

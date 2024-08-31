from flask import Flask, request, jsonify
from module1.mymathformulas import MyMathFormalus

app = Flask(__name__)
api_active = 'I am alive'

def multiplier(x, y):
    return x**10 + y**2

@app.route('/test1', methods=['GET', 'POST'])
def checking_test_route():
    if request.method == 'GET':
        return api_active
    else:
        input_data = request.json
        x = input_data.get('x', 0)
        y = input_data.get('y', 0)
        output = multiplier(x, y)
        result = MyMathFormalus(x, y).run()
        print(x,y)
        return jsonify(result)

if __name__ == '__main__':
    app.run("0.0.0.0", port=8013)



# output = multiplier(2, 3)

# print(output)
from flask import Flask, request, jsonify

from variables import CONFIG
from storageutils import MySQLManager

app = Flask(__name__)


def insert_data(id, person, classyear):
    query = "insert into sample values('{}', '{}', {});".format(id, person, classyear)
    try:
        MySQLManager.execute_query(query, None, **CONFIG['database']['vjit'])
    except Exception as error:
        print(error)
    return None


def check_data(id):
    query = 'select * from sample where id = "{}"'.format(id)
    result = {}
    try:
        result = MySQLManager.execute_query(query, None, **CONFIG['myvalues'])
    except Exception as error:
        print(error)
    return result[0]


@app.route('/data/insert', methods=['GET', 'POST'])
def mystudentdatabase():
    if request.method == 'GET':
        return "Im Alive"
    else:
        _input = request.json
        id = _input.get("id", "")
        person = _input.get("person", '')
        classyear = _input.get("classyear", 1)
        insert_data(id, person, classyear)
        return jsonify("Data Inserted")


@app.route('/data/checkdetails', methods=['GET', 'POST'])
def mystudentdatabasedetails():
    if request.method == 'GET':
        return "Im Alive"
    else:
        _input = request.json
        id = _input.get("id", "")
        result = check_data(id)
        return jsonify(result)


if __name__ == '__main__':
    app.run("0.0.0.0", port=8407)
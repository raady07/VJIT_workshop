#!flask/bin/python
from flask import Flask, request, jsonify, abort
from storageutils import MySQLManager
from config import CONFIG


app = Flask(__name__)


def insert_data(student_name, roll, s_year, gender, course, joinedyear):
    query = 'insert into students values("{}", "{}", "{}", {}, "{}", "{}");'.format(
        student_name, roll, gender, s_year, course, joinedyear)
    status = 'failed'
    try:
        res = MySQLManager.execute_query(query, None, **CONFIG['database']['gnits'])
        status = 'sucessful'
    except Exception as error:
        print(error)
    return status

@app.route('/api/studentdatabase', methods=['GET', 'POST'])
def mystudentdatabase():
    if request.method == 'GET':
        return "Im Alive"
    else:
        """
            input: 1. insert query 
                {
                    'studentname': "sample",
                    'rollnumber': "12321",
                    'study_year': 3,
                    'gender': "male",
                    'course': "ece",
                    'joinedyear': "2024"
                }
        """
        input_json = request.json
        student_name = input_json.get('studentname', "")
        roll = input_json.get('rollnumber', 0)
        s_year = input_json.get('study_year', 1)
        gender = input_json.get('gender', "male")
        course = input_json.get('course', '')
        joinedyear = input_json.get('joinedyear', "2024")
        res = insert_data(student_name, roll, s_year, gender, course, joinedyear)
        return jsonify(res)


if __name__ == '__main__':
    app.run("0.0.0.0", port=8407)

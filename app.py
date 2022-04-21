from crypt import methods
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
import json

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this on deployment
api = Api(app)
file = open('todos.txt', 'a+')
# L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
# file.write("yeen \n")
# file.seek(0)
# lines = file.readlines()
# print(lines)


@app.route("/")
def index():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/update', methods=['GET'])
def helloWorld():
    file.seek(0)
    return {"todos": file.readlines()}

@app.route('/update', methods=['POST'])
def updateTodo():
    parser = reqparse.RequestParser()
    parser.add_argument("type", type=str)
    parser.add_argument("message", type=str)

    args = parser.parse_args()

    print(args)

    request_type = args['type']
    request_msg = args['message']
    print(request_type)
    print(request_msg)
    
    # currently just returning the request straight back
    if request_type == "create" and request_msg != "":
        ret_msg = "Your Message: yeen"
        file.write(request_msg + "\n")
        file.seek(0)

    elif request_type == "delete":
        file.seek(0)
        lines = file.readlines()
        lines.remove(request_msg)
        file.truncate(0)
        for line in lines:
            file.write(line)
        # for line in file:
        #     if request_msg in line:
        #         line = line.replace(request_msg, "")
        #     file.write(line)



    
    final_ret = {}

    return final_ret

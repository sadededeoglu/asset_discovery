from flask import Flask, request
from flask_restful import Resource, Api
from control import checkControl

app = Flask(__name__)
api = Api(app)

class nmapCheck(Resource):
    def get(self, IPAddress):
       return(checkControl.checkNmap(IPAddress))

api.add_resource(nmapCheck, '/nmap/<string:IPAddress>')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)

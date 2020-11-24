from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from control import control

app = Flask(__name__)
api = Api(app)

class nmapCheck(Resource):
    def get(self, IPAddress):
       return(checkConn.checkNmap(IPAddress))

api.add_resource(nmapCheck, '/nmap/<string:IPAddress>/')

if __name__ == '__main__':
    app.run(host='192.168.1.129', port='5000', debug=True)

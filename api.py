from flask import Flask, json, jsonify
from flask_restful import reqparse, abort, Api, Resource, request
import json, sys


app = Flask(__name__)
api = Api(app)

entries = {
    "num_entries" : 0,
    "entries" :
    [

    ]
}

class Entries(Resource):
    def get(self):
        return jsonify(entries)

    def post(self):
        """
        args = parser.parse_args()
        d = {}
        k = args['key']
        v = args['value']
        d['k'] = v
        """
        d = request.get_json(force=True)
        entries["entries"].append(d)
        entries["num_entries"] +=1
        return entries


api.add_resource(Entries, '/api/v1/entries')


if __name__ == '__main__':
    portnum = sys.argv[1]
    app.run(host='localhost', port=portnum, debug=True)

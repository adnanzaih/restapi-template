from flask import Flask
from flask_restx import Api, Resource
from auth import token_required
from core.system import ClassSystem

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

app = Flask(__name__)
api = Api(app, 
          title="SIMPLE FLASK-REST API TEMPLATE", 
          version="0.1",
          authorizations=authorizations,
          security="apiKey",
          prefix='/api/v1', 
          description='This is a Flask-RESTX API Template designed to serve as a boilerplate for creating RESTful APIs with security and modularity in mind. The template provides a basic structure to handle authenticated requests and interact with backend systems.')

ns = api.namespace('General')

@ns.route('/system/')
class Operations(Resource):
    @ns.doc(security='apikey')
    @token_required
    def get(self):
        obj = ClassSystem()
        return obj.get_system_info()
    
    @ns.doc(security='apikey')
    @token_required
    def put(self):
        obj = ClassSystem()
        return obj.get_system_info()
    
    @ns.doc(security='apikey')
    @token_required
    def delete(self):
        obj = ClassSystem()
        return obj.get_system_info()
    
    @ns.doc(security='apikey')
    @token_required
    def post(self):
        obj = ClassSystem()
        return obj.get_system_info()

if __name__ == '__main__':
    app.run()
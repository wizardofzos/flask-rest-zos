from flask import Flask
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

app = Flask(__name__)  
api = Api(app)  
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',       
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  
})
docs = FlaskApiSpec(app)



from endpoints import DemoAPI

api.add_resource(DemoAPI, '/demo')
docs.register(DemoAPI)



if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 12345))
    app.run(debug=True, host='0.0.0.0', port=port)
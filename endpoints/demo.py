from marshmallow import Schema, fields
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_restful import Resource
from flask import abort

class DemoResponseSchema(Schema):
    message = fields.Str(default='Success')


class DemoRequestSchema(Schema):
    demo = fields.String(required=True, description="API type of awesome API")


#  Restful way of creating APIs through Flask Restful
class DemoAPI(MethodResource, Resource):
    @doc(description='My Demo GET Awesome API.', tags=['Demo'],
    responses={
        '200': {'description': 'Everything is ok!'},
    }
    )
    
    @marshal_with(DemoResponseSchema)  # marshalling
    def get(self):
        '''
        Get method represents a GET API method
        '''
        return {'message': 'My First Demo API'}

    @doc(description='My Demo POST Awesome API.', tags=['Demo'],
    responses={
        '200': {'description': 'Everything is ok!'},
        '418': {'description': 'Cannot have teapot as demo field.'}
    })
    @use_kwargs(DemoRequestSchema, location=('json'))
    @marshal_with(DemoResponseSchema)  # marshalling
    def post(self, demo):
        '''
        Get method represents a GET API method
        '''
        if demo == 'teapot':
            abort(418, "Oef!")
        return {'message': f'demo from request={demo}'}
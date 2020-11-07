from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import json

from random import randint

app = Flask(__name__)
api = Api(app, version="1.0", title="API title", description="A simple API example")
ns_todos = api.namespace('todos', description='Todos operations')

todos = []

todo_model = api.model('todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

@ns_todos.route("/")
class TodoList(Resource):
    @ns_todos.doc('list_todos')
    @ns_todos.marshal_list_with(todo_model)
    def get(self):
        """
        Returns a list of todos
        """
        return todos

    @ns_todos.doc('create_todo')
    @ns_todos.expect(todo_model)
    @ns_todos.marshal_with(todo_model, code=201)
    def post(self):
        """
        Adds a new todo to the list
        """
        todo = api.payload
        todo['id'] = randint(0, 1000)
        todos.append(todo)
        return todo

@ns_todos.route("/<int:id>")
@ns_todos.response(404, 'Todo not found')
@ns_todos.param('id', 'The task identifier')
class Todo(Resource):

    @ns_todos.doc('get_todo')
    @ns_todos.marshal_with(todo_model)
    def get(self, id):
        '''Fetch a given resource'''
        for todo in todos:
            if todo['id'] == id:
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

    @ns_todos.doc('delete_todo')
    @ns_todos.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        for todo in todos:
            if todo['id'] == id:
                todos.remove(todo)
                return '', 204
        api.abort(404, "Todo {} doesn't exist".format(id))

    @ns_todos.expect(todo_model)
    @ns_todos.marshal_with(todo_model)
    def put(self, id):
        '''Update a task given its identifier'''
        for todo in todos:
            if todo['id'] == id:
                todo.update(api.payload)
                return todo
        api.abort(404, "Todo {} doesn't exist".format(id))

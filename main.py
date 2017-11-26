from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from urllib.request import urlopen, Request
import os   

app = Flask(__name__)
api = Api(app)

TODOS = []

def abort_if_todo_doesnt_exist(id):
    if id not in TODOS:
        abort(404, message="Todo {} doesn't exist!!!".format(id))

parser = reqparse.RequestParser()
parser.add_argument('barcode')
parser.add_argument('name')
parser.add_argument('price')
parser.add_argument('active')
parser.add_argument('category_id'),
parser.add_argument('duedate')




# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, id ):
        return jsonify({'alimentos': TODOS[id]})


    def delete(self, id ):
        ######abort_if_todo_doesnt_exist(id)
         for person in TODOS:
            if person['barcode'] == id:
               TODOS.pop(person['id'])
               return jsonify({'alimentos': person})


    def put(self, id):
        args = parser.parse_args()
        task = { 'id': id,'barcode': args['barcode'],'name': args['name'],'price': args['price'],'active': args['active'],'category_id': args['category_id'],'duedate': args['duedate']}
        TODOS[id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
            return jsonify({'alimentos': TODOS})


    def post(self):
       
        args = parser.parse_args()
        id =   len(TODOS)
        todo_id = 'alimento%i' % id
        TODOS.append({ 'id': id,'barcode': args['barcode'],'name': args['name'],'price': args['price'],'active': args['active'],'category_id': args['category_id'],'duedate': args['duedate']})
        return TODOS[id], 201



##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/api/todos')
api.add_resource(Todo, '/api/todos/<string:id>')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
   port = int(os.environ.get('PORT', 5000))
   # Tem que ser 0.0.0.0 para rodar no Heroku
   app.run(host='0.0.0.0', port=port)

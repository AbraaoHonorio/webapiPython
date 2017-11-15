from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

TODOS = {
    
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('Código de barra')
parser.add_argument('Nome')
parser.add_argument('Preço')
parser.add_argument('Ativo')
parser.add_argument('Categoria'),
parser.add_argument('Vencimento')




# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        id =   (len(TODOS) +1) #int(max(TODOS.keys()).lstrip('alimento')) 
        todo_id = 'alimento%i' % id
        TODOS[todo_id] = {'id': id,'Código de barra': args['Código de barra'],'Nome': args['Nome'],'Preço': args['Preço'],'Ativo': args['Ativo'],'Categoria': args['Categoria'],'Vencimento': args['Vencimento']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
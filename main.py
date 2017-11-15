from flask import Flask, jsonify, request,abort
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os   

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/api/v1/stock', methods=['GET'])
def filmes():
    html_doc = urlopen("http://globoesporte.globo.com/futebol/selecao-brasileira/").read()
    soup = BeautifulSoup(html_doc, "html.parser")
    a = ['Feijão', 'Arroz', 'Sabão', 'Carne', 'Biscoito']
    b = [5.00, 3.50 , 2.55, 20.50, 1.7]
    c = ['Alimentos', 'Alimentos', 'Limpeza', 'Carnes', 'Padaria']
    at = [1,0,0,0,1]
    l = list(range(10000000,10000005))
    data = []
    for i in range(5):
       
       data.append({'Código de barra' : l[i],
                    'Nome:': a[i],
                    'Preço:' : b[i],
                    'Ativo:' : at[i],
                    'Categoria' : c[i],
                    'Vencimento' :  "07/11/2017"})
                         #'Categoria' : c[i]})
                        #'data' :  dataObj.text[1:23].strip().replace('/',' ')})
                
    return jsonify({'Estoque': data})


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True)

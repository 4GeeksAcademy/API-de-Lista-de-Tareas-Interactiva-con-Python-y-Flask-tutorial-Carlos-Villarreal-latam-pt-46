from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ 
    { "label": "My first task", "done": False }
]


#@app.route('/todos', methods=['GET'])
#def hello_world():
#    return '<h1>Hello!</h1>'


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    
     #Agregar el nuevo todo a la lista
    todos.append(request_body)

    print("Incoming request with the following body", request_body)
    #return 'Response for the POST todo'
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    #return 'something'

    todos.pop(position)

    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
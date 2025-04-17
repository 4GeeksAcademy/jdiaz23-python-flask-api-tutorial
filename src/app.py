from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "Sample Todo 1", "done": True },
    { "label": "Sample Todo 2", "done": False },
    { "label": "Sample Todo 3", "done": False },    
     ]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


def show_todos():
    return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

# Criar uma tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

# Listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id < len(tasks):
        tasks[task_id] = request.json
        return jsonify(tasks[task_id])
    return jsonify({"error": "Tarefa não encontrada"}), 404

# Excluir uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id < len(tasks):
        task = tasks.pop(task_id)
        return jsonify(task)
    return jsonify({"error": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)

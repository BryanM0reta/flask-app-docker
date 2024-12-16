from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Lista de tareas
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            tasks.append({"task": new_task, "completed": False})
    return render_template("index.html", tasks=tasks)

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    tasks[task_id]["completed"] = True
    return jsonify({"status": "success"})

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks.pop(task_id)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask, render_template
from planner import load_tasks, calculate_daily_target

app = Flask(__name__)

@app.route("/")
def dashboard():

    tasks = load_tasks()

    data = []

    for task in tasks:

        target = calculate_daily_target(
            task["total"],
            task["completed"],
            task["deadline"]
        )

        data.append({
            "name": task["name"],
            "target": target
        })

    return render_template("dashboard.html", tasks=data)

if __name__ == "__main__":
    app.run(debug=True)
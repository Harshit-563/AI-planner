import json
from datetime import datetime
from youtube_parser import get_playlist_length

def load_tasks():
    with open("tasks.json", "r") as f:
        return json.load(f)

def calculate_daily_target(total, completed, deadline):

    today = datetime.today().date()
    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()

    remaining_work = total - completed
    days_left = (deadline - today).days

    if days_left <= 0:
        return remaining_work

    return max(1, round(remaining_work / days_left))

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def generate_today_plan():

    tasks = load_tasks()

    print("\nToday's Study Plan\n")

    for task in tasks:

        # Determine total and completed work
        if task.get("type") == "dsa":

            total = task["total"]
            completed = count_solved_problems()

        elif task.get("type") == "youtube":

            total = get_playlist_length(task["url"])
            completed = task["completed"]

        else:

            total = task["total"]
            completed = task["completed"]

        # Calculate daily target
        target = calculate_daily_target(
            total,
            completed,
            task["deadline"]
        )

        print(task["name"])
        print("Total:", total)
        print("Completed:", completed)
        print("Do today:", target)
        print()
        save_tasks(tasks)

def log_progress(task_name, amount):

    try:
        with open("progress_log.json","r") as f:
            log = json.load(f)
    except:
        log = {}

    if task_name not in log:
        log[task_name] = []

    log[task_name].append(amount)

    with open("progress_log.json","w") as f:
        json.dump(log,f,indent=4)

def get_average_speed(task_name):

    with open("progress_log.json","r") as f:
        log = json.load(f)

    if task_name not in log:
        return 0

    data = log[task_name]

    return sum(data)/len(data)


def analyze_deadline_risk():

    tasks = load_tasks()

    print("\nDeadline Risk Analysis\n")

    for task in tasks:

        if task["type"] == "youtube":
            total = get_playlist_length(task["url"])
        else:
            total = task["total"]

        completed = task["completed"]

        remaining_work = total - completed

        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        today = datetime.today().date()

        days_left = (deadline - today).days

        if days_left <= 0:
            print(f"{task['name']} deadline already passed!")
            continue

        required_speed = remaining_work / days_left
        avg_speed = get_average_speed(task["name"])

        print(task["name"])
        print("Required speed:", round(required_speed,2), "per day")
        print("Your speed:", round(avg_speed,2), "per day")

        if avg_speed < required_speed:
            print("⚠️ You may miss the deadline\n")
        else:
            print("✅ You are on track\n")
            
import os

def count_solved_problems():

    folder = r"D:\DSA"

    total = 0

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".cpp") or file.endswith(".py") or file.endswith(".java"):
                total += 1

    return total

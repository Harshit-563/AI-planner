from planner import load_tasks, calculate_daily_target, count_solved_problems
from notifier import send_message



def progress_check():

    tasks = load_tasks()

    message = "📊 Study Planner Update\n\n"

    for task in tasks:

        if task["type"] == "dsa":

            current = count_solved_problems()
            previous = task["completed"]

            today_done = current - previous

            task["completed"] = current

            total = task["total"]

        else:

            total = task["total"]
            today_done = 0

        target = calculate_daily_target(
            total,
            task["completed"],
            task["deadline"]
        )

        remaining = max(0, target - today_done)

        message += f"{task['name']}\n"
        message += f"Target today: {target}\n"
        message += f"Solved today: {today_done}\n"
        message += f"Remaining today: {remaining}\n\n"

    send_message(message)


if __name__ == "__main__":
    progress_check()
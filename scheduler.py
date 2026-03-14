from apscheduler.schedulers.blocking import BlockingScheduler
from progress_checker import progress_check

scheduler = BlockingScheduler()

print("Scheduler started... Waiting for checks")

scheduler.add_job(progress_check, 'cron', hour=14)
scheduler.add_job(progress_check, 'cron', hour=18)
scheduler.add_job(progress_check, 'cron', hour=22)

scheduler.start()
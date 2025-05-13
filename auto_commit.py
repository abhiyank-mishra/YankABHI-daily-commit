import datetime
import random
import os

file_name = "daily_log.txt"
messages = [" Daily Update", " Just Checking In", " GitHub Automation Baby!"]
message = random.choice(messages)
now = datetime.datetime.now()

with open(file_name, "a") as f:
    f.write(f"{now} - {message}\n")

os.system("git add .")
os.system(f'git commit -m "Auto commit: {message}"')
os.system("git push origin main")

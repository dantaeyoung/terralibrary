import subprocess
def say(text):
    subprocess.call(["espeak-ng", "-v", "mb-en1", "-p", "30", "-s", "145", text ])


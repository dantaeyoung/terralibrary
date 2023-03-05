import subprocess
def say(text, printtext=True):
    if(printtext):
        print("[SAYING] " + text)
    subprocess.call(["espeak-ng", "-v", "mb-en1", "-p", "30", "-s", "155", text ])


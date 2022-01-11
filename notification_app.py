import time
# pip install plyer
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Make a project!",
            message = "I have to make a project and learn something new.",
            timeout = 10
        )
        time.sleep(15)
        
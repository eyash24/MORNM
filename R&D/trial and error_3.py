import time
import plyer
from playsound import playsound


current_time()
print(type(tm_hour))

#notification
def notify_(title,message,timeout):
    global title_
    global message_
    global timeout_
    title_=title
    message_=message
    timeout_=int(timeout)
    if title == None :
        title_="Alert"
    else:
        title_=title

    if timeout == None:
        timeout_ = 5
    else:
        timeout_ = timeout

    plyer.notification.notify(title=title_, message=message_, timeout=timeout_)
    playsound('/Users/yashlucky/Downloads/ding-sound-effect/Ding-sound-effect.mp3')

notify_("Alert","This is my first notification",5)

from datetime import datetime


def sampleRespones(inputText):
    userMsg = str(inputText).lower()
    if userMsg in ('hi', 'hello', 'hey'):
        return "Hey! How's it going?"
    if userMsg in ("who are you?", "who are you"):
        return "I am TeamOpine bot!"
    if userMsg in ('time', 'time?', 'time!', 'date time!', 'datetime!', 'datetime', 'date time', 'date', 'date!', 'date?'):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M:%S")
        return dateTime
    return "i do not understand what are you saying!"

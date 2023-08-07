# Moviewflix 

_____ Ideas Todo _____

newuser.bat mit mehreren beispiel usern testen ?
forms.py am Ende für CustumUser - Video 15  Custom Admin Forms

____ Using rqworker _____


Aktuell --> rqworker -w rq_win.WindowsWorker

rqworker | nur um den Redis Worker zu starten

Nochmal lesen
___
python manage.py rqworker
python manage.py rqworker --worker-class rq_win.WindowsWorker default
___

git philosophie feature/email verification

## Setup

1. Collect static Files
    - Create env: ```python -m venv env```
    - ACtivateenv with: ```source env/bin/activate```
    - In ```settings.py``` define ```STATIC_ROOT```
    - Run ```python manage,py collectstatic```


__________________

Email Bestätigung via google mail machen 
Link in er Mail als Url endpoint auf def(in der views.py) activateModel isactive Field durch die funktion ändern()



____________________________

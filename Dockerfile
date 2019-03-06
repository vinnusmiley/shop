FROM python:2.7-onbuild

EXPOSE 5000

CMD gunicorn flaskk:app --logfile - --bind 0.0.0.0:5000

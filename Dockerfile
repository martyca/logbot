FROM python:alpine
COPY logbot.py mb.txt /app/
WORKDIR /app
ENTRYPOINT ["python", "logbot.py"]

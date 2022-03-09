FROM python:slim

COPY bot.py /app/
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
 
CMD ["python", "-u", "/app/bot.py"]


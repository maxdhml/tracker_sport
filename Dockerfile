FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# On force directement pip à utiliser le proxy pour cette ligne précise !
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]
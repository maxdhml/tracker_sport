FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# On force directement pip à utiliser le proxy pour cette ligne précise !
RUN pip install --proxy=http://cache-etu.univ-artois.fr:3128 -r requirements.txt

COPY . .

CMD ["python", "run.py"]
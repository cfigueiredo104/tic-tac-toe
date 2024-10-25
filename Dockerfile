# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requeriments.txt

COPY . .

CMD ["python", "tic-tac-toe.py"]
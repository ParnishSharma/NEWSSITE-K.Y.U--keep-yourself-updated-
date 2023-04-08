FROM python:3.9-slim

ENV API_KEY 9ad2852f515c4ab5b1446c632061b2d2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

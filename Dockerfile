FROM python:3.9-slim

ENV API_KEY 9ad2852f515c4ab5b1446c632061b2d2

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

COPY . .

EXPOSE 5000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]

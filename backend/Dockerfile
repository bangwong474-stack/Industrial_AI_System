FROM python:3.11.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libgomp1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","10000"]
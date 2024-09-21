FROM python:3.8.10
WORKDIR /app
COPY requirements.txt .
COPY ./src /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

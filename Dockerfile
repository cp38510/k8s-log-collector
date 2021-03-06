FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app
ENTRYPOINT [ "python", "app.py" ]

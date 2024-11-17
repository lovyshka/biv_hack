FROM pytorch/pytorch:latest

USER 0

WORKDIR /app

COPY model/* .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
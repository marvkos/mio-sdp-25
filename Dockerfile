FROM python:3.11.8-slim

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD /app /app

RUN ruff check app

CMD ["fastapi", "run", "app/main.py"]

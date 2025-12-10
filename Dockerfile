FROM python:3.11.8-slim

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD /app /app
ADD /tests /tests

RUN ruff check app
RUN python -m unittest discover tests -v

CMD ["fastapi", "run", "app/main.py"]

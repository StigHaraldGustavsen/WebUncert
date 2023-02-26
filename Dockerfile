FROM python:3.10.10-slim-buster
WORKDIR /app
COPY . /app
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install
EXPOSE 5000
CMD ["poetry", "run", "flask", "--app", "webuncert/app", "run", "--port=5000","--host=0.0.0.0"]

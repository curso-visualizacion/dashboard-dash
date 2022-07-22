FROM python:3.8
RUN curl -sSL https://install.python-poetry.org | python -
COPY ./pyproject.toml /app/pyproject.toml
COPY ./poetry.lock /app/poetry.lock
WORKDIR /app
RUN $HOME/.local/bin/poetry install
COPY . /app
EXPOSE 5000
CMD ["/root/.local/bin/poetry", "run", "python", "dashboard/app.py"]

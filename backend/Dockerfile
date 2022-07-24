# Docker 
# https://github.com/svx/poetry-fastapi-docker/blob/main/docker/Dockerfile

FROM python:3.9-slim-buster

WORKDIR /backend

# Install Poetry
RUN apt-get update -y
RUN apt-get install curl -y

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY . .

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# For development, to use jupyter kernel inside the container
# jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888
ARG INSTALL_JUPYTER=false
RUN bash -c "if [ $INSTALL_JUPYTER == 'true' ] ; then pip install jupyterlab ; fi"

# expose the port that uvicorn will run the app on
EXPOSE 5000

# execute the command python main.py (in the WORKDIR) to start the app
ENV PYTHONPATH=/app
CMD python3 -m app
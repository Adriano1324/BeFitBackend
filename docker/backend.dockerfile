FROM python:3.11

WORKDIR /app/

# Install Poetry
RUN pip install "poetry==1.4.1"

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ../pyproject.toml ../poetry.lock* /app/
RUN poetry config virtualenvs.create false
# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# For development, Jupyter remote kernel, Hydrogen
# Using inside the container:
# jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.custom_display_url=http://127.0.0.1:8888

COPY ./ /app
ENV PYTHONPATH=/app
FROM python:3.11-alpine
LABEL maintainer='mezamateoj@gmail.com'

ENV PYTHONUNBUFFERED=1 


COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8000


# create venv --this is optional 
# install requirements
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    # creates a user in the vm
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

# this swithces to this user
# so everthing will run from this user
USER django-user
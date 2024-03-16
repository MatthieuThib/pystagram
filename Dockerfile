# Use an official Python runtime as a parent image
FROM python:3.8-alpine

WORKDIR /app

COPY pystagram /app/pystagram
COPY pyproject.toml /app/pyproject.toml
COPY LICENSE /app/LICENSE
COPY README.rst /app/README.rst

# Install the library
RUN python -m pip install .

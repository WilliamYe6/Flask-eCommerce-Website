FROM python:3.8-slim-buster
ENV LISTEN_PORT=5000
EXPOSE 5000
RUN mkdir sneakerApp
WORKDIR /sneakerApp
COPY requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt
CMD ["python","run.py"]


# RUN python3 -m venv 
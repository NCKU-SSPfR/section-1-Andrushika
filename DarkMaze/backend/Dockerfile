# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

RUN groupadd -r myuser && useradd -r -g myuser myuser


WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

USER myuser

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload"]
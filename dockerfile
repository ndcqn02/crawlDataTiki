FROM python:3.7.13-slim-buster
COPY ./api
RUN pip install fastapi uvicorn pandas sqlalchemy==1.4.46 requests random
WORKDIR ./api
CMD ["uvicorn", "main:app_craw", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.7.13-slim-buster
COPY ./ /app/
RUN pip install --no-cache-dir -r app/requirements.txt
WORKDIR /app
CMD ["uvicorn", "main:app_craw", "--host", "0.0.0.0", "--port", "8000"]

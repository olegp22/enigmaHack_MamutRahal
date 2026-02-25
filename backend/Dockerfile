FROM python:3.11-slim

WORKDIR /app

COPY requrements.txt .

RUN pip install --no-cache-dir -r requrements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "programm_API.main:app", "--host", "0.0.0.0", "--port", "8000"]

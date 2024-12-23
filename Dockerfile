
FROM python:3.11-slim


WORKDIR /app


COPY servis.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
COPY . .

CMD ["python", "servis.py"]




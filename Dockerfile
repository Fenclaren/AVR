# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл сервера в контейнер
COPY servis.py .

# Указываем команду для запуска сервера
CMD ["python", "servis.py"]

# Экспонируем порт, который использует сервер
EXPOSE 8080
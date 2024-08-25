# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Создаем директории для статики и медиа
RUN mkdir -p /app/static /app/media

# Устанавливаем права доступа
RUN chown -R www-data:www-data /app/static /app/media

# Выполняем миграции и собираем статику при запуске контейнера
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn shop_project.wsgi:application --bind 0.0.0.0:8000"]
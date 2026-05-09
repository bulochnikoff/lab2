# Лабораторная работа №2: PostgreSQL и ORM

## Цель
Освоить SQLAlchemy, Alembic, создание моделей, миграций и CRUD операций.

## Технологии
- Python 3.12, Flask, SQLAlchemy, Alembic
- PostgreSQL 15
- Docker, Docker Compose

## Запуск
```bash
cd backend
docker compose up --build



API эндпоинты
Метод	                  URL	                             Описание
GET	                  /health	                       Проверка статуса
GET	                  /api/readings	               Список всех показаний
GET	                  /api/readings/<id>	         Получить одно показание
POST	                /api/readings	                 Добавить показание
PUT                 	/api/readings/<id>	            Обновить показание
DELETE	              /api/readings/<id>	            Удалить показание



Примеры запросов
Добавление показания
bash
curl -X POST http://localhost:5000/api/readings \
  -H "Content-Type: application/json" \
  -d '{"sensor_id":"sensor-001","value":23.5,"timestamp":"2026-05-09T12:00:00Z","lat":55.75,"lon":37.61}'


Получение всех показаний
bash
curl http://localhost:5000/api/readings



Обновление показания
bash
curl -X PUT http://localhost:5000/api/readings/1 \
  -H "Content-Type: application/json" \
  -d '{"value":24.0}'



Удаление показания
bash
curl -X DELETE http://localhost:5000/api/readings/1




Миграции Alembic
bash
# Генерация миграции
docker exec -it lab2_backend alembic revision --autogenerate -m "message"

# Применение миграции
docker exec -it lab2_backend alembic upgrade head

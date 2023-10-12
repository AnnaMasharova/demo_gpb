docker-compose up -d --build

# Вывести контейнеры с портами
docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a

# Вывести ip конкретного контейнера, например postgres
docker inspect \
  -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aqf "name=postgres")

# Проверить слушает ли бд порт 5432 
nc -zv 172.18.0.2 5432

# Получить логи postgres по id контейнера
docker logs $(docker ps -aqf "name=postgres")

# Зайти в базу, проверить таблицы \dt
psql -U gpbuworker -d accounts -h 172.18.0.2

# Остановить и удалить контейнеры
docker-compose -f docker-compose.yml down --remove-orphans
sudo rm -r postgres-data/

# Пример POST запроса в account
curl -0 -v -X POST http://127.0.0.1:80/account \
-H "Expect:" \
-H 'Content-Type: application/json; charset=utf-8' \
--data-binary @- << EOF
{ 
    "method": "create", 
    "data":{ 
        "account_id": "test_demo" 
    }, 
    "balance": "777" 
}
EOF

# Пример валидного ответа
{"result": "ok", "reason": "new_account_is_created"}


# Пример POST запроса в user
curl -0 -v -X POST http://127.0.0.1:80/user \
-H "Expect:" \
-H 'Content-Type: application/json; charset=utf-8' \
--data-binary @- << EOF
{ 
    "method": "create", 
    "data":{ 
        "name": "test_user_05.10", 
        "email": "demo@test.tu", 
        "password": "test_password" 
    }, 
    "balanse": "555" 
}
EOF

# Пример валидного ответа
{"result": "ok", "reason": "user is created: 11187529-95bd-4e33-81e8-22b746a87314"}
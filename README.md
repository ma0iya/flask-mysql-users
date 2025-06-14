# Flask + MySQL Dockerized App

## 📁 Структура

- `backend/`: Flask приложение
- `init.sql`: Създава таблица `users` и добавя данни
- `compose.yml`: Docker Compose конфигурация

## ▶️ Стартиране

```bash
docker compose up --build
```

След стартиране отворете:  
http://localhost:5000/

## 🔧 Компоненти

- **Flask**: Web сървър, който показва списък от потребители
- **MySQL**: Таблица с имена, заредена автоматично чрез init.sql
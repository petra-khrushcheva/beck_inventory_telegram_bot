![Workflow badge](https://github.com/petra-khrushcheva/beck_inventory_telegram_bot/actions/workflows/main.yml/badge.svg)

# Телеграм бот Тест Бека 📝

Этот бот дает возможность пройти тест Бека на определение уровня депрессии.  
Тест построен на основе FSM. В качестве хранилища состояний используется Redis.
***
### Технологии
Aiogram 3.4  
Redis
Pydantic 2.5    
Pydantic settings 2.2
***
### Установка
- Создайте бота через [@BotFather](https://t.me/botfather) по [инструкции](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).
- Добавьте описание и команды для своего бота из файла [bot_texts.txt](https://github.com/petra-khrushcheva/beck_inventory_telegram_bot/blob/main/bot_texts.txt).
- Клонируйте проект:
```
git clone git@github.com:petra-khrushcheva/beck_inventory_telegram_bot.git
``` 
- Перейдите в директорию beck_inventory_telegram_bot:
```
cd beck_inventory_telegram_bot
``` 
- Cоздайте переменные окружения по [образцу](https://github.com/petra-khrushcheva/beck_inventory_telegram_bot/blob/main/.env.example).
- Запустите Docker-compose:
```
docker compose -f docker-compose-dev.yml up
``` 
Готово! 📝 
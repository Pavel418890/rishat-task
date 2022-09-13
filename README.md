# Rishat Task
https://rishat-task.herokuapp.com/item/1

# Запуск локально
```shell
docker build -t rishat_task .
docker run -d \
--name=rishat_task \
-p=8000:8000 \
-e SECRET_KEY=yoursecretkey \
-e STRIPE_PRIVATE_KEY=sk_test_your_private_stripe_key \
-e CLIENT_BASE_URL=http://localhost:8000 \
-e DJANGO_SETTINGS_MODULE=apps.config.settings \
-e ALLOWED_HOSTS=".localhost;" \
-e PORT=8000 \
rishat_task:latest
```
# Деплой в heroku
Реализован CI/CD github flow с запуском линтеров и тестов c автоматическим
деплоем в heroku после commit в `master` ветку.




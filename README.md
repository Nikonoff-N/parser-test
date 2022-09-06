# Тестовое задание для Backend-разработчика от компании POPSO

Состоит из 3 частей

1.  Парсер // Спарсить первые 10 новостей со следующих ресурсов, проставить тэги (ozon, yandex).

Спарсить новости с yandex удалось легко через запрос по api с помощью httpx. Текст новости был запарсен через bs4. 
Новости с озона были по защитой cloudflare обойти удалось только через selenium.

2. Админка // Сделать на Django админку для новостей с шаблоном Admin LTE 3 и занести данные из парсера в базу MySQL.

Была сделана простая админка на джанго, занесены полученные новости

3. API // Сделать простой API запрос для frontend на получение структурированных новостей в формате JSON

Создал апи с точками для получения всех данных, данных по дате и по тегу, списка всех тегов.

Инструкции по использованию

1. Установить зависимости выполнив pip install -r requirements.txt
2. Изменить настройки базы данных джанго в файле settings.py
Пример:

DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'parser',
        
        'USER': 'root',
        
        'PASSWORD': 'admin',
        
        'HOST': 'localhost',
        
        'PORT': 3306,
        
    }
    
}

3. Произведите миграции выполнив python manage.py migrate

4. Спарсите новости python manage.py parseNews

5. Запустите сервер python manage.py runserver

6. По адресу http://127.0.0.1:8000/ доступен просмотр записей

7. По адрессу http://127.0.0.1:8000/admin - админка 

для доступа нужна учётная запись, её можно создать ,выполнив python manage.py createsuperuser

8. По адресу http://127.0.0.1:8000/swagger - документация к API
 

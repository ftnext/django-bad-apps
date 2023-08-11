# SQLインジェクションできてしまう Bad Django App

## 環境構築

```sh
% # pwdは sql-injection
% python3.11 -m venv venv --upgrade-deps
% source venv/bin/activate
% pip install -r requirements.lock
```

## アプリケーションを動かす

`vim bad_sql_injection/.env`

```
DEBUG=True
SECRET_KEY=' django.core.management.utils.get_random_secret_key を使って生成した値に置き換える '
DATABASE_URL=postgres://developer:mysecretpassword@127.0.0.1:5432/badapp
```

別ターミナル

```sh
% # pwdは sql-injection
% docker compose up -d
```

元のターミナル

```sh
% cd bad_sql_injection
% python manage.py migrate
% python manage.py loaddata dump_todos.json
% python manage.py runserver
```

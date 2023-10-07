# SQLインジェクションできてしまう Bad Django App

## [推奨] docker composeで動かす

カレントディレクトリは sql-injection

`vim bad_sql_injection/.env`

```
DEBUG=True
SECRET_KEY=' django.core.management.utils.get_random_secret_key を使って生成した値に置き換える '
DATABASE_URL=postgres://developer:mysecretpassword@db/badapp
```

Then run `docker compose up -d` （dbもwebも起動）

Go http://127.0.0.1:8000/todolist/

データ投入は `docker compose run web python manage.py loaddata dump_todos.json`

## 開発時の環境構築

```sh
% # pwdは sql-injection
% python3.11 -m venv venv --upgrade-deps
% source venv/bin/activate
% pip install -r requirements.lock
```

### アプリケーションを動かす

`vim bad_sql_injection/.env`

```diff
-DATABASE_URL=postgres://developer:mysecretpassword@db/badapp
+DATABASE_URL=postgres://developer:mysecretpassword@127.0.0.1:5432/badapp
```

docker-compose.ymlのservicesのwebをコメントアウト（dbだけを動かす）

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

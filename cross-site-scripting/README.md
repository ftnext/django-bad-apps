# XSSできてしまう Bad Django App

## [推奨] docker composeで動かす

カレントディレクトリは cross-site-scripting

`vim bad_xss/.env`

```
DEBUG=True
SECRET_KEY=' django.core.management.utils.get_random_secret_key を使って生成した値に置き換える '
DATABASE_URL=postgres://developer:mysecretpassword@db/badapp
```

Then run `docker compose up -d` （db・web・evil-server起動）

- JavaScriptコードが実行されるページ（`HttpResponse`で返している）
  - http://127.0.0.1:8000/example/
- 持続型XSS
  - http://127.0.0.1:8000/todolist/

ユーザ作成は `docker compose run web python manage.py createsuperuser --username wasbook --email wasbook@example.com`  
（superuserの権限は必須ではありませんが、コマンド一発で作れるので採用しています）

## 開発時の環境構築

```sh
% # pwdは cross-site-scripting
% python3.11 -m venv venv --upgrade-deps
% source venv/bin/activate
% pip install -r requirements.lock
```

### アプリケーションを動かす

`vim bad_xss/.env`

```diff
-DATABASE_URL=postgres://developer:mysecretpassword@db/badapp
+DATABASE_URL=postgres://developer:mysecretpassword@127.0.0.1:5432/badapp
```

docker-compose.ymlのservicesのwebをコメントアウト（dbとevil-serverを動かす）

別ターミナル

```sh
% # pwdは cross-site-scripting
% docker compose up -d
```

元のターミナル

```sh
% cd bad_xss
% python manage.py migrate
% python manage.py runserver
```

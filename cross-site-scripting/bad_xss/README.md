# XSSできてしまう Bad Django App （作成中）

## 環境構築

```sh
% # pwdは cross-site-scripting
% python3.11 -m venv venv --upgrade-deps
% source venv/bin/activate
% pip install -r requirements.lock
```

## アプリケーションを動かす

`vim bad_xss/.env`

```
DEBUG=True
SECRET_KEY=' django.core.management.utils.get_random_secret_key を使って生成した値に置き換える '
```

```sh
% cd bad_xss
% python manage.py runserver
```

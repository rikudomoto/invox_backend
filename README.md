# invox_backend

### 主な使用フレームワーク

- [Flask]
- [SQLAlchemy]

### docker コンテナ立ち上げ

db

```
docker-compose build db
docker-compose up -d db
```

api

```
docker-compose build api
docker-compose up -d api
```

### db migration

```
docker-compose exec api bash
flask db init
flask db migrate
flask db upgrade
```

### 動作確認

リクエスト成功

```
curl --location 'http://0.0.0.0:5001/input_ai' \
--header 'Content-Type: application/json' \
--data '{
    "path": "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"
}'
```

リクエスト失敗

```
curl --location 'http://0.0.0.0:5001/input_ai' \
--header 'Content-Type: application/json' \
--data '{
    "path": ""
}'
```

mysql ログイン

```
docker-compose exec db mysql -u root -p
use invox_db;
select * from  ai_analysis_log;
```

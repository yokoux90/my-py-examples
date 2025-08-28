## 1. Initialize 

```sh
uv sync
```

## 2. Docker

```sh
docker compose up -d
```

## 3. Celery

```sh
celery -A tasks worker -P solo --loglevel=INFO
```

## 4. FastAPI

```sh
fastapi dev main.py
```

## 5. [OpenAPI](http://127.0.0.1:8000/docs)


-----

## Skill Tips 

> Format Code

```shell
black .
```

> Type Check

```shell
mypy .
```
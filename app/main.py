from fastapi import FastAPI
from decouple import config
from tortoise.contrib.fastapi import register_tortoise
from app.models.user import User, UserProfile

app = FastAPI()


@app.get("/")
def users() -> dict:
    return {"Message": "Test Users"}


try:
    username = config("DB_USERNAME")
    password = config("DB_PASSWORD")
    database_name = config("DB_NAME")

    register_tortoise(
        app,
        db_url=f"postgres://{username}:{password}@localhost:5432/{database_name}",
        modules={
            "models": [
                "app.models.user",
            ]
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )


except Exception as e:
    print(f"Error initializing Tortoise ORM: {e}")
    raise e

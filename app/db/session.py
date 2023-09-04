from decouple import config
from tortoise import Tortoise, fields
from tortoise.models import Model


username = config("DB_USERNAME")
password = config("DB_PASSWORD")
database_name = config("DB_NAME")


async def init_db():
    await Tortoise.init(
        db_url=f"postgres://{username}:{password}@localhost:5432/{database_name}",
        modules={"models": ["your_module_name"]},
    )
    await Tortoise.generate_schemas()

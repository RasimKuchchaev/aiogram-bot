from typing import Union
import asyncpg
from aiohttp.web_routedef import static
from asyncpg import Pool, Connection

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool =await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,      # fetch выгружает все
                      fetchval: bool = False,   # fetchval выгружает 1 значение
                      fetchrow: bool = False,   # fetchrow выгружает 1 строку
                      execute: bool = False,    # выполнить команду
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result
    async def create_table_user(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(255) NOT NULL,
        user_name VARCHAR(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters:dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, fullname, username, telegram_id):
        sql = "INSERT INTO Users (fullname, username, telegram_id) VALUES($1, $2, $3)"
        return await self.execute(sql,fullname,username,telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = " SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = " UPDATE User SET username =$1 WHERE telegram_id =$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_user(self):
        await self.execute("DELETE FROM User WHERE TRUE", execute=True)

    async def drop_user(self):
        await self.execute("DROP TABLE Users", execute=True)


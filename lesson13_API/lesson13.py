import asyncio
import random

import aiohttp

MAX_POKEMON = 100
SIZE = 1
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


async def get_pokemon_async(id_: str) -> str:
    url = BASE_URL + id_

    async with aiohttp.ClientSession.get(url) as session:
        return session.json()["name"]


async def get_random_pokemon_async() -> str:
    random_id = get_random_id()
    return await get_pokemon_async(random_id)


async def async_main():
    tasks = [get_random_pokemon_async() for _ in range(SIZE)]
    random_pokemons = await asyncio.gather(*tasks)
    print(f"Pokemons: {random_pokemons}")


asyncio.run(async_main())

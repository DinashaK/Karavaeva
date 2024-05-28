# Реализуйте простой HTTP-клиент. Он принимает один параметр командной строки - URL. Клиент делает запрос по указанному URL и выдает тело ответа на терминал как текст.
import asyncio
import sys
import aiohttp

async def async_simple_http_client(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    print("Response Body:")
                    print(await response.text())
                else:
                    print(f"Failed to fetch URL: {response.status}")
    except aiohttp.ClientError as e:
        print(f"Error fetching URL: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python http_client.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    asyncio.run(async_simple_http_client(url))
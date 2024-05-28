# Напишите простой многопоточный загрузчик URL. Список URL скрипт принимает как аргументы командной строки.
import concurrent.futures
import requests
import sys

def load_url(url):
    try:
        response = requests.get(url)
        print(f"Loaded {url} with status code {response.status_code}")
    except Exception as e:
        print(f"Error loading {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python downloader.py url1 url2 url3 ...")
        sys.exit(1)

    urls = sys.argv[1:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(load_url, urls)

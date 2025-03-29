import requests


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url

# yield se 'duerme' después de entregar un resultado,
# y el for que lo llama lo 'despierta' para pedir el siguiente

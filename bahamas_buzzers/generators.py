import requests
from url_utils import gen_from_urls

# Iterable using List
for i in [x*3 for x in [1, 2, 3, 4, 5]]:
    print(i)
print()

# Iterable using generator '(...)'
for i in [x*3 for x in [1, 2, 3, 4, 5]]:
    print(i)
print()

#
# request example
#
urls = ('https://headfirstlabs.com',
        'http://oreilly.com', 'http://twitter.com')

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)


print('Using gen_from_urls...')
new_urls = tuple(list(urls) + ['http://talkpython.fm',
                 'http://pythonpodcast.com', 'http://python.org'])
print(f'{new_urls=}')

for resp_len, status, url in gen_from_urls(new_urls):
    print(resp_len, '->', status, '->', url)

import urllib.request, json
url = 'https://api.github.com/users/meth04/repos?sort=updated&per_page=100'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = json.loads(urllib.request.urlopen(req).read())
with open('repos.txt', 'w', encoding='utf-8') as f:
    for r in res:
        desc = r.get('description') or ''
        lang = r.get('language') or ''
        stars = r.get('stargazers_count', 0)
        f.write(f"{r['name']}: {desc} ({lang}) - ★{stars}\n")

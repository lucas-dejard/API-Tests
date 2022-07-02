from httpx import get, post, patch, delete


url_base = 'http://localhost:5000/todos/api/tasks'

request = get(url_base)

assert request.status_code == 200, 'codigo de resposta diferente de 200'
assert request.json() == [], 'vish'

# request = delete(url_base + '/1')
# assert request.status_code == 204, 'huuuuum'


import ipdb
from httpx import get, post, patch, delete

url_base = 'http://localhost:5000/todos/api/tasks'


not_task = {'titulo': 'tomar pingos!'}
bad_task = {'title': 'Tomar pinga!'}
god_task = {'title': 'Tomar pinga!', 'description': 'Pq e bom', 'done': False}

# ipdb.set_trace()

class Test_Primario:

    def test_returona_200_um_get(self):
        """
        garantir que quando fizer o primiero request não pode ter registro /tasks
        """
        request = get(url_base)
        assert request.status_code == 200



    def test_lista_volta_vazia(self):
        """
        garantir que quando fizer o primiero request não pode ter registro /tasks
        """
        request = get(url_base)
        assert (request.json()) == []



# request = post(url_base, json=not_task)
# assert request.status_code == 400, 'codigo de resposta diferente de 400'
#
# request = post(url_base, json=bad_task)
# assert request.status_code == 400, 'codigo de resposta diferente de 400'
#
# request = post(url_base, json=god_task)
# assert request.status_code == 201, 'codigo de resposta diferente de 201'
#
# request = delete(url_base + '/19')
# assert request.status_code == 204

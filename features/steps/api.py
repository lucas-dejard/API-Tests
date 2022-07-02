from httpx import get, post
from behave import then, when, given

url_base = 'http://localhost:5000/todos/api/tasks'

@given('que exista uma tarefa')
def inserir_tarefa(context):
    feature_table = context.table[0]
    tarefa = {}
    tarefa['title'] = feature_table['nome']
    tarefa['description'] = feature_table['descrição']
    tarefa['state'] = feature_table['estado']
    assert post(url_base, json=tarefa).status_code == 201

@when('verificar minhas tarefas em "{endpoint}"')
def pegando_minhas_tarefas(context, endpoint):
    context.request = get(url_base)

@then('não devo ter tarefas para fazer')
def checando_se_não_tem_tarefa(context):
    context.request.json() == []

@then('devo ter a sguinte tarefa para fazer')
def checar_se_tarefa_esta_para_ser_feita(context):
    feature_table = context.table[0]
    tarefa = {}
    tarefa['title'] = feature_table['nome']
    tarefa['description'] = feature_table['descrição']
    tarefa['state'] = feature_table['estado']
    assert context.requestjson() == []

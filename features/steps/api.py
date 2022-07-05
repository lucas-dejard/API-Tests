from httpx import get, post
from behave import then, when, given
from json import load
from ast import literal_eval


@given('que exista uma tarefa')
def inserir_tarefa(context):
    feature_table = context.table[0]
    tarefa = {}
    tarefa['tittle'] = feature_table['nome']
    tarefa['description'] = feature_table['descrição']
    tarefa['done'] = feature_table['estado']

    assert post(context.base_url, json=tarefa).status_code == 201

@when('verificar minhas tarefas em "{endpoint}"')
def pegando_minhas_tarefas(context, endpoint):
    context.request = get(context.base_url)

@then('não devo ter tarefas para fazer')
def checando_se_nao_tem_tarefa(context):
    assert context.request.json() == []

@then('devo ter a seguinte tarefa para fazer')
def checar_se_tarefa_esta_para_ser_feita(context):
    feature_table = context.table[0]
    tarefa = {}
    tarefa['tittle'] = feature_table['nome']
    tarefa['description'] = feature_table['descrição']
    tarefa['done'] = literal_eval(feature_table['estado'])
    response = context.request.json()
    del response[0]['id']

    assert tarefa in response, f'{response} {tarefa}'

# language:pt

Funcionalidade:

  """
  Seja eu uma pessoa interessante
  Quero saber quais tarefas tenho
  """
  Cenário: No primeiro uso do sistema, não existem tarefas registradas
    Dado que exista uma tarefa
      |nome|descrição|estado|
      |toma pinga|pq é bom|false|
    Quando verificar minhas tarefas em "/tasks"
    Então não devo ter tarefas para fazer

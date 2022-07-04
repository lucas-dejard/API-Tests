# language:pt

Funcionalidade: Saber as tarefas que tenho a realizar

  """
  Seja eu uma pessoa interessante
  Quero saber quais tarefas tenho
  """
  Cenário: No primeiro uso do sistema, não existem tarefas registradas
    Quando verificar minhas tarefas em "/tasks"
    Então não devo ter tarefas para fazer

  Cenário: ver tasks registradas
    Dado que exista uma tarefa
      |nome|descrição|estado|
      |toma pinga|pq é bom|False|
    Quando verificar minhas tarefas em "/tasks"
    Então devo ter a seguinte tarefa para fazer
      |nome|descrição|estado|
      |toma pinga|pq é bom|False|
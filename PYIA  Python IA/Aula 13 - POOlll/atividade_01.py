# Desenvolva um aplicativo de gerenciamento de tarefas em python. Crie duas classes, Tarefa e Projeto, com uma associação unidirecional. Permita que as tarefas sejam associadas a projetos e que você possa listar as tarefas de um projeto em particular.

class Tarefa:
    def __init__(self, nome, descricao, situacao='Indefinida'):
        self.nome = nome
        self.descricao = descricao
        self.situacao = situacao

    def marcar_concluida(self, concluida):
        self.concluida = concluida
        self.situacao = 'Concluida'
        if concluida:
            print('Sua tarefa foi conluída!')
        else:
            print('Sua tarefa está pendente!')


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(f'- {tarefa.nome}: {tarefa.descricao} ({tarefa.situacao})')


nome = str(input('Digite seu nome: '))
descricao =str(input('Tipo de Tarefa: '))
situacao = str(input('Você concluiu a tarefa? '))
situacao.lower()
if situacao == 'sim':
    print('Sua tarefa foi concluída!')
else:
    print('Sua tarefa não foi concluída')

tarefa = Tarefa(nome,descricao,situacao)
projeto = Projeto('Treinar')

tarefa1 = Tarefa('Treinar', 'Bíceps e costas', situacao='Pendente')
projeto = Projeto('Projeto Verão')
projeto.adicionar_tarefa(tarefa)
projeto.listar_tarefas()



        

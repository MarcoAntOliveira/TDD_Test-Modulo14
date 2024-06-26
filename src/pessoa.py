import requests # type: ignore

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False
    def obter_todos_os_dados(self):
        resposta = requests.get('https://jsonplaceholder.typicode.com/users/1')
        if resposta.ok:
            self.dados_obtidos = True
            return  'CONECTADO'
        else:
            return 'ERRO 404'
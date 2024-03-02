from model import Pessoa

#acesso bando de dados
class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoas.txt", "r") as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
    
    @classmethod
    def ler(cls):
        nome = "Rodrigo"
        idade = 34
        cpf = "12345678910"
        return Pessoa(nome, idade, cpf)
    

    p1 = Pessoa("Rodrigo", 34, "08549892777")
    print(p1)
from datetime import datetime

class Jogo:

    def __init__(self,cod,nome,genero,descricao):
        self._cod = cod
        self._nome = nome
        #self._lancamento = datetime.strptime(lancamento, '%d/%m/%Y').date()
        self._genero = genero
        self._descricao = descricao
        
    
    def _get_nome(self):
        return self._nome

    def _get_lancamento(self):
        return self._lancamento

    def _get_genero(self):
        return self._genero
    
    def _get_cod(self):
        return self._cod

    def _get_descricao(self):
        return self._descricao

    def _set_nome(self, nome):
        self._nome = nome
 
    def _set_lancamento(self, lancamento):
        self._lancamento = lancamento

    def _set_genero(self, genero):
        self._genero = genero
    
    def _set_cod(self, cod):
        self._cod = cod
    
    def _set_descricao(self, descricao):
        self._descricao = descricao
    
    nome = property(_get_nome,_set_nome)
    genero = property(_get_genero,_set_genero)
    lancamento = property(_get_lancamento,_set_lancamento)
    cod = property(_get_cod,_set_cod)
    descricao= property(_get_descricao,_set_descricao)
    
    def __str__(self):
        return "{},{},{},{},{}".format(self._cod,self._nome,self._genero,self._lancamento,self._descricao)







class jogoDAO:
  
    def _inserir (self,jogo):
        arquivo = open('jogos.txt', 'a')
        arquivo.write(jogo.__str__()+"\n")
        arquivo.close()

    def _listar(self):
        arquivo = open('jogos.txt','r')
        texto = arquivo.readlines()
        for linha in texto :
            print(linha)
        arquivo.close()

"""
    def _excluir(self,cod):
        arquivo = open('jogos.txt','r+')
        #texto = arquivo.readlines()
        for linha in arquivo:
            linha1=linha.split(",")
            print(linha)
            if (linha1[0]==cod):
                #linha.replace(linha, "")
                
                
        #for linha in texto :
            #frase = texto.split(",")

            #for codigo in frase[0]: 
                #if codigo==cod: 
                    #linha="" 

        arquivo.close()
"""






def jogar(): 
    menu=0
    while menu!=2:

        menu=int(input("Menu: \n \n O que gostaria de fazer? \n \n 1 - adicionar um jogo \n 2 - Sair \n"))

        if menu==1:
            cod = int(input('Digite o ID do jogo: '))
            nome = input('Nome do jogo: ')
            l = input('Digite a data de lançamento: ')
            genero = input('Categoria do Jogo: ')
            descricao = input('Insira a descrição: ')
            lanc=datetime.strptime(l, '%d/%m/%Y').date()
            jogo = Jogo(cod,nome,genero,descricao)
            jogo.lancamento = lanc
            novoJogo=jogoDAO()
            novoJogo._inserir(jogo.__str__())
            




jogar()
#novoJogo._listar()
#novoJogo._excluir("1")





import random


class Gene(object):
    def __init__(self,vR):
        self.gene = vR
        self.fitness = 0

    def parte_inferior(self,indice):
        parte = self.gene[0:indice]
        return parte

    def parte_superior(self,indice):
        final = len(self.gene)
        parte = self.gene[indice:final]
        return parte

    def corrigir_gene(self,i,valor):
        self.gene[i]= valor

    def get_gene(self):
        return self.gene

    def mutacao(self,taxa_mutacao,i):
        if(random.random()*100<=taxa_mutacao):
            self.gene[i]= int(random.choice([0,1,2,3]))
    def score(self,listaReq,qRel):
        p=qRel
        x=0
        score = 0
        for i in self.gene:
            if(i==0):
                y=0
            else:
                y=1
            a = listaReq[x].importancia * (p-i+1)*y
            b = listaReq[x].risco * i *y
            score = score + a-b
            x=x+1
        self.fitness = score

    def fitness(self):
        return self.fitness

    def __str__(self):
        string ="|"
        for cromossomo in self.gene:
            string = string + str(cromossomo) + "|"
        return string


class Realise:
    def __init__(self,number,custo_max):
        self.number = number
        self.releases = []
        self.custoAtual = 0
        self.cutosmax = custo_max

    def Veri_cheia(self,custo_cromossomo):
        if(self.cutosmax >= custo_cromossomo + self.custoAtual):
            return True
        else:
            return False
    def add_custo(self,custo_cromossomo):
        self.custoAtual = self.custoAtual + custo_cromossomo
    def zerar_custo(self):
        self.custoAtual = 0
    def get_customax(self):
        return self.cutosmax

class Requisito:
    def __init__(self, number, custo, risco,importancia):
        self.number = number
        self.custo = custo
        self.risco = risco
        self.importancia = importancia

    def risco(self):
        return self.risco

    def importancia(self):
        return self.importancia

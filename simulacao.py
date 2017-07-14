#!/usr/bin/env python
import os
import rows

class Documento(object):
    def __init__(self, documento_nome):
        self.doc = rows.import_from_xls(documento_nome)
    
    def retornaDoc(self):
        return self.doc
    
    def mostraTipos(self):
        x = self.retornaDoc()
        for row in x.fields.items():
            print(row)
            
class Coeficiente(object):
    def __init__(self):
        self.nf = 0 # somatorio de nota*cargahoraria
        self.chs = 0 # somatorio de carga horaria
        self.notas_pesadas = [ ] # nota de cada materia já pesada: nota * carga
        self.cr = 0 # coeficiente final

    def registro(self, Documento):
        """
        Abre o documento e lê todas as linhas, fazendo:
        1) Salva todas as notas pesadas, ou seja: nota * media
        2) Salva o somatorio de todas as cargas horarias
        """

        x = Documento.doc

        for item in x:
            if item.cht_3 is not None and item.media is not None:
                self.notas_pesadas.append(item.media*item.cht_3)
                self.chs += item.cht_3
            else:
                continue

    def insere_materia(self, Materia):
        self.notas_pesadas.append(Materia.media * Materia.carga)
        self.chs += Materia.carga

    def soma_notas(self):
        for item in self.notas_pesadas:
            self.nf += item
        

    def calcula_cr(self, Documento):
        self.registro(Documento)
        self.soma_notas()

        self.cr = ( (self.nf) / (10 * self.chs))

class Materia(object):
    def __init__(self, media=0, carga=0):
        self.media = media
        self.carga = carga
   
def main():
    # Assume existência do documento
    notas = Documento('documento.xls')
    coeficiente = Coeficiente()
    
    # Para inserir nova matéria:
    nova = Materia(8, 90)
    coeficiente.insere_materia(nova)

    # Para calcular coeficiente:
    coeficiente.calcula_cr(notas)

    print(coeficiente.cr)

if __name__ == '__main__':
    main()

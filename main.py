#!/usr/bin/env python

import src.documento as d
import src.materia as m
import src.coeficiente as c

nome_arquivo = "notas.xls"

def main(): # faça o tem que ser feito aqui
    notas = d.Documento("arquivos/{}".format(nome_arquivo))

    cr = c.Coeficiente()
    cr.inserir_materia(m.Materia(9, 10))
    cr.gerar_coeficiente(notas)

    print(cr.retorna_coeficiente())

if __name__ == '__main__':
    main()

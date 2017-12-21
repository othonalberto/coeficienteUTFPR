#!/usr/bin/env python

import documento as d
import materia as m
import coeficiente as c

def main(): # faça o tem que ser feito aqui
    cr = c.Coeficiente()
    cr.inserir_materia(m.Materia(9, 10))
    cr.gerar_coeficiente()

    print(cr.retorna_coeficiente())

if __name__ == '__main__':
    main()

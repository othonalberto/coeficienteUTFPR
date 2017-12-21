import pytest
import sys

sys.path.append('../')
import coeficiente as c 
import materia as m 
import documento as d


def test_init():
    obj = c.Coeficiente()

    assert obj.horas == 0
    assert obj.coeficiente == 0
    assert obj.notasVezesHoras == []

    return obj


def test_registrar_doc():
    obj = test_init()
    doc = d.Documento("document.xls")
    doc.abre_doc()

    obj.registrar_doc(doc)

    assert obj.horas == 150
    assert obj.notasVezesHoras[0] == 801


def test_inserir_materia():
    subj = m.Materia(10, 5)

    obj = test_init()

    obj.inserir_materia(subj)

    assert obj.horas == 5
    assert obj.coeficiente == 0
    assert obj.notasVezesHoras[0] == 50


def test_retorna_coeficiente():
    obj = c.Coeficiente() 

    assert obj.coeficiente == obj.retorna_coeficiente()

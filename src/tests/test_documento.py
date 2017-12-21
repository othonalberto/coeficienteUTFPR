import pytest
import sys
import rows

sys.path.append('../')
import documento as d


def test_init():
    obj = d.Documento("document.xls")

    assert obj.doc_tipo == "xls"
    assert obj.doc_nome == "document"
    assert obj.doc == "document.xls"


def test_retorna_doc():
    obj = d.Documento("document.xls")

    assert obj.doc == obj.retorna_doc()


def test_define_tipo():
    obj = d.Documento("document.xls")

    obj.define_tipo("document.xls")

    assert obj.doc_tipo == "xls"


def test_abre_doc():
    obj = d.Documento("document.xls")

    obj.abre_doc()

    assert isinstance(
            rows.import_from_xls(obj.doc_nome + '.' + obj.doc_tipo), type(obj.doc) )

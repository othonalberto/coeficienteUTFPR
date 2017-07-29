import pytest
import sys
import rows

sys.path.append('../')
import document as d

def test_init():
    obj = d.Document("document.xls")

    assert obj.doc_type == "xls"
    assert obj.doc_name == "document"
    assert obj.doc == "document.xls"


def test_get_doc():
    obj = d.Document("document.xls")

    assert obj.doc == obj.get_doc()


# def test_show_doc_field():

def test_define_type():
    obj = d.Document("document.xls")

    obj.define_type("document.xls")

    assert obj.doc_type == "xls"

def test_open_doc():
    obj = d.Document("document.xls")
    
    obj.open_doc()

    assert type(obj.doc) == type(
            rows.import_from_xls(obj.doc_name + '.' + obj.doc_type))

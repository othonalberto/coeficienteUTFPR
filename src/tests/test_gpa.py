import pytest
import sys

sys.path.append('../')
import gpa
import subject
import document as d


def test_create():
    obj = gpa.Gpa()

    assert obj.hours == 0
    assert obj.gpa == 0
    assert obj.gradesTimesHours == []

    return obj


def test_register():
    obj = test_create()
    doc = d.Document("document.xls")
    doc.open_doc()

    obj.register(doc)

    assert obj.hours == 150
    assert obj.gradesTimesHours[0] == 801


def test_insert_subject():
    subj = subject.Subject(10, 5)

    obj = test_create()

    obj.insert_subject(subj)

    assert obj.hours == 5
    assert obj.gpa == 0
    assert obj.gradesTimesHours[0] == 50


def test_get_gpa():
    obj = gpa.Gpa()

    assert obj.gpa == obj.get_gpa()

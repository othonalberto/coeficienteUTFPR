import pytest
import sys

sys.path.append('../')
import subject


def test_create():
    obj = subject.Subject(10, 5)

    assert obj.grade == 10
    assert obj.hours == 5

    return obj


def test_set_grade():
    obj = test_create()

    obj.set_grade(8)

    assert obj.grade == 8


def test_set_hours():
    obj = test_create()

    obj.set_hours(20)

    assert obj.hours == 20


def test_get_grade():
    obj = test_create()

    assert obj.grade == obj.get_grade()


def test_get_hours():
    obj = test_create()

    assert obj.hours == obj.get_hours()

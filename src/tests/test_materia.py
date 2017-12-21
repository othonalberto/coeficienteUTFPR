import pytest
import sys

sys.path.append('../')
import materia as m


def test_init():
    obj = m.Materia(10, 5)

    assert obj.nota == 10
    assert obj.horas == 5

    return obj


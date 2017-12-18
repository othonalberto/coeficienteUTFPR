#!/usr/bin/env python


class Materia(object):
    def __init__(self, nota=0, horas=0):
        if horas <= 0:
            raise Exception(
                    "Não é possível uma matéria ter {} horas." .format(hours)
            )

        if nota < 0 or nota> 10:
            raise Exception("Não é possível tirar {}." .format(grade))

        self.nota = nota
        self.horas = horas

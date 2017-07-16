#!/usr/bin/env python

import os
import rows
import document
import subject

class Gpa(object):
    def __init__(self):
        self.hours = 0
        self.gradesTimesHours = [ ]
        self.gpa = 0

    def register(self, Document):
        x = Document.doc

        for item in x:
            if item.cht_3 is not None and item.media is not None:
                self.gradesTimesHours.append(item.media*item.cht_3)
                self.hours += item.cht_3

    def new_subject(self, Subject):
        self.gradesTimesHours.append(Subject.grade * Subject.hours)
        self.hours += Subject.hours

    def set_gpa(self, Document=None):
        if Document is not None:
            Document.open_doc()
            self.register(Document)

        self.gpa = (sum(self.gradesTimesHours) / (10*self.hours))

    def get_gpa(self):
        return self.gpa

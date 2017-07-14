import rows

class Subject(object):
    def __init__(self, grade=0, hours=0):
        self.grade = grade
        self.hours = hours

    def set_grade(self, grade):
        self.grade = grade
    
    def set_hours(self, hours):
        self.hours = hours

    def get_grade(self):
        return self.grade

    def get_hours(self):
        return self.hours

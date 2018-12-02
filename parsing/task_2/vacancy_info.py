class VacancyInfo:
    def __init__(self, title, salary, requirements):
        self.title = title
        self.salary = salary
        self.requirements = requirements

    def __str__(self):
        s = 'title: %s\nsalary : %s\nТребования:\n' % (self.title, self.salary)
        for req in self.requirements:
            s += '- ' + req + '\n'
        return s

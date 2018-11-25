class Entry:
    def __init__(self, day, time, subject, teacher):
        self.time = time
        self.day = day
        self.subject = subject
        self.teacher = teacher

    def __str__(self):
        return self.day + " " + self.time +\
               " " + self.subject + "" + self.teacher

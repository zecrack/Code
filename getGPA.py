class StudentGPA:
    def __init__(self, name, num, credits, qpoints):
        self.name = name
        self.num = num
        self.credits = float(credits)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name, self.num

    def getCredits(self):
        return self.credits

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.credits

def makeStudent(infoStr):
        name, num, credits, qpoints = infoStr.split(" ")
        return StudentGPA(name, num, credits, qpoints)

filename = input("Enter name the grade file:")
infile = open(filename, 'r')
best = makeStudent(infile.readline())
for line in infile:
    s = makeStudent(line)
    if s.gpa() > best.gpa():
        best = s
infile.close()
print("the best student:",best.getName())
print("Credits",best.getQPoints())
print("GPA",best.gpa())
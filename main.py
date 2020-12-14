class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self):
        return self.address

    def toString(self):
        return f'Name: {self.name} \nAddress: {self.address}'


class Student(Person):
    def __init__(self, name: str, address: str):
        Person.__init__(self, name, address)
        self.courseGrade = {}
        self.totalGrade = 0
        self.numCourse = 0

    def toString(self):
        return f'{Person.toString(self)}'

    def aCourseGrade(self, course: str, grade: int):
        self.course = course
        self.grade = grade
        self.courseGrade.update({course: grade})
        self.numCourse = len(self.courseGrade)

    def aCourseGrade(self, course: str, grade: int):
        self.course = course
        self.grade = grade
        self.courseGrade.update({course: grade})
        self.numCourse = len(self.courseGrade)

    def printGrade(self):
        for i in self.courseGrade:
            print(f'{i}: {self.courseGrade[i]}')

    def getAvgGrade(self):
        for i in self.courseGrade.values():
            self.totalGrade += i
        self.avgGrade = self.totalGrade / len(self.courseGrade)
        return self.avgGrade

    def getNumCourse(self):
        return self.numCourse


class Teacher(Person):
    def __init__(self, name: str, address: str):
        Person.__init__(self, name, address)
        self.course = []
        self.numCourse = 0

    def toString(self):
        return f'{Person.toString(self)}'

    def addCourse(self, course):
        if course in self.course:
            return False
        else:
            self.course.append(course)
            self.numCourse = len(self.course)
            return True

    def rmvCourse(self, course):
        if course not in self.course:
            return False
        else:
            self.course.remove(course)
            self.numCourse = len(self.course)
            return True

    def getNumCourse(self):
        return self.numCourse


def main():
    stdnt = Student('Ricky', 'Bali, ID')
    print(stdnt.toString())
    stdnt.aCourseGrade('English', 91)
    stdnt.aCourseGrade('Indonesian', 87)
    stdnt.aCourseGrade('Mathematics', 95)
    stdnt.aCourseGrade('Physics', 85)
    stdnt.aCourseGrade('Information Technology', 89)
    print(stdnt.getAvgGrade())
    print(stdnt.aCourseGrade())
    print(stdnt.printGrades())
    tcher = Teacher('Ms. Jackson', 'Sydney, AU')
    tcher.addCourse("English ")
    tcher.addCourse('Indonesian ')
    tcher.addCourse('Mathematics ')
    tcher.addCourse('Physics')
    tcher.addCourse('Information Technology')
    print(tcher.getNumCourse())
    tcher.rmvCourse('Indonesian')
    tcher.rmvCourse('Physics')
    print(tcher.getNumCourse())


main()

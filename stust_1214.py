class Student:
    def __init__(self, name, ID, major):
        self._name = name
        self._ID = ID
        self._major = major
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Course '{course}' added successfully for {self._name}.")
        else:
            print(f"You're already enrolled in the course '{course}'.")

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"Course '{course}' dropped successfully for {self._name}.")
        else:
            print(f"You're currently not enrolled in the course '{course}'.")

    def display_courses(self):
        if self.courses:
            print(f"List of courses for {self._name}:")
            for course in self.courses:
                print(course)
        else:
            print(f"No courses enrolled yet for {self._name}.")

# 使用示例
student1 = Student("Judy", "0055", "Computer Science")
student1.add_course("Math")
student1.add_course("English")
student1.display_courses()

student1.add_course("Math")  # Trying to add a course already enrolled
student1.drop_course("English")
student1.display_courses()

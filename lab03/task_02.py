class Student:
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Группа: {self.group}")


student = Student("Анна", 20, "ПИ-21")
student.show_info()

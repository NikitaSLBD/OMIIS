
class Student_сontroller:
    from models.services.student_service import Student_service, Student

    student_service = Student_service

    @classmethod
    def register_student(cls, student: Student) -> str:
    
        cls.student_service.save(student)
        return f"Student with ID {student.get_id()} registered successfully."

    @classmethod
    def get_student(cls, id: int) -> Student:
       
        student = cls.student_service.find_by_id(id)
        if not student:
            raise ValueError(f"Student with ID {id} not found.")
        return student

    @classmethod
    def list_students(cls) -> list[Student]: return cls.student_service.find_all()
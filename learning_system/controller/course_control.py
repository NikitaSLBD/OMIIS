
class Course_сontroller:
    from models.services.course_service import Course_service, Course


    course_service = Course_service

    @classmethod
    def create_course(cls, course: Assignment) -> str:

        cls.course_service.save(course)
        return f"Course with ID {course.get_id()} created successfully."

    @classmethod
    def get_course(cls, id: int) -> Assignment:
        
        course = cls.course_service.find_by_id(id)
        if not course:
            raise ValueError(f"Course with ID {id} not found.")
        return course

    @classmethod
    def list_courses(cls) -> list[Assignment]:
       
        return cls.course_service.find_all()
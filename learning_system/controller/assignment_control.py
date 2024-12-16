class Assignment_сontroller:
    from models.services.assignment_service import Assignment_service, Assignment


    assignment_service = Assignment_service

    @classmethod
    def create_assignment(cls, assignment: Assignment) -> str:
       
        cls.assignment_service.save(assignment)
        return f"Assignment with ID {assignment.get_id()} created successfully."

    @classmethod
    def get_assignment(cls, id: int) -> Assignment:
    
        assignment = cls.assignment_service.find_by_id(id)
        if not assignment:
            raise ValueError(f"Assignment with ID {id} not found.")
        return assignment

    @classmethod
    def list_assignments(cls) -> list[Assignment]:
    
        return cls.assignment_service.find_all()

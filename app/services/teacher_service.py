class TeacherService:

    # La "base de données" en mémoire
    teachers = [
        {"id": 1, "name": "Mr. Aly N. Tall",       "email": "alytallniang@edu.com",      "speciality": "Python & Data"},
        {"id": 2, "name": "Birane Baila Wane",  "email": "wane@edu.com",  "speciality": "Programmation"},
        {"id": 3, "name": "Dr. Diaby",        "email": "diaby@edu.com",      "speciality": "CyberSecurity"},
    ]

    next_id = 4

    def listTeachers(self) -> list:
        return self.teachers
    
    def getTeacherById(self, teacher_id: int) -> dict | None:
        for teacher in self.teachers:
            if teacher["id"] == teacher_id:
                return teacher
        return None

    def addTeacher(self, name: str, email: str, speciality: str) -> bool:
        if not name or not email or not speciality:
            return False
        
        for teacher in self.teachers:
            if teacher["email"] == email:
                return False

        new_teacher = {
            "id":         self.next_id,
            "name":       name,
            "email":      email,
            "speciality": speciality
        }

        self.teachers.append(new_teacher)
        self.next_id += 1
        return True

    def deleteTeacher(self, teacher_id: int) -> bool:
        for teacher in self.teachers:
            if teacher["id"] == teacher_id:
                self.teachers.remove(teacher)
                return True
        return False
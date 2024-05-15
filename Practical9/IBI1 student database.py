class students:
    'It is a class which contain students name, major (BMI/BMS); score for their code portfolio; score for their group project;and exam	score'
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def show_details(self):
        return f"Name: {self.name}, Major: {self.major}, Code portfolio score: {self.code_portfolio_score}, Group project score: {self.group_project_score}, Exam score: {self.exam_score}"

# An example of the usage of this class 
student_A = students("Yuan Yizhou", "BMI", 100, 99.5, 100)
studentA_details = student_A.show_details()
print(studentA_details)              

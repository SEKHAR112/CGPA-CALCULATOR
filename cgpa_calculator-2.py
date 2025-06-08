grades={'o':10,'s':9,'a':8,'b':7,'c':6,'d':5}

def get_valid_grade(prompt):
    while(True):
        gr=input(prompt).strip().lower()
        if gr in grades:
            return grades[gr]
        else:
            print("Invalid grade, Please enter one of : o, s, a, b, c, d")



class cgpa_calculator:
    def disclaimer(self):
        print("\n*THIS CODE FOLLOWS GENERAL CGPA CALCULATION FORMULA OF JNTUK R19 REGULATION*\n")
    def __init__(self):
        self.subject_total=0
        self.labs_total=0
        self.projects=1
        self.drawing=0
        self.other_subject=0
        self.total_credits=0


    def subjects(self):
        print("---------------------------------------------------------------------------------")
        subject=int(input("Enter number of subjects: "))
        for i in range(subject):
            grade= get_valid_grade("Enter grade of subject "+ str(i+1) +":")
            self.subject_total+=grade*3
            self.total_credits+=3

    def labs(self):
        print("---------------------------------------------------------------------------------")
        lab=int(input("Enter number of labs: "))
        for i in range(lab):
            grade=get_valid_grade("Enter grade of lab "+ str(i+1) +":")
            self.labs_total+=grade*1.5
            self.total_credits+=1.5

    def project(self):
        print("---------------------------------------------------------------------------------")
        grade=get_valid_grade("Enter grade of project: ")
        self.projects=grade*9
        self.total_credits+=9

    def other_subjects(self):
        print("---------------------------------------------------------------------------------")
        grade=get_valid_grade("Enter grade of Engineering drawing: ")
        self.drawing+=grade*2.5
        self.total_credits+=2.5
        print("---------------------------------------------------------------------------------")

        other_sub = int(input("Enter number of subjects that have 1 credit :"))
        for i in range(other_sub):
            grade=get_valid_grade("Enter grade of 1-credit subject "+ str(i+1) +":")
            self.other_subject+=grade*1
            self.total_credits+=1


    def total(self):
        self.subjects()
        self.labs()
        self.project()
        self.other_subjects()
        

        total=self.subject_total+self.labs_total+self.projects+self.drawing+self.other_subject
        print("---------------------------------------------------------------------------------")
        print("Your CGPA is :",round(total/self.total_credits,2))


cgpa= cgpa_calculator()
cgpa.disclaimer()
cgpa.total()
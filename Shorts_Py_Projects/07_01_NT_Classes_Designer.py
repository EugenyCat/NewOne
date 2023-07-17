"""
Write a Designer class that takes into account the number of international prizes.

The comment for the Designer class is:
Write a Designer class that takes into account the number of international awards for designers
(from the presentation: "Increase by 1 grade for every 7 points. Receiving an international award is +2 points").
Consider that when you come to work, the employee already has two bonuses and their number does not change with seniority
(of course if you want to change it manually).
"""


class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority

        self.grade = 1


    def grade_up(self):
        """Increase level of employee"""
        self.grade += 1


    def publish_grade(self):
        """Publish results of accreditation of employee"""
        print(self.name, self.grade)


    def check_if_it_is_time_for_upgrade(self):
        pass


class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        """
        For each accreditation increase grade on 1
        Think that every developer do accreditation
        """
        self.seniority += 1

        #conditional increase grade
        if self.seniority % 5 == 0:
            self.grade_up()

        return self.publish_grade()



class Designer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
        self.award = 2

    def international_award(self):
        self.seniority += self.award

        # conditional increase grade
        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()

designer = Designer('Jake', 0)

for aw in range(20):
    designer.international_award()
from django.db import models

# Create your models here.


class Classe(models.Model):
    name = models.CharField(max_length=400)
    sub_name = models.CharField(max_length=400)
    no_of_students = models.CharField(max_length=400)

    def __str__(self):
        return self.name + ' - ' + self.sub_name


class Student(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=400)
    middle_name = models.CharField(max_length=400, blank=True)
    last_name = models.CharField(max_length=400)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=400, choices=(('Male', 'Male'), ('Female', 'Female')))
    residential_address = models.CharField(max_length=600)

    def __str__(self):
        return self.classe + ' - ' + self.first_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=400)
    middle_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30)
    residential_address = models.CharField(max_length=600)

    def __str__(self):
        return self.first_name


class ParentDetail(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=400)
    first_name = models.CharField(max_length=400)
    middle_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    nationality = models.CharField(max_length=400)
    profession = models.CharField(max_length=400)
    special_skills = models.CharField(max_length=400)
    identity_number = models.CharField(max_length=400)
    number_of_children = models.CharField(max_length=400)
    date_of_birth = models.DateField()
    identity_type = models.CharField(max_length=100)
    picture = models.CharField(max_length=600)

    def __str__(self):
        return self.student_id


class Sponsorship(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor_name = models.CharField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField()
    award_type = models.CharField(max_length=400)
    payment_type = models.CharField(max_length=400)
    payment_method = models.CharField(max_length=400)
    details = models.CharField(max_length=400)
    total_amount = models.CharField(max_length=400)
    amount_payed = models.CharField(max_length=400)
    amount_owed = models.CharField(max_length=400)


class StudentAdmissionRecord(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=400)
    applied_on = models.DateField()
    admitted_on = models.DateField()
    admitted_by = models.CharField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField()
    expected_graduation_date = models.DateField()
    actual_graduation_date = models.DateField()
    placement = models.CharField(max_length=400)
    status = models.CharField(max_length=400)


class StudentEnrollmentRecord(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    type = models.CharField(max_length=400)
    level_name = models.CharField(max_length=400)
    placement = models.CharField(max_length=400)
    class_name = models.CharField(max_length=400)
    concentration = models.CharField(max_length=400)
    cleared_for_enrollment = models.DateField()
    enrollment_year = models.DateField()
    enroll_on = models.DateField()
    enrolled_by = models.CharField(max_length=400)
    balance = models.CharField(max_length=400)
    remarks = models.CharField(max_length=400)


class Term(models.Model):
        term_name = models.CharField(max_length=400)
        academic_year_id = models.DateField()


class Department(models.Model):
        name = models.CharField(max_length=400)
        head_of_department = models.CharField(max_length=400)


class Subject(models.Model):
    name = models.CharField(max_length=400)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)


class Score(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE)



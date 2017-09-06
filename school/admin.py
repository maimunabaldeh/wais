from django.contrib import admin

#from .models import Student, Teacher,ParentDetail, Classe, Sponsorship, StudentAdmissionRecord, StudentEnrollmentRecord
from .models import *

admin.site.register(Classe)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ParentDetail)
admin.site.register(Sponsorship)
admin.site.register(StudentAdmissionRecord)
admin.site.register(StudentEnrollmentRecord)
admin.site.register(Score)


from django.db import models

class Student(models.Model):
    GENDER_CHOICES=[("Male","Male"),
                    ("Female","Female"),
                    ("Other","Other")]
    student_name=models.CharField(max_length=100,default='')
    father_name=models.CharField(max_length=100,default='')
    mobile_number=models.CharField(max_length=10)
    dob=models.DateField(default=None)
    gender=models.CharField(max_length=100, choices=GENDER_CHOICES)    
    email=models.EmailField(unique=True)
    class_student=models.CharField(max_length=10)
    roll_number=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name
    class Meta:
        db_table="Student"
        ordering=["student_name"]
class Teachers(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True) 
    mobile_number=models.CharField(max_length=10)
    subjects=models.CharField(max_length=100)
    Assigned_class=models.CharField(max_length=100)
    password=models.CharField(max_length=100)       

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)     

class Notification(models.Model):
    send_choices=[
        ('all_students' ,'All Students'),
        ('all_teachers', 'AllTeachers'),
        ('specific_class' , 'Specific Class'),
        ('specific_teacher' , 'Specific Teacher'),
    ]
    send_to=models.CharField(max_length=50) 
    title=models.CharField(max_length=100)
    message=models.TextField()
    type_choice=[
        ('general' , 'General'),
        ('important' , 'Important'),
        ('alert' , 'Alert'),
    ]
    message_type=models.CharField(max_length=50)
    sceduled_date=models.DateField(null=True,blank=True)
    attached_file=models.FileField(upload_to='notification/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title      



    

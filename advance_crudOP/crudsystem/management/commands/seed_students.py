import random
from django.core.management.base import BaseCommand
from crudsystem.models import Student, Department, Course
from faker import Faker

# Faker instance create karein random data ke liye
fake = Faker()

class Command(BaseCommand):
    help = "Seed database with random student data"

    def handle(self, *args, **kwargs):
        # 1. Pehle kuch Departments aur Courses create karte hain (Basic Setup)
        departments_data = {
            'Computer Science': ['BCA', 'MCA', 'B.Tech CS'],
            'Agriculture': ['B.Sc Agriculture', 'M.Sc Agriculture'],
            'Management': ['BBA', 'MBA']
        }

        self.stdout.write("Seeding data...")

        for dept_name, courses in departments_data.items():
            # Department object banayein
            dept_obj, created = Department.objects.get_or_create(name=dept_name)

            for course_name in courses:
                # Course object banayein aur Department assign karein
                Course.objects.get_or_create(name=course_name, department=dept_obj)

        # 2. Saare Departments aur Courses ko fetch karein taaki students ko assign kar sakein
        all_departments = list(Department.objects.all())
        all_courses = list(Course.objects.all())

        # 3. 20 Naye Students create karein
        for _ in range(20):
            # Random data generate karein
            random_dept = random.choice(all_departments)
            # Sirf wahi courses lein jo us department ke hain
            available_courses = Course.objects.filter(department=random_dept)
            random_course = random.choice(available_courses)

            std_roll = f"STU-{fake.unique.random_int(min=1000, max=9999)}"
            
            # Galti yahan thi: Humein instances (objects) pass karne hain
            student, created = Student.objects.get_or_create(
                std_roll=std_roll, 
                defaults={
                    'std_name': fake.name(),
                    'std_village': fake.city(),
                    'std_pinCode': fake.zipcode(),
                    'department': random_dept,   
                    'course': random_course,    
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created student: {student.std_name} ({std_roll})"))
            else:
                self.stdout.write(self.style.WARNING(f"Student {std_roll} already exists."))

        self.stdout.write(self.style.SUCCESS("Database Seeding Completed!"))
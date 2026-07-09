from django.test import TestCase
from django.urls import reverse

from .models import Branch, Course, Student


class StudentRegistrationViewTests(TestCase):
    def test_student_registration_creates_student(self):
        course = Course.objects.create(course_name="BCA")
        branch = Branch.objects.create(course=course, branch_name="Computer")

        response = self.client.post(
            reverse("student_registration"),
            {
                "std_name": "Amit Sharma",
                "course": course.id,
                "branch": branch.id,
                "semester": 3,
                "std_roll": "101",
                "std_no": "1001",
                "std_email": "amit@example.com",
                "std_address": "Delhi",
                "std_dob": "2001-01-01",
                "gender": "MALE",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("student_registration"))
        self.assertTrue(Student.objects.filter(std_roll="101").exists())

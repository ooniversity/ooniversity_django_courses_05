from django.test import TestCase
from students.models import Student
from courses.models import Course
from django.test import Client



def initialize_test():
    course1 = Course.objects.create(
                        name='pybursa',
                        short_description='web django')
    student1 = Student.objects.create(
                        name='Ivan',
                        surname='Ivanov',
                        date_of_birth='2016-11-27',
                        email='sdsdf@fg.com',
                        phone='345345345345',
                        address='street',
                        skype='vanua')
    student1.courses.add(course1)


class StudentsListTest(TestCase):

    def test_student(self):
        initialize_test()
        self.assertEqual(Student.objects.all().count(), 1)

    def test_links_students(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Contacts')

    def test_links_2_students(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Main')

    def test_links_3_students(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Feedback')

    def test_links_4_students(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Students')


class StudentsDetailTest(TestCase):

    def test_students_detail(self):
        client = Client()
        initialize_test()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        client = Client()
        initialize_test()
        response = self.client.get('/students/1/')
        self.assertContains(response, '345345345345')

    def test_adding(self):
        client = Client()
        initialize_test()
        response = self.client.get('/students/add/')
        self.assertEqual(response.status_code, 200)

    def test_student_editing_page(self):
        client = Client()
        initialize_test()
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'Ivanov')

    def test_student_deleting(self):
        client = Client()
        initialize_test()
        self.client.delete('/students/remove/1/','Delete')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
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


class StudentsDetailTest(TestCase):

    def test_create_student(self):
        initialize_test()
        self.assertEqual(Student.objects.all().count(), 1)

    def test_page(self):
        client = Client()
        initialize_test()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_3(self):
        client = Client()
        initialize_test()
        response = self.client.get('/students/add/')
        self.assertEqual(response.status_code, 200)

    def test_4(self):
        client = Client()
        initialize_test()
        response = self.client.get('/students/edit/1/')
        self.assertContains(response, 'Ivanov')

    def test_5(self):
        client = Client()
        initialize_test()
        self.client.delete('/students/remove/1/','Delete')
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
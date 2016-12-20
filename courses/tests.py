from django.test import TestCase
from courses.models import Course, Lesson
from django.test import Client
# Create your tests here.


def initialize_test():
    course1 = Course.objects.create(
                        name='pybursa',
                        short_description='web django')
    lesson1 = Lesson.objects.create(
                        subject='pybursa',
                        description='web django',
                        course=course1,
                        order=1)

class CoursesListTest(TestCase):

    def test_1(self):
        initialize_test()
        self.assertEqual(Course.objects.all().count(), 1)

    def test_2(self):
        client = Client()
        initialize_test()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_3(self):
        initialize_test()
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_4(self):
        client = Client()
        initialize_test()
        response = self.client.get('/courses/edit/1/')
        self.assertContains(response, 'pybursa')

    def test_5(self):
        client = Client()
        initialize_test()
        response = self.client.get('/courses/1/add_lesson')
        self.assertEqual(response.status_code, 200)

    def test_6(self):
        client = Client()
        initialize_test()
        self.client.delete('/courses/remove/1/', 'Delete')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
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

    def test_course_creation(self):
        initialize_test()
        self.assertEqual(Course.objects.all().count(), 1)

    def test_lesson_adding_page(self):
        initialize_test()
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_links_courses(self):
        initialize_test()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'Main')

    def test_links_2_courses(self):
        initialize_test()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'Main')

    def test_links_3_courses(self):
        initialize_test()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'Feedback')

class CoursesDetailTest(TestCase):

    def test_course_details(self):
        client = Client()
        initialize_test()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_detail_course(self):
        client = Client()
        initialize_test()
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'pybursa')

    def test_course_editing(self):
        client = Client()
        initialize_test()
        response = self.client.get('/courses/edit/1/')
        self.assertContains(response, 'pybursa')

    def test_course_adding_lesson(self):
        client = Client()
        initialize_test()
        response = self.client.get('/courses/1/add_lesson')
        self.assertEqual(response.status_code, 200)

    def test_course_deleting(self):
        client = Client()
        initialize_test()
        self.client.delete('/courses/remove/1/', 'Delete')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

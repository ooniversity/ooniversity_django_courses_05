from django.test import TestCase, Client
from django.urls import reverse

from courses.models import Course, Lesson


def create_course(name):
    Course.objects.create(
        name=name,
        short_description=name + ' description',
        description='course description',
    )

def create_lesson(name, course):
    Lesson.objects.create(
        subject=name,
        order=555,
        description='lesson description',
        course=course,
    )


class CoursesListTest(TestCase):

    def test_valid_links(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)

        response = client.get('/contact/')
        self.assertEquals(response.status_code, 200)

        response = client.get('/students/')
        self.assertEquals(response.status_code, 200)

        response = client.get('/feedback/')
        self.assertEquals(response.status_code, 200)

    def test_add_course(self):
        create_course('Course_Test1')
        client = Client()

        response = client.get('/courses/1/')
        self.assertEquals(response.status_code, 200)

    def test_manage_links(self):
        create_course('Course_Test1')
        create_course('Course_Test2')
        create_course('Course_Test3')
        client = Client()

        response = client.get('/courses/add/')
        self.assertEquals(response.status_code, 200)

        response = client.get('/courses/edit/2/')
        self.assertEquals(response.status_code, 200)

        response = client.get('/courses/remove/3/')
        self.assertEquals(response.status_code, 200)


    def test_table_info(self):
        create_course('Course_Test1')
        client = Client()

        response = client.get(reverse('index'))
        self.assertContains(response, 'Course_Test1')

    def test_head(self):
        create_course('Course_Test1')
        client = Client()
        response = client.get(reverse('index'))
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')
        self.assertContains(response, 'Feedback')


class CoursesDetailTest (TestCase):

    def test_students_page(self):
        create_course('Course_Test1')
        client = Client()
        response = client.get('/courses/1/')
        self.assertEquals(response.status_code, 200)

    def test_head_links(self):
        create_course('Course_Test1')
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')
        self.assertContains(response, 'Feedback')

    def test_course_info(self):
        create_course('Course_Test1')
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Course_Test1')
        self.assertContains(response, 'course description')

    def test_courses_lesson(self):
        create_course('Course_Test1')
        course = Course.objects.get(id=1)
        create_lesson('Lesson_Test1', course)
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, 'Lesson_Test1')

    def test_lesson_info(self):
        create_course('Course_Test1')
        course = Course.objects.get(id=1)
        create_lesson('Lesson_Test1', course)
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, '555')
        self.assertContains(response, 'lesson description')

    def test_add_lesson(self):
        create_course('Course_Test1')
        client = Client()
        response = client.get('/courses/1/add_lesson')
        self.assertEquals(response.status_code, 200)

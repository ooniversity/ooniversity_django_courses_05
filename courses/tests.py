from django.test import TestCase, Client
from .models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class CoursesListTest(TestCase):
    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        self.assertEquals(Course.objects.all().count(), 1)

    def test_page(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_valid_link_main(self):
        response = self.client.get('/')
        self.assertContains(response, 'Main')

    def test_valid_link_contacts(self):
        response = self.client.get('/')
        self.assertContains(response, 'Contacts')

    def test_valid_link_students(self):
        response = self.client.get('/')
        self.assertContains(response, 'Students')


class CoursesDetailTest(TestCase):
    def create_lesson(self, course, order):
        lesson = Lesson.objects.create(
            subject='Name of Lesson',
            description='Description of Lesson',
            course=course,
            order=order,
        )
        return lesson

    def test_course_detail(self):
        course1 = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        response = self.client.get('/courses/1/')
        self.assertContains(response, course1.name)

    def test_course_detail_response(self):
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        response = self.client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_list_lessons_course(self):
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
        )
        lesson2 = self.create_lesson(course, 2)
        lesson3 = self.create_lesson(course, 3)
        client = Client()
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_coach_course(self):
        user = User(first_name='Vladislav', last_name='Yushchuk')
        user.save()
        coach = Coach.objects.create(
            user=user,
            date_of_birth='1989-01-01',
            gender='M',
            phone='+380937707670',
            address='Ukraine, Poltava, Lesnaya str 24',
            skype='FireTheEagle',
            description='Good coach',
        )
        course = Course.objects.create(
            name='Some Course',
            short_description='Short description',
            description='Default',
            coach=coach,
        )
        response = self.client.get('/courses/{1}/'.format(course.id))
        self.assertContains(response, '/coaches/{1}/'.format(coach.id))
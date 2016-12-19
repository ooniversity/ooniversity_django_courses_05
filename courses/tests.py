from django.test import TestCase, Client
from .models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class CoursesListTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        Course.objects.create(name='Django', short_description='Web разработка на Python/Django',
            description='Курс для начинающих',)
        self.assertEquals(Course.objects.all().count(), 1)

    def test_course_detail(self):
        client = Client()
        Course.objects.create(name="Html/Css", short_description='HTML5 with CSS3')
        response = self.client.get('/', follow=True)
        self.assertContains(response, '/courses/1/')

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
    def test_course_detail(self):
        course = Course.objects.create(name='Java', short_description='Изучаем Java', description='Java для начинающих',)
        response = self.client.get('/courses/1/')
        self.assertContains(response, course.name)

    def test_course_detail_response(self):
        Course.objects.create(name='Course', short_description='Short description', description='Description',)
        response = self.client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def create_lesson(self, course, order):
        lesson = Lesson.objects.create(subject='Урок 1', description='Описание урока 1', course=course, order=order,)
        return lesson

    def test_lesson_create(self):
        course = Course(name='Python/Django')
        course.save()
        Lesson.objects.create(
            subject='Списки',
            description='Изучаем списки в Python',
            course=course,
            order='1',
        )
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_list_lessons(self):
        course = Course.objects.create(name='Course', short_description='Short description', description='Description',)
        lesson2 = self.create_lesson(course, 2)
        lesson3 = self.create_lesson(course, 3)
        client = Client()
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)

    def test_coach_course(self):
        user = User(first_name='Ivanov', last_name='Ivan')
        user.save()
        coach = Coach.objects.create(
            user=user,
            date_of_birth='1985-12-12',
            gender='M',
            phone='982374092374',
            address='Москва, ул. Ленина, д. 154, кв. 222',
            skype='Ivanov_I',
            description='Основатель курса',
        )
        course = Course.objects.create(name='Course', short_description='Short description',
                                       description='Description', coach=coach,)
        response = self.client.get('/courses/{1}/'.format(course.id))
        self.assertContains(response, '/coaches/{1}/'.format(coach.id))
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.test import Client

from coaches.models import Coach
from courses.models import Course, Lesson


class CoursesListTest(TestCase):
    c = Client()

    def test_course_list_200_ok(self):
        response = self.c.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_detail_not_found(self):
        response = self.c.get(reverse('courses:detail', args='1'))
        self.assertEqual(response.status_code, 404)

    def test_course_show_info(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        response = self.c.get(reverse('courses:detail', args=(course.id,)))
        self.assertContains(response, 'Test Course')

    def test_description_shows(self):
        response = self.c.get(reverse('index'))
        self.assertContains(response=response, text="Description")

    def test_program_shows(self):
        response = self.c.get(reverse('index'))
        self.assertContains(response=response, text="Program")

    def test_course_edit_go_and_displays(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        response = self.c.get(reverse('courses:edit', args=(course.id,)))
        self.assertContains(response, 'Test Course')

    def test_course_delete_go_and_displays(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        response = self.c.get(reverse('courses:remove', args=(course.id,)))
        self.assertContains(response, 'Курс {0} будет удален'.format(course.name))

    def test_course_create_go_and_displays(self):
        response = self.c.get(reverse('courses:add'))
        self.assertContains(response, 'Create new Course')


class CoursesDetailTest(TestCase):
    c = Client()

    def create_lesson(self, course, order):
        lesson = Lesson.objects.create(subject='Subject of lesson{0}'.format(order),
                                       description='Small description of lesson {0}'.format(order),
                                       course=course,
                                       order=order)
        return lesson

    def create_coach(self, first_name, last_name, username):
        user = User(first_name=first_name, last_name=last_name, username=username)
        user.save()
        coach = Coach.objects.create(user=user,
                                     date_of_birth='1988-01-11',
                                     gender='F',
                                     phone='0930674890',
                                     address='Tests',
                                     skype='Test',
                                     description='Test'
                                     )
        coach.save()
        return coach

    def test_course_detail_page_found(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        response = self.c.get(reverse('courses:detail', args=(course.id,)))
        self.assertContains(response, 'Test Course')

    def test_course_lesson_create_and_displaied(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        lesson1 = self.create_lesson(course, 1)
        response = self.c.get(reverse('courses:detail', args=(course.id,)))
        self.assertContains(response, 'Subject of lesson1')

    def test_course_create_more_lesson(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        lesson1 = self.create_lesson(course, 1)
        lesson2 = self.create_lesson(course, 2)
        lesson3 = self.create_lesson(course, 3)
        self.assertEqual(Lesson.objects.all().count(), 3)

    def test_add_lesson_work(self):
        course = Course.objects.create(name='Test Course', short_description='Web tests course')
        response = self.c.get(reverse('courses:add_lesson', args=(course.id,)))
        self.assertContains(response, 'Create new Lesson')

    def test_courses_coach_displaied(self):
        coach = self.create_coach(first_name='Nana', last_name='Nanaeva', username='Nana')
        assistant = self.create_coach(first_name='Banna', last_name='Berga', username='Banna')
        course = Course.objects.create(name='Test Course', short_description='Web tests course', coach=coach,
                                       assistant=assistant)
        response = self.c.get(reverse('courses:detail', args=(course.id,)))
        self.assertContains(response, 'Nana')

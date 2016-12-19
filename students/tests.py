from django.test import TestCase, Client
from . models import Student
from courses.models import Course
from django.urls import reverse


class StudentsListTest(TestCase):
    def test_pages_student_list(self):
        client = Client()
        Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_page_student_create(self):
        Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        self.assertEqual(Student.objects.all().count(), 1)

    def test_page_student_edit(self):
        client = Client()
        Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        response = self.client.get('/students/', follow=True)
        self.assertContains(response, '/students/edit/1/')

    def test_page_student_delete(self):
        client = Client()
        Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        response = self.client.get('/students/', follow=True)
        self.assertContains(response, '/students/remove/1/')

    def test_list_students(self):
        response = self.client.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)

    def test_valid_links(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')


class StudentsDetailTest(TestCase):
    def test_student_detail(self):
        client = Client()
        Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        response = client.get('/students/1/')
        self.assertContains(response, 'Ivan')
        self.assertContains(response, 'Ivanov')

    def test_link_menu(self):
        response = Student(name = "Ivan",)
        response = self.client.get('/students/', follow=True)
        self.assertContains(response, '/')
        self.assertContains(response, '/students/')
        self.assertContains(response, '/contact/')
        self.assertContains(response, '/feedback/')

    def test_students_full_name(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        response = self.client.get('/students/{0}/'.format(student.id))
        self.assertContains(response, student.full_name)

    def test_students_valid_info(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        response = self.client.get('/students/{0}/'.format(student.id))
        self.assertContains(response, 'дата рождения')
        self.assertContains(response, 'адрес')
        self.assertContains(response, 'почта')
        self.assertContains(response, 'телефон')
        self.assertContains(response, 'логин skype')

    def test_students_courses(self):
        student = Student.objects.create(
            name='Ivan',
            surname='Ivanov',
            address='Москва, ул. Ленина, 155-222',
            skype='Ivanov_I',
            phone='+7923849028',
            date_of_birth='1901-01-01',
            email='ivanov@mail.ru',
        )
        course1 = student.courses.create(name='Python/Django', short_description='Web with Django',
                                         description='Description',)
        course2 = student.courses.create(name='Java', short_description='Web with Java', description='Description', )
        response = self.client.get('/students/{0}/'.format(student.id))
        self.assertContains(response, '/courses/{0}/'.format(course1.id))
        self.assertContains(response, '/courses/{0}/'.format(course2.id))
        self.assertEqual(student.courses.all()[0], course1)
        self.assertEqual(student.courses.all()[1], course2)
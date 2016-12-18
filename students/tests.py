from django.test import Client
from django.test import TestCase
from django.urls import reverse

from courses.models import Course
from students.models import Student


class StudentsListTest(TestCase):
    c = Client()

    def create_student(self):
        student = Student.objects.create(name='Tatyana', surname='Paschenko',
                                         date_of_birth='1988-01-11',
                                         phone='0930444509',
                                         address='Украина, г.Харьков, ул.Мумухиных, д.38, кв.7',
                                         skype='test')
        return student

    def test_student_list_200_ok(self):
        response = self.c.get(reverse('students:list_view'))
        self.assertEqual(response.status_code, 200)

    def test_header_shows(self):
        response = self.c.get(reverse('students:list_view'))
        self.assertContains(response=response, text="BrainBursa students list")

    def test_student_create(self):
        self.create_student()
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student_detail_not_found(self):
        response = self.c.get(reverse('students:detail', args='1'))
        self.assertEqual(response.status_code, 404)

    def test_student_show_info(self):
        student = self.create_student()
        response = self.c.get(reverse('students:detail', args=(student.id,)))
        self.assertContains(response, 'Tatyana')

    def test_student_edit(self):
        student = self.create_student()
        response = self.c.get(reverse('students:edit', args=(student.id,)))
        self.assertContains(response, 'Tatyana')

    def test_student_delete(self):
        student = self.create_student()
        response = self.c.get(reverse('students:remove', args=(student.id,)))
        self.assertContains(response, 'Студент {0} будет удален '.format(student.name))

    def test_student_create_page_found(self):
        response = self.c.get(reverse('students:add'))
        self.assertContains(response, 'Create new Student')


class StudentsDetailTest(TestCase):
    c = Client()

    def create_student(self, name, surname):
        student = Student.objects.create(name=name, surname=surname,
                                         date_of_birth='1988-01-11',
                                         phone='0930444509',
                                         address='Украина, г.Харьков, ул.Мумухиных, д.38, кв.7',
                                         skype='test')
        return student

    def test_students_detail_page_200_ok(self):
        student = self.create_student(name='Tatyana', surname='Paschenko')
        response = self.c.get(reverse('students:detail', args=(student.id,)))
        self.assertContains(response, 'Tatyana')

    def test_student_detail_not_found(self):
        response = self.c.get(reverse('students:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_course_for_student_displaied(self):
        student = self.create_student(name='Tatyana', surname='Paschenko')
        course1 = student.courses.create(name='Test Course', short_description='Web tests course')
        course2 = student.courses.create(name='Test Course2', short_description='Web tests course')
        response = self.c.get(reverse('students:detail', args=(student.id,)))
        self.assertContains(response, 'Test Course')
        self.assertContains(response, 'Test Course2')

    def test_student_detail_page_contain_mail_fields(self):
        student = self.create_student(name='Tatyana', surname='Paschenko')
        response = self.c.get(reverse('students:detail', args=(student.id,)))
        self.assertContains(response, 'дата рождения')
        self.assertContains(response, 'адрес')
        self.assertContains(response, 'почта')
        self.assertContains(response, 'телефон')
        self.assertContains(response, 'skype')

    def test_course_for_student_linkable(self):
        student = self.create_student(name='Tatyana', surname='Paschenko')
        course = student.courses.create(name='Test Course', short_description='Web tests course')
        response = self.c.get(reverse('courses:detail', args=(course.id,)))
        self.assertEqual(response.status_code, 200)

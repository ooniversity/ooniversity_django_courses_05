from django.contrib.gis.geos.prototypes.geom import create_collection
from django.test import TestCase, Client
from courses.models import Course
from students.models import Student


def create_student(name, surname):
    Student.objects.create(
        name=name,
        surname=surname,
        date_of_birth='1980-01-01',
        email='email@email.co',
        phone='phone',
        address='address',
        skype='skype',
    )


def create_course(name):
    Course.objects.create(
        name=name,
        short_description=name + ' description',
        description='course description',
    )


class StudentsListTest (TestCase):

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


    def test_add_student(self):
        create_student('Name_Test1', 'SurName_Test1')
        client = Client()

        response = client.get('/students/1/')
        self.assertEquals(response.status_code, 200)



    def test_pagination(self):
        create_student('Name_Test1', 'SurName_Test1')
        create_student('Name_Test2', 'SurName_Test2')
        create_student('Name_Test3', 'SurName_Test3')

        client = Client()

        response = client.get('/students/', {'page' : 1})
        self.assertEquals(response.status_code, 200)

        response = client.get('/students/', {'page' : 2})
        self.assertEquals(response.status_code, 200)

        response = client.get('/students/', {'page' : 3})
        self.assertEquals(response.status_code, 404)


    def test_manage_links(self):
        create_student('Name_Test1', 'SurName_Test1')
        create_student('Name_Test2', 'SurName_Test2')
        create_student('Name_Test3', 'SurName_Test3')
        client = Client()

        response = client.get('/students/add/')
        self.assertEquals(response.status_code, 200)

        response = client.get('/students/edit/2/')
        self.assertEquals(response.status_code, 200)

        response = client.get('/students/remove/3/')
        self.assertEquals(response.status_code, 200)

    def test_table_info(self):
        create_student('Name_Test1', 'SurName_Test1')
        client = Client()

        response = client.get('/students/')
        self.assertContains(response, 'address')
        self.assertContains(response, 'skype')
        self.assertContains(response, 'Name_Test1')
        self.assertContains(response, 'SurName_Test1')


class StudentsDetailTest (TestCase):

    def test_students_page(self):
        create_student('Name_Test1', 'SurName_Test1')
        client = Client()
        response = client.get('/students/1/')
        self.assertEquals(response.status_code, 200)

    def test_head_link(self):
        create_student('Name_Test1', 'SurName_Test1')
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Main')
        self.assertContains(response, 'Contacts')
        self.assertContains(response, 'Students')
        self.assertContains(response, 'Feedback')

    def test_students_info(self):
        create_student('Name_Test1', 'SurName_Test1')
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Jan. 1, 1980')
        self.assertContains(response, 'email@email.co')
        self.assertContains(response, 'skype')
        self.assertContains(response, 'address')
        self.assertContains(response, 'SurName_Test1')
        self.assertContains(response, 'Name_Test1')


    def test_students_courses(self):
        create_student('Name_Test1', 'SurName_Test1')
        create_course('Course_Test1')

        student = Student.objects.get(id=1)
        course = Course.objects.get(id=1)
        course.student_set.add(student)

        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Course_Test1')


    def test_students_name(self):
        create_student('Name_Test1', 'SurName_Test1')

        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Name_Test1 SurName_Test1')

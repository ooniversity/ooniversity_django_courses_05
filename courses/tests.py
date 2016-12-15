from django.test import TestCase
from. models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User

class CoursesListTest(TestCase):

    def test_pages_course_list(self):
        from django.test import Client
        client = Client()
        course1 = Course.objects.create(
		               name = "PyBursa02",
		               short_description = 'Web development with django')

        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        course1 = Course.objects.create(
		               name = "PyBursa02",
		               short_description = 'Web development with django')
        self.assertEqual(Course.objects.all().count(), 1)


    def test_course_detail(self):
        from django.test import Client
        client = Client()
        course1 = Course.objects.create(
		               name = "PyBursa02",
		               short_description = 'Web development with django')
        response = self.client.get('/', follow=True)
        self.assertContains(response, '/courses/1/')   

    
    def test_course_edit(self):
        from django.test import Client
        client = Client()
        course1 = Course.objects.create(
		               name = "PyBursa02",
		               short_description = 'Web development with django')
        response = self.client.get('/', follow=True)
        self.assertContains(response, '/courses/edit/1/') 

    
    def test_course_remove(self):
        from django.test import Client
        client = Client()
        course1 = Course.objects.create(
		               name = "PyBursa02",
		               short_description = 'Web development with django')
        response = self.client.get('/', follow=True)
        self.assertContains(response, '/courses/remove/1/') 
  
    def test_courses_name(self):
        course1 = Course(name = "PyBursa")
        self.assertEqual(course1.name, "PyBursa")


class CoursesDetailTest(TestCase):
    
    def test_pages_course_detail_404(self):
        from django.test import Client
        client = Client()

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
    
    def test_pages_course_detail_200(self):
        from django.test import Client
        client = Client()
        course1 = Course.objects.create(
		               name = "PyBursa02",
		               short_description = 'Web development with django')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PyBursa02")

    def test_lesson_create(self):
        course1 = Course(name = "Python")
        course1.save()
        lesson1 = Lesson.objects.create(
		               subject = "Calculator",
		               description = 'Python as calculator',
                               course = course1,
                               order = '1',
                 )
        lesson2 = Lesson.objects.create(
		               subject = "OOP",
		               description = 'OOP',
                               course = course1,
                               order = '2'
                  )
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_coach_create(self):
        from django.test import Client

        user1 = User(first_name = "Maria", last_name = 'Ivanova',)
        user1.save()
        coach1 = Coach.objects.create(
	               user = user1,
	               date_of_birth = '1980-06-14',
                       gender = 'F',
                       phone = '55555',
                       address = 'Kharkov',
                       skype = 'Anna',
                       description = 'profi',

         )
        coach1.save()
        course1 = Course.objects.create(
		               name = "Django",
		               short_description = 'Django it is cool',
                               description = 'Django it is very cool',
                               coach = coach1,
                 )
        client = Client()        
        response = client.get('/courses/1/')
        self.assertContains(response, "Maria")
        self.assertContains(response, "Ivanova")
        self.assertContains(response, "Django")

    def test_link_coach_detail(self):
        from django.test import Client

        user1 = User(first_name = "Maria", last_name = 'Ivanova',)
        user1.save()
        coach1 = Coach.objects.create(
	               user = user1,
	               date_of_birth = '1980-06-14',
                       gender = 'F',
                       phone = '55555',
                       address = 'Kharkov',
                       skype = 'Anna',
                       description = 'profi',

         )
        coach1.save()
        course1 = Course.objects.create(
		               name = "Django",
		               short_description = 'Django is cool',
                               description = 'Django is very cool',
                               coach = coach1,
                 )
        client = Client()        
        response = self.client.get('/courses/1/', follow=True)
        self.assertContains(response, 'coaches/1/') 
        









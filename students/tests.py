from django.test import TestCase
from. models import Student
from courses.models import Course

class StudentsListTest(TestCase):

    def test_pages_student_list(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_create(self):
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student_detail(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        response = self.client.get('/students/', follow=True)
        self.assertContains(response, '/students/1/')  

    def test_student_edit(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        response = self.client.get('/students/', follow=True)
        self.assertContains(response, '/students/edit/1/')  


    def test_student_remove(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        response = self.client.get('/students/', follow=True)
        self.assertContains(response, '/students/remove/1/')  


class StudentsDetailTest(TestCase):
    
    def test_pages_student_detail_404(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)
    
    def test_pages_student_detail_200(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)


    def test_student_detail(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        response = client.get('/students/1/')
        self.assertContains(response, "Lyuda")
        self.assertContains(response, "Kaluzhynova")

    def test_two_equal_students(self):
        from django.test import Client
        client = Client()
        student1 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        student2 = Student.objects.create(
		               name = "Lyuda",
                               surname = "Kaluzhynova",
                               address = "г. Харьков",
		               skype = 'kaluzhynoval',
			       date_of_birth = '1980-06-14',   
			       email = 'vlyuda@mail.ru',
			       phone = '096-3-777-463',  
                                  )
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_link_menu(self):
        student1 = Student(name = "Lyuda",)
        response = self.client.get('/students/', follow=True)
        self.assertContains(response, '/') 
        self.assertContains(response, '/students/') 
        self.assertContains(response, '/contact/') 
        self.assertContains(response, '/feedback/') 


  

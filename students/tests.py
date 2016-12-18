from django.test import TestCase
from . models import Student
from courses.models import Course

class StudentsListTest(TestCase):
	def test_pages_student_list(self):
		from django.test import Client
		client = Client()
		resp = Student.objects.create(
	        name = "Ivan", surname = "Ivanov",
            address = "Ukraine, Lviv, Ivanova str.28",
	        skype = 'ivanoviv', phone = '+380930010101',
	        date_of_birth = '1988-01-01',   
	        email = 'iv.ivanov@outlook.com')
		resp = client.get('/students/')
		self.assertEqual(resp.status_code, 200)

	def test_page_student_create(self):
		resp = Student.objects.create(
	        name = "Ivan", surname = "Ivanov",
            address = "Ukraine, Lviv, Ivanova str.28",
	        skype = 'ivanoviv', phone = '+380930010101',
	        date_of_birth = '1988-01-01',   
	        email = 'iv.ivanov@outlook.com')
		self.assertEqual(Student.objects.all().count(), 1)

	def test_page_student_edit(self):
		from django.test import Client
		client = Client()
		resp = Student.objects.create(
	        name = "Ivan", surname = "Ivanov",
            address = "Ukraine, Lviv, Ivanova str.28",
	        skype = 'ivanoviv', phone = '+380930010101',
	        date_of_birth = '1988-01-01',   
	        email = 'iv.ivanov@outlook.com')
		resp = self.client.get('/students/', follow=True)
		self.assertContains(resp, '/students/edit/1/')

	def test_page_student_remove(self):
		from django.test import Client
		client = Client()
		resp = Student.objects.create(
	        name = "Ivan", surname = "Ivanov",
            address = "Ukraine, Lviv, Ivanova str.28",
	        skype = 'ivanoviv', phone = '+380930010101',
	        date_of_birth = '1988-01-01',   
	        email = 'iv.ivanov@outlook.com')
		resp = self.client.get('/students/', follow=True)
		self.assertContains(resp, '/students/remove/1/')

	def test_page_student_detail(self):
		from django.test import Client
		client = Client()
		resp = Student.objects.create(
	        name = "Ivan", surname = "Ivanov",
            address = "Ukraine, Lviv, Ivanova str.28",
	        skype = 'ivanoviv', phone = '+380930010101',
	        date_of_birth = '1988-01-01',   
	        email = 'iv.ivanov@outlook.com')
		response = self.client.get('/students/', follow=True)
		self.assertContains(response, '/students/1/')

class StudentsDetailTest(TestCase):

	def test_page_student_detail_not_exist(self):
		from django.test import Client
		client = Client()
		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

	def test_page_student_detail_succes(self):
		from django.test import Client
		client = Client()
		resp = Student.objects.create(
	        name = "Ivan", surname = "Ivanov",
            address = "Ukraine, Lviv, Ivanova str.28",
	        skype = 'ivanoviv', phone = '+380930010101',
	        date_of_birth = '1988-01-01',   
	        email = 'iv.ivanov@outlook.com')
		response = self.client.get('/students/1/')
		self.assertEqual(response.status_code, 200)

	def test_student_detail(self):
		from django.test import Client
		client = Client()
		student1 = Student.objects.create(
			name = "Ivan",surname = "Ivanov",
			address = "Ukraine, Lviv, Ivanova str.28",
			skype = 'ivanoviv',
			date_of_birth = '1988-01-01',   
			email = 'iv.ivanov@outlook.com',
			phone = '+380930010101')
		response = client.get('/students/1/')
		self.assertContains(response, "Ivan")
		self.assertContains(response, "Ivanov")

	def test_two_equal_students(self):
		from django.test import Client
		client = Client()
		resp = Student.objects.create(
			name = "Ivan",surname = "Ivanov",
			address = "Ukraine, Lviv, Ivanova str.28",
			skype = 'ivanoviv',
			date_of_birth = '1988-01-01',   
			email = 'iv.ivanov@outlook.com',
			phone = '+380930010101')
		resp2 = Student.objects.create(
			name = "Ivan",surname = "Ivanov",
			address = "Ukraine, Lviv, Ivanova str.28",
			skype = 'ivanoviv',
			date_of_birth = '1988-01-01',   
			email = 'iv.ivanov@outlook.com',
			phone = '+380930010101')
		response = client.get('/students/1/')
		self.assertEqual(response.status_code, 200)

	def test_link_menu(self):
		resp = Student(name = "Ivan",)
		response = self.client.get('/students/', follow=True)
		self.assertContains(response, '/') 
		self.assertContains(response, '/students/') 
		self.assertContains(response, '/contact/') 
		self.assertContains(response, '/feedback/') 
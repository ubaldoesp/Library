from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from books.models import Book
from autors.models import Autor
from django.http import response 
# Create your tests here.

class BookTestCase(APITestCase):
    
    def setUp(self):
        self.host = 'http://127.0.0.1:8090'
        
        self.book = Book.objects.create(name='juegos del hambre',pages=10,published=True,
                                        publication_date='2020-01-18',edition=1)
        self.user = User.objects.create_user(username='user',password='password', is_staff=True)
        
        response = self.client.post(f'{self.host}/api/token',
                {'username':'user','password':'password'}, format="json"
        )
        
        assert response.status_code == 200, response.status_code
        self.token = response.data['access']
    
    # get Books
    def test_get_books(self):
        # response = self.client.get('https://127.0.0.1:8090/books/')
        response = self.client.get(f'{self.host}/books/',
                                    HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code,200, response.data)
        total_books = Book.objects.all().count()
        self.assertNotEqual(total_books,0)
        
        
    def test_create_book(self):
        autor= Autor.objects.create(
            name='Autor',
            age=21,
            date_of_birth='2021-01-01'
            )
        
        data={
            'name':'en llamas',
            'pages':10,
            'published':True,
            'publication_date':'2021-01-18',
            'edition':1,
            'autor':[autor.id]
             }
        response= self.client.post(f'{self.host}/books/',data=data,
                                   HTTP_AUTHORIZATION=f'Bearer {self.token}')
        # print('la data: ',response.data)
        self.assertEqual(response.status_code,201, response.data)
        total_books = Book.objects.all().count()
        self.assertNotEqual(total_books,0)
        
    def test_patch_patch(self):
        
        data={
            'name':'la brujula dorada'
        }
        response= self.client.patch(f'{self.host}/books/{self.book.id}/',data=data, 
                                    HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code,200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.name, data['name'])
        
    def test_delete_book(self):
        book = Book.objects.create(name='',pages=10,published=True,
                publication_date='2021-01-18',edition=1,user= self.user)
        
        response =self.client.delete(f'{self.host}/books/{book.id}/',
            HTTP_AUTHORIZATION=f'Bearer {self.token}')
        print(f'response:',response)
        self.assertEqual(response.status_code,204)
        total_books = Book.objects.filter(id=book.id).count()
        self.assertEqual(total_books,0)
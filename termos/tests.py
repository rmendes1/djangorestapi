from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from termos.serializers import Term1Serializer, Term2Serializer, Term3Serializer, Term4Serializer
from .models import Term1, Term2, Term3, Term4


def make_test_class(model_name, model, serializer_class, url_name_prefix):
    class TestClass(APITestCase):
        def setUp(self):
            self.data = {'title': 'titletest', 'block': {'foo': 'bar'}}
            self.term = model.objects.create(**self.data)
            self.serializer = serializer_class(instance=self.term)

        def test_create_term(self):
            url = reverse(f'{url_name_prefix}-list-create')
            response = self.client.post(url, data=self.data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(model.objects.count(), 2)
            self.assertEqual(model.objects.get(uuid=response.data['uuid']).block, self.data['block'])

        def test_list_terms(self):
            url = reverse(f'{url_name_prefix}-list-create')
            response = self.client.get(url, data=self.data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data[0]['block'], self.data['block'])

        def test_retrieve_term(self):
            url = reverse(f'{url_name_prefix}-retrieve-update-destroy', args=[str(self.term.uuid)])
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['title'], self.data['title'])
            self.assertEqual(response.data['block'], self.data['block'])

        def test_patch_term(self):
            self.new_data = {
                'block': {
                    'foo': 'bazzzz'
                }
            }
            url = reverse(f'{url_name_prefix}-retrieve-update-destroy', args=[str(self.term.uuid)])
            response = self.client.patch(url, self.new_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(model.objects.get(uuid=self.term.uuid).block, self.new_data['block'])

        def test_put_term(self):
            self.new_data = {
                'title': 'New title',
                'block': {
                    'foo': 'bazzzz'
                }
            }
            url = reverse(f'{url_name_prefix}-retrieve-update-destroy', args=[str(self.term.uuid)])
            response = self.client.put(url, self.new_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(model.objects.get(uuid=self.term.uuid).block, self.new_data['block'])

        def test_delete_term(self):
            url = reverse(f'{url_name_prefix}-retrieve-update-destroy', args=[str(self.term.uuid)])
            response = self.client.delete(url, self.data, format='json')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(model.objects.count(), 0)

    TestClass.__name__ = f'{model_name}TestClass'
    return TestClass


Term1TestClass = make_test_class(
    'Term1', Term1, Term1Serializer, 'term1'
)

Term2TestClass = make_test_class(
    'Term2', Term2, Term2Serializer, 'term2'
)

Term3TestClass = make_test_class(
    'Term3', Term3, Term3Serializer, 'term3'
)

Term4TestClass = make_test_class(
    'Term4', Term4, Term4Serializer, 'term4'
)


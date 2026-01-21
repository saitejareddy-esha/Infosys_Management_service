from rest_framework.test import APITestCase
from .models import Dataset

class MetadataTests(APITestCase):

    def test_create_dataset(self):
        response = self.client.post(
            '/api/datasets/',
            {
                'name': 'customer',
                'description': 'this customer data'
            },
            format='json' 
        )
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, 201)

    def test_add_data_element(self):
        dataset = Dataset.objects.create(name='customer')
        # print(dataset.id)
        response = self.client.post(
            f'/api/datasets/1/elements/',
            {
                'name': '19-06-1999',
                'data_type': 'string',
                'is_required': True
            },
            format='json'  
        )
        print(response.status_code, response.data)
        self.assertEqual(response.status_code, 201)

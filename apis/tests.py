from django.test import TestCase


class HomePageTests(TestCase):

    def test_status_code_correct(self):
        response = self.client.get('/apis/v1/weather?city=Cape+Town&period=2020-06-28%2C2020-07-02')
        self.assertEquals(response.status_code, 200)

    def test_status_code_incorrect(self):
        response = self.client.get('/apis/v1/weather?city=Cape+Town&period=asdasda28%2C2020-07-02')
        self.assertEquals(response.status_code, 400)

    def test_response_keys_correct(self):
        response = self.client.get('/apis/v1/weather?city=Cape+Town&period=2020-06-28%2C2020-07-02')
        self.assertEquals(list(response.json().keys()), ['2020-06-28', '2020-06-29', '2020-06-30', '2020-07-01', '2020-07-02'])

    def test_response_keys_incorrect(self):
        response = self.client.get('/apis/v1/weather?city=Cape+Town&period=2020-06-28%2C2020-07-02')
        self.assertNotEquals(list(response.json().keys()), ['sdfsdf', 'asdfas', 'asdfasdf', 'asdfasdf', 'asdfasd'])

    def test_data_correct(self):
        response = self.client.get('/apis/v1/weather?city=Cape+Town&period=2020-06-28%2C2020-07-02')
        self.assertEquals(type(response.json()['2020-06-28']['humidity']), float)

    def test_data_incorrect(self):
        response = self.client.get('/apis/v1/weather?city=Cape+Town&period=2020-06-28%2C2020-07-02')
        self.assertNotEquals(type(response.json()['2020-06-28']['humidity']), str)

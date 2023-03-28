from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        response=self.client.post(self.register_url)
        self.assertEqual(response.status_code,400)

    def test_user_cannot_register_correctly(self):
        response=self.client.post(self.register_url, self.data, format="json")
        self.assertEqual(response.status_code,201)

    
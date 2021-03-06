from django.test import TestCase

from wagtailaltgenerator import helpers


class GenerateLabelTest(TestCase):
    def test_generate(self):
        image_url = 'https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg'  # NOQA
        data = helpers.describe(image_url)

        self.assertTrue('description' in data)
        self.assertTrue('captions' in data['description'])
        self.assertTrue(len(data['description']['captions']) > 0)
        self.assertTrue('text' in data['description']['captions'][0])

from django.test import SimpleTestCase

class TestNearHundred(SimpleTestCase):
    def test_93(self):
        response = self.client.get("/warmup-1/near-hundred/93")
        self.assertContains(response, True)
    def test_90(self):
        response = self.client.get("/warmup-1/near-hundred/90")
        self.assertContains(response, True)
    def test_89(self):
        response = self.client.get("/warmup-1/near-hundred/89")
        self.assertContains(response, False)
class TestStringSplosion(SimpleTestCase):
    def test_Code(self):
        response = self.client.get("/warmup-2/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")
    def test_ab(self):
        response = self.client.get("/warmup-2/string-splosion/ab")
        self.assertContains(response, "aab")
    def test_abc(self):
        response = self.client.get("/warmup-2/string-splosion/abc")
        self.assertContains(response, "aababc")
class TestCatDog(SimpleTestCase):
    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/catdog")
        self.assertContains(response, True)
    def test_catcat(self):
        response = self.client.get("/string-2/cat-dog/catcat")
        self.assertContains(response, False)
    def test_cadodog(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog")
        self.assertContains(response, True)
class TestLoneSum(SimpleTestCase):
    def test_123(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3")
        self.assertContains(response, 6)
    def test_333(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3")
        self.assertContains(response, 0)
    def test_323(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3")
        self.assertContains(response, 2)
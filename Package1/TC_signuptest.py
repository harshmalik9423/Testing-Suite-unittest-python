import unittest

class SignUpTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is sign up by Email test")
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print("This is sign up by Facebook test")
        self.assertTrue(True)

    def test_signupbyTwitter(self):
        print("This is sign up by Twitter test")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

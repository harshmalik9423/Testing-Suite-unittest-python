import unittest
from Package1.TC_logintest import LoginTest
from Package1.TC_signuptest import SignUpTest
from Package2.TC_paymenttest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest


# Getting all test from every file
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating test suites
sanityTestSuite = unittest.TestSuite([tc1,tc2])
functionalTestSuite = unittest.TestSuite([tc3,tc4])
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])

# unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)
# unittest.TextTestRunner(verbosity=2).run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)

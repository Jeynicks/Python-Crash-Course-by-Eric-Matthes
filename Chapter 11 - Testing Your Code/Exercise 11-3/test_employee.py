"""1-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5,000 to the
annual salary by default but also accepts a different raise amount.
Write a test file for Employee with two test functions, test_give_default
_raise() and test_give_custom_raise(). Write your tests once without using a
fixture, and make sure they both pass. Then write a fixture so you don’t have to
create a new employee instance in each test function. Run the tests again, and
make sure both tests still pass."""
import pytest
from Employee import Employee  

@pytest.fixture
def new_employee():
    """Return an Employee instance for use in tests."""
    return Employee("Jeynicks", "Python", 3600)


def test_give_default_raise(new_employee):
    salary_raise = new_employee.give_raise()
    
    assert salary_raise == 8600
    
def test_give_custom_raise(new_employee):

    salary_raise = new_employee.give_raise(10000)
    
    assert salary_raise == 13600


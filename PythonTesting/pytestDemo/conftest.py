import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return  ["Mujeeb","Rahaman","mujeeb.rahaman@cognine.com"]


@pytest.fixture(params=[("chrome","Mujeeb","Rahaman"), ("firefox","Mujeeb"),("IE","Rahaman")])
def crossBrowser(request):
    return request.param
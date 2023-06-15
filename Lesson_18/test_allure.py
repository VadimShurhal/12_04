import allure


@allure.step('Check value')
def check_value(a, b):
    print(f'We check {a} and {b}')
    assert a == b


@allure.step('Check sum value')
def check_sum_value(a, b):
    print(f'We sum {a} and {b}')
    assert a + b == a + b


@allure.story('My first story')
class TestAllure:

    @allure.description('My test description test_1')
    @allure.title('Test assert #1')
    @allure.severity("Low")
    def test_1(self):
        check_value(2, 2)
        check_sum_value(11, 11)
        print('My first test')
        with allure.step("Finish check ...."):
            assert 1 == 1

    @allure.description('My test description test_1')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_2(self):
        print('My second test')
        assert 1 == 1

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('My test description test_1')
    def test_3(self):
        assert 1 == 1

    @allure.description('My test description test_1')
    @allure.title('Test assert #4')
    def test_4(self):
        assert 1 == 2

    @allure.description('My test description test_1')
    @allure.title('Test assert  #5')
    def test_5(self):
        assert 1 == 3

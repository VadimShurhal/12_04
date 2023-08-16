import allure


@allure.story('My first story')
class TestClass:

    @allure.description('My test description test_upper')
    @allure.title('Test assert #1')
    @allure.severity("Low")
    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    @allure.description('My test description test_isupper')
    @allure.title('Test assert #2')
    @allure.severity("Height")
    def test_isupper(self):
        assert 'FOO'.isupper()


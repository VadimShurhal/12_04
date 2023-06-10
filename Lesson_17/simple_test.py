# def test_fixture(db):
#     print('Test is run')


def test_fixture(generate_data):
    print(generate_data)
    print(f'Login - {generate_data[0]}')
    print(f'Password - {generate_data[1]}')

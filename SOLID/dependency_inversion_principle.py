import os


# class ApiClient:
#
#     def __init__(self) -> None:
#         self.api_key = os.getenv("API_KEY")
#         self.timeouy = int(os.getenv("TIMEOUT"))
#
#
# class Service:
#
#     def __init__(self) -> None:
#         self.api_client = ApiClient()
#
#
# def main() -> None:
#     service = Service()
#
#
# if __name__ == "__main__":
#     main()


###############################################


class ApiClient:

    def __init__(self, api_key: str, timeout: int):
        self.api_key = api_key
        self.timeout = timeout


class Service:

    def __init__(self, api_client: ApiClient):
        self.api_client = api_client


def main(service: Service):
    ...


if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_key=os.getenv("API_KEY"),
                timeout=int(os.getenv("TIMEOUT")),
            ),
        ),
    )



# class Human:
#
#     def __init__(self):
#         self.name = 'Joe'
#         self.age = 22


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age


API_KEY = os.getenv("API_KEY")
print(API_KEY)


import os

for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))
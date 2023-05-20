import argparse
import re


class UrlAnalyzer:

    def __new__(cls, *args, **kwargs):
        analyzer = super().__new__(cls)
        if not args and not kwargs:
            analyzer.url = cls.user_input
        return analyzer

    def __init__(self, url=None):
        if url:
            self.url = url
        self.link_analyzer = LinkAnalyzer(self.url)

    @staticmethod
    def user_input():
        parse = argparse.ArgumentParser()
        parse.add_argument('-url', type=str, help='Please se url for parsing')
        args = parse.parse_args()
        if args.url:
            return args.url
        else:
            url = input('Please set url for parsing')
            return url

    def info_from_link(self, url):
        self.link_analyzer.check_link(url)

    def get_links_from_url(self, url) -> list:
        return re.findall('', url)


class LinkAnalyzer:

    def __init__(self, url):
        self.url = url

    def check_link(self, link):
        pass

    def check_links(self, links):
        for link in links:
            self.check_link(link)


if __name__ == "__main__":
    url = UrlAnalyzer('www.google.com')
    url_1 = UrlAnalyzer()
    print(url_1)

# class A:
#
#     def __init__(self, name):
#         self.name = name
#
#
# a = A('Joe')
# print(a.name)
#
# a.name = "Marta"
#
# print(a.name)
#
# a.last_name = 'Tomas'
#
# print(a.last_name)

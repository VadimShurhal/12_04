from abc import ABC, abstractmethod

#after

# class Printer(ABC):
#
#     @abstractmethod
#     def print(self, document):
#         pass
#
#     @abstractmethod
#     def fax(self, document):
#         pass
#
#     @abstractmethod
#     def scan(self, document):
#         pass
#
#
# class ModernPrinter(Printer):
#
#     def print(self, document):
#         print(f'Printing {document} in color ...')
#
#     def fax(self, document):
#         print(f'Faxing {document} ...')
#
#     def scan(self, document):
#         print(f'Scanning {document} ...')
#
#
# class OldPrinter(Printer):
#
#     def print(self, document):
#         print(f'Printing {document} in black color ...')
#
#     def fax(self, document):
#         raise NotImplementedError('Fax not supported')
#
#     def scan(self, document):
#         raise NotImplementedError('Fax not supported')


#after

class Printer(ABC):

    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class OldPrinter(Printer):

    def print(self, document):
        print(f'Printing {document} in black color ...')


class NewPrinter(Printer, Fax, Scanner):

    def print(self, document):
        print(f'Printing {document} in color ...')

    def fax(self, document):
        print(f'Faxing {document} ...')

    def scan(self, document):
        print(f'Scanning {document} ...')
from reversedns import DNSReverser
from testes.teste import Teste, FalhouNoTeste
from testes.tester import Tester


class ReverseTester(Tester):

    def __init__(self):
        teste = Teste()
        self.testes = []
        self.set_tests()

    def set_tests(self):
        empty_file = DNSReverser()
        empty_file_test = Teste('', '', 'empty_file_test')
        self.testes.append(empty_file_test)

        reverser = DNSReverser('dns.txt')
        header_test = Teste(reverser.header(), '$TTL 3D\n\
@       IN      SOA     land-5.com. root.land-5.com. (\n\
                        199609206       ; serial, todays date + \
todays serial #\n\
                        8H              ; refresh, seconds\n\
                        2H              ; retry, seconds\n\
                        4W              ; expire, seconds\n\
                        1D )            ; minimum, seconds\n\n',
                            'header_test')
        self.testes.append(header_test)

        ns_test = Teste(reverser.ns(), '                NS      land-5.com.\n',
                        'ns_test')
        self.testes.append(ns_test)
        reverse_test = Teste(reverser.a(), '1               PTR     router\n\
2               PTR     land-5.com.\n\
3               PTR     ns\n\
192             PTR     www\n\
2               PTR     funn\n\
200             PTR     ws-177200\n\
201             PTR     ws-177201\n\
202             PTR     ws-177202\n\
203             PTR     ws-177203\n\
204             PTR     ws-177204\n\
205             PTR     ws-177205\n\
250             PTR     ws-177250\n\
251             PTR     ws-177251\n\
252             PTR     ws-177252\n\
253             PTR     ws-177253\n\
254             PTR     ws-177254\n', 'reverse_test')
        self.testes.append(reverse_test)


if __name__ == '__main__':
    tester = ReverseTester()
    tester.test()

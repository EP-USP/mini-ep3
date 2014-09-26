import re
import argparse


class DNSReverser(object):

    a_line = re.compile('(^[^\s]+)\s+A\s+(?:\d+\.){3}(\d+)')     # get A lines
    ns_line = re.compile('\s+NS\s+(?:ns)?(.*)$')        # get NS lines

    def __init__(self, text_file='', text=''):
        if not text_file == '':
            f = open(text_file, 'r')
            self.direct_dns = f.readlines()
            f.close()
        else:
            self.direct_dns = text.split('\n')

    # Copy reader from a DNS zone file named infile to a FILE type out_file
    def header(self):
        header = ''
        for line in self.direct_dns:
            if DNSReverser.ns_line.search(line):
                return header
            header += line
        return header

    # Copy NS lines from a DNS zone file named infile to a FILE type out_file
    def ns(self):
        ns = ''
        for line in self.direct_dns:
            if DNSReverser.ns_line.search(line):
                ns += line
        return ns

    def a(self, domain):
        a = ''
        for line in self.direct_dns:
            match = DNSReverser.a_line.search(line)
            if match:
                if match.group(1) == domain:
                    a += match.group(2).ljust(16) + \
                        'PTR'.ljust(8) + \
                        domain + \
                        '\n'
                else:
                    a += match.group(2).ljust(16) + \
                        'PTR'.ljust(8) + \
                        match.group(1) + '.' + \
                        domain + \
                        '\n'

        return a

    def reversed_domains(self):
        domains = self.ns()
        domain = DNSReverser.ns_line.search(domains).group(1)
        return self.a(domain)

    def reverse(self):
        reversed_text = ''
        reversed_text += self.header()
        reversed_text += self.reversed_domains()
        return reversed_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        help='Arquivo de zona DNS',
                        default='dns.txt')
    parser.add_argument('-o', '--output',
                        help='Arquivo de saida para DNS reverso',
                        default='reversed_dns.txt')
    parser.add_argument('-p', '--print',
                        dest='p',
                        action='store_true',
                        default=False,
                        help='Print no console (default: escreve no arquivo)')

    args = parser.parse_args()
    reverser = DNSReverser(args.file)
    rev = reverser.reverse()
    if args.p:
        print(rev)
    else:
        f = open(args.output, 'w')
        f.write(rev)
        f.close()

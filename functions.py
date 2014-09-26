import re


class DNSReverser(object):

    a_line = re.compile('\s+A\s+')      # get A lines
    ip_pattern = re.compile('(\d+\.){3}\d+')        # get IPs from A lines
    domain_pattern = re.compile('(^[^\s]+)\s+A\s+((\d+\.){3}\d+)')
    # get domain from A lines
    ns_line = re.compile('\s+NS\s+')        # get NS lines

    def __init__(self, text='', text_file=''):
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

    def a(self):
        for line in self.direct_dns:
            match = DNSReverser.domain_pattern.search(line)
            if match:
                print(match.group(1)+'\t'+match.group(2))
        return ''

    def reverse(self):
        reversed_text = ''
        reversed_text += self.header()
        reversed_text += self.ns()
        reversed_text += self.a()
        return reversed_text


if __name__ == '__main__':
    reverser = DNSReverser(text_file='dns.txt')
    print(reverser.reverse())

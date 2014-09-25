import re

# Copy reader from a DNS zone file named infile to a FILE type out_file
def copy_header(infile, out_file):
    in_file = open(infile, 'r')
    ns_line = re.compile('\s+NS\s+')
    for line in in_file:
        if ns_line.search(line):
            in_file.close()
            return
        out_file.write(line)
    in_file.close()

# Copy NS lines from a DNS zone file named infile to a FILE type out_file
def copy_ns(infile, out_file):
    in_file = open(infile, 'r')
    ns_line = re.compile('\s+NS\s+')
    for line in in_file:
        if ns_line.search(line):
            out_file.write(line)
    in_file.close()

# Script starts here
out_file = open('reverse_dns.txt', 'w')

a_line = re.compile('\s+A\s+') # get A lines
ip_pattern = re.compile('(\d+\.){3}\d+') # get IPs from A lines
domain_pattern = re.compile('^[^\s]+') # get domain from A lines

copy_header('dns.txt', out_file)
copy_ns('dns.txt', out_file)

# Gets domain and ip from A lines (better turn it into a function)
in_file = open('dns.txt', 'r')
for line in in_file:
    if a_line.search(line):
        domain = domain_pattern.search(line)
        ip = ip_pattern.search(line)
        
        print(domain.group(), end=' ')
        print(ip.group())
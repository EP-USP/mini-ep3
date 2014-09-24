in_file = open('dns.txt', 'r')
out_file = open('reverse_dns.txt', 'w')

def is_ns(line):
	return line.find('NS')

def ns_position(in_file):
	line_num = 0
	for line in in_file:
		line_num++
		match = line.find('NS')
		if match:
			return line_num
	return -1

def copy_header(in_file, out_file):
    out_file.writelines(line for line in in_file while not is_ns(line))

def copy_ns(in_file, out_file):
	for line in in_file:
		if is_ns(line):
			out_file.writelines(line)
import sys
import os
import pdf2md

def main():
	argv = sys.argv
	if len(argv) > 1:
		filename = argv[1]
		title = os.path.splitext(os.path.basename(filename))[0]
		if not print_result():
			print 'Parsing', filename
	else:
		print 'usage:'
		print '    python main.py <pdf>'
		return

	parser = pdf2md.Parser(filename)
	parser.extract()
	piles = parser.parse()

	syntax = pdf2md.UrbanSyntax()

	writer = pdf2md.Writer()
	writer.set_syntax(syntax)
	writer.set_mode('simple')
	writer.set_title(title)
	if print_result():
		writer.write(piles, True)
		return
	else:
		writer.write(piles, False)
	print 'Your markdown is at', writer.get_location()

def print_result():
	argv = sys.argv
	return (len(argv) > 2 and int(argv[2]) > 0)

if __name__ == '__main__':
	main()


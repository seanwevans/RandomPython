#!/usr/bin/env python

"""
makeenv.py: Makes envelopes from Excel spreadsheet.

usage:
python makeenv.py [spreadsheet.xlsx] [-pdf]
"""

from os import system
from sys import argv
import xlrd

class Envelopes(object):
	def __init__(self, source, sheet, rows, cols, dims):
		self.source = source
		self.sheet = int(sheet) - 1
		self.rows = (self.start, self.end) = rows
		self.cols = (self.name, self.street, self.city, self.country) = self.convertCols(cols)
		self.dims = (self.height, self.width, self.margin) = dims
		try:
			self.book = xlrd.open_workbook(self.source)
		except:	
			print("Failed to open Excel spreadsheet. Exiting...")
			exit()
		self.tex = self.generate_TeX_Source()
		
	def convertCols(self, columnTuple):
		"""	Converts tuple of chars ('A','B','D') into tuple of array indexes (0,1,3). 
		only supports columns A-Z. 	"""
		
		o = []
		for col in columnTuple:
			o.append(ord(col.upper())-65)
		return tuple(o)
		
	def sanitize(self, unwashed_string):
		"""	Converts raw text to TeX friendly formatting. """
		s = unwashed_string
		ss = unwashed_string.split(' ')
		
		# add escape to special characters
		for c in ['#','&']:
			if c in s:
				s = s.replace(c, '\\'+c)
				
		# detect numbers within address and format correctly
		if ss[0].isdigit() or (ss[0].split('-'))[0].isdigit():
			
			for w in ss:
				if w !='' and w[0].isdigit():				
					if w[-2:] in ['st', 'nd', 'rd', 'th']:
						s = s.replace(w, '$'+w[:-2]+'^{'+w[-2:]+'}$')
			
		return s.lstrip()
	
	def generate_TeX_Source(self):
		"""	Generates a long string representing TeX source code. """
		
		head ="""\\documentclass{article}

		\\usepackage[paperheight="""+str(self.height)+"in,paperwidth="+str(self.width)+"in,margin="+str(self.margin)+"""in]{geometry}
		\\pagenumbering{gobble}

		\\begin{document}
			
		\\begin{center}
		\\begin{Huge}

		"""

		tail ="""\\end{Huge}
		\\end{center}
			
		\\end{document}"""

		body = ""
		
		sheet = self.book.sheet_by_index(self.sheet)

		for i in range(self.start-1, self.end):

			r = sheet.row_values(i)
			
			if (r[self.street] != '?'):
				name = self.sanitize(r[self.name]) + "\\\\"
				street = self.sanitize(r[self.street]) + "\\\\"
				city = self.sanitize(r[self.city]) + "\\\\"
				country = self.sanitize(r[self.country])
				
				body += "\\vspace*{\\fill}\n"
				body += name + "\n"
				body += street + "\n"
				body += city + "\n"
				if country != "United States":	body += country + "\n"
				body += "\\vspace{\\fill}\n\n"
				body += "\\clearpage\n\n"
			
		tex = head + body + tail
		return(tex)
		
	def generate_TeX(self, output_filename):
		""" Generates a .tex file with the contents of self.tex """
		try:
			with open(output_filename+".tex",'w') as g:			
				g.write(self.tex)
			return True
		except:
			return False

	def generate_PDF(self, pdf_filename):
		""" Generates a pdf.
		note: only works if texify.exe is present. """
		if(self.generate_TeX(pdf_filename)):
			try:
				command = "texify " + pdf_filename + ".tex --pdf > $null"	# Windows 10 with MikTeX
				system(command)
				print(pdf_filename + ".pdf created successfully.")
				return True
			except:
				print(pdf_filename + ".pdf NOT created.")
				return False
				
if __name__ == "__main__":
	
	# Default Values
	path = "marry.xlsx"			# The spreadsheet with names and addresses
	sheet = 2					# The second sheet of path.xlsx	
	rows = (5, 129)				# The range of rows in which the name and addresses are contained
	cols = ('B','E','F','G')	# The columns in which the name and addresses are contained
	dims = (5.25, 7.25, 1)		# The physical dimensions of the envelope in inches (height, width, margin)
	output_filename = "envelopes"
	
	for arg in argv:
		if ".xlsx" in arg:	path = arg
			
	env = Envelopes(path, sheet, rows, cols, dims)
	
	for arg in argv:
		if ".pdf" in arg:	env.generate_PDF(arg[:-4])			# generates .tex and .pdf
		if ".tex" in arg:	env.generate_TeX(arg[:-4])			# generates just .tex
		if arg == "-out":	print(env.generate_TeX_Source())	# prints .tex source
from random import randint
from fractions import Fraction

head = """\\documentclass[a4paper, 11pt]{article}

\\usepackage[margin=1.0in]{geometry}
\\usepackage{fancyhdr}

\\pagestyle{fancy}
\\pagenumbering{gobble}

\\lhead{Adding Fractions}
\\chead{Name:}
\\rhead{Date:}

\\begin{document}
"""

body = ""

tail = """

\\end{document}
"""

s = []

num_prob = 100
max_den = 100
answers = True

for i in range(num_prob):
	d1 = randint(2, max_den)
	d2 = randint(2, max_den)
	n1 = randint(1, d1-1)
	n2 = randint(1, d2-1)
	sd1 = str(d1)
	sd2 = str(d2)
	sn1 = str(n1)
	sn2 = str(n2)
	si = str(i+1)
	
	s.append(Fraction(n1,d1) + Fraction(n2,d2))
	
	body += """
	\\noindent{} {\Large \\textbf{"""+si+""")}} \hspace{1cm} $ \\displaystyle{}\\frac{"""+sn1+"""}{"""+sd1+"""} + \\frac{"""+sn2+"""}{"""+sd2+"""} $
	\\vspace{5.5cm}
	"""

if answers:
	body += """
	\\clearpage

	\\section*{Answers}
	
	"""

	for i in range(num_prob):
		sa = str(s[i])
		body += "\\noindent{} \\textbf{" + str(i+1) + ") } " + sa + " \\\\ "
	
with open('py.tex', 'w') as f:
	f.writelines([head, body, tail])
	
import os

langs = ["ar", "en", "de", "fr", "ru", "it", "es"]



for l in langs:
	text = open(l + "_technology_wiki_glossary.csv").read()
	lines = text.split("\n")
	count_tot = 0
	term_tot = 0
	def_tot = 0
	for line in lines:
		try:
			term = line.split(",")[0]
			defin = line.split(",")[1]

			len_term = len(term.split())
			len_def = len(defin.split())

			term_tot += len_term
			def_tot += len_def
			count_tot += 1

		except:
			print ("ERROR with:")
			print (line.split(","))

	print ("Language", l)
	print ("Total entries:", count_tot)
	print ("Total Terms Words:", term_tot)
	print ("Total Defs  Words:", def_tot)
	print ("Avg Terms Words:", round(term_tot/count_tot, 2))
	print ("Avg Defs  Words:", round(def_tot/count_tot, 2))
	print ()
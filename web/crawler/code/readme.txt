please run this module with terminal: $ python crawl.py 'http://www.cs.columbia.edu/~jikk/index.html' 2

expected result:
Title:  Kangkook Jee - Research home 	URL:  http://www.cs.columbia.edu/~jikk/index.html
Title:  NSL: Network Security Lab at Columbia University 	URL:  http://nsl.cs.columbia.edu
Title:  Department of Computer Science, Columbia University | Home 	URL:  http://www.cs.columbia.edu
Title:  Columbia University in the City of New York 	URL:  http://www.columbia.edu
Title:  Prof. Angelos Keromytis' Home Page 	URL:  http://www.cs.columbia.edu/~angelos
Title:  Free CSS Templates - Download free CSS templates 	URL:  http://www.freecsstemplates.org/


$ python titletest.py 'http://www.cs.columbia.edu/~jikk/index.html' 1

Title:  Kangkook Jee - Research home 	URL:  http://www.cs.columbia.edu/~jikk/index.html
 Check the correctness of this Title:
  is_alpha(TITLE[i]) and TITLE[i].isalpha(): 
   False False
  is_alnum(TITLE[i]) and TITLE[i].isalnum(): 
   False False
  startswith(TITLE[i],TITLE[i]) and TITLE[i].startswith(TITLE[i]):
   True True
  is_in(TITLE[i],TITLE[i]) and TITLE[i] in TITLE[i]
   True True

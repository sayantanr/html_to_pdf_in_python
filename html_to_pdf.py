import pdfkit #pip install pdfkit in cmd or bash
pdfkit.from_url('https://www.google.co.in/','sanu.pdf') #take website as input and make it a pdf
pdfkit.from_string('sayantan','GfG.pdf') #make text as input and make it as pdf
pdfkit.from_url(['google.com', 'geeksforgeeks.org', 'facebook.com'], 'sayantan.pdf')#take  multiple url and make it one pdf
pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf') #we can take multiple html file and make it pdf







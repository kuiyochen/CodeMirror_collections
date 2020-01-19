import sys
import cgi
parameter = cgi.FieldStorage()
print(parameter)
text = parameter.getvalue('name')
print(text)
# text = "123456"
f = open("123.txt","w")
f.write(text)
f.close()
print("YOOOOOOOO")
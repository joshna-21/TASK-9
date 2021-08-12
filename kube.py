#!/usr/bin/python3

import subprocess as sp
import cgi

print("content-type: text/html")
print()

y = cgi.FieldStorage()
x = y.getvalue("X")
	
z=s.getoutput("sudo "+"kubectl "+x+" --kubeconfig /root/kubetask9/admin.conf")
        
print(z)
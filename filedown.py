import requests, re, random, time, os, string, re
from tqdm import tqdm
from rich.console import Console as con

colours = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white', 'grey0', 'navy_blue', 'dark_blue', 'blue3', 'blue1', 'dark_green', 'deep_sky_blue4', 'dodger_blue3', 'dodger_blue2', 'green4', 'spring_green4', 'turquoise4', 'deep_sky_blue3', 'dodger_blue1', 'dark_cyan', 'light_sea_green', 'deep_sky_blue2', 'deep_sky_blue1', 'green3', 'spring_green3', 'cyan3', 'dark_turquoise', 'turquoise2', 'green1', 'spring_green2', 'spring_green1', 'medium_spring_green', 'cyan2', 'cyan1', 'purple4', 'purple3', 'blue_violet', 'grey37', 'medium_purple4', 'slate_blue3', 'royal_blue1', 'chartreuse4', 'pale_turquoise4', 'steel_blue', 'steel_blue3', 'cornflower_blue', 'dark_sea_green4', 'cadet_blue', 'sky_blue3', 'chartreuse3', 'sea_green3', 'aquamarine3', 'medium_turquoise', 'steel_blue1', 'sea_green2', 'sea_green1', 'dark_slate_gray2', 'dark_red', 'dark_magenta', 'orange4', 'light_pink4', 'plum4', 'medium_purple3', 'slate_blue1', 'wheat4', 'grey53', 'light_slate_grey', 'medium_purple', 'light_slate_blue', 'yellow4', 'dark_sea_green', 'light_sky_blue3', 'sky_blue2', 'chartreuse2', 'pale_green3', 'dark_slate_gray3', 'sky_blue1', 'chartreuse1', 'light_green', 'aquamarine1', 'dark_slate_gray1', 'deep_pink4', 'medium_violet_red', 'dark_violet', 'purple', 'medium_orchid3', 'medium_orchid', 'dark_goldenrod', 'rosy_brown', 'grey63', 'medium_purple2', 'medium_purple1', 'dark_khaki', 'navajo_white3', 'grey69', 'light_steel_blue3', 'light_steel_blue', 'dark_olive_green3', 'dark_sea_green3', 'light_cyan3', 'light_sky_blue1', 'green_yellow', 'dark_olive_green2', 'pale_green1', 'dark_sea_green2', 'pale_turquoise1', 'red3', 'deep_pink3', 'magenta3', 'dark_orange3', 'indian_red', 'hot_pink3', 'hot_pink2', 'orchid', 'orange3', 'light_salmon3', 'light_pink3', 'pink3', 'plum3', 'violet', 'gold3', 'light_goldenrod3', 'tan', 'misty_rose3', 'thistle3', 'plum2', 'yellow3', 'khaki3', 'light_yellow3', 'grey84', 'light_steel_blue1', 'yellow2', 'dark_olive_green1', 'dark_sea_green1', 'honeydew2', 'light_cyan1', 'red1', 'deep_pink2', 'deep_pink1', 'magenta2', 'magenta1', 'orange_red1', 'indian_red1', 'hot_pink', 'medium_orchid1', 'dark_orange', 'salmon1', 'light_coral', 'pale_violet_red1', 'orchid2', 'orchid1', 'orange1', 'sandy_brown', 'light_salmon1', 'light_pink1', 'pink1', 'plum1', 'gold1', 'light_goldenrod2', 'navajo_white1', 'misty_rose1', 'thistle1', 'yellow1', 'light_goldenrod1', 'khaki1', 'wheat1', 'cornsilk1', 'grey100', 'grey3', 'grey7', 'grey11', 'grey15', 'grey19', 'grey23', 'grey27', 'grey30', 'grey35', 'grey39', 'grey42', 'grey46', 'grey50', 'grey54', 'grey58', 'grey62', 'grey66', 'grey70', 'grey74', 'grey78', 'grey82', 'grey85', 'grey89', 'grey93']

def animated_print(text, delay):
	colour = random.choice(colours)
	for char in text:
		if char == ' ':
			con().print(char, end='', style="none", overflow="ignore")
		else:
			con().print(char, end='', style=colour, overflow="ignore")
			time.sleep(delay)
	con().print()

logo = r"""
                   ||`                             .|';
                   ||                              ||    ''
               .|''||  .|''|, '\\    //` `||''|,  '||'   ||  .|''|,
               ||  ||  ||  ||   \\/\//    ||  ||   ||    ||  ||..||
               `|..||. `|..|'    \/\/    .||  ||. .||.  .||. `|...
"""
line = """----------------------------------------------------------------------------------------"""
os.system("clear")
animated_print(logo, 0.001)
animated_print(line, 0.001)

urls = []
dic = {}

url1 = input("☆ url > ")
while True:
	try:
		host = re.findall('//(.*?)/', url1)[0]
		headers = {
    'Host': host,
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
		hh = requests.get(url1, headers=headers, verify=False, timeout=20)
		if  hh.status_code == 200:
			break
		else:
			pass
	except:
		pass

def get_urls():
	matches = re.findall('href="(.*?)"', hh.text)
	for i in matches:
		for a in ['.jpeg', '.jpg', '.pnj', '.mp4']:
			if a in i:
				urls.append(i)
				name = "".join(random.choices(string.ascii_letters, k=10))
				dic[i] = f'{name}{a}'


def download():
	for url in urls:
		filename = dic.get(url)
		while True:
			try:
				headers = {
    'Host': host,
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': url1,
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

				file = requests.get(f'{url1}{url}', headers=headers, verify=False)
				if file.status_code == 200:
					break
				elif file.status_code == 502:
					message = "☆ Server is Down :("
					animated_print(message, 0.001)
					os._exit(0)
			except requests.exceptions.RequestException:
				pass
		file_size = int(file.headers.get('Content-Length', 0))
		progress = tqdm(file.iter_content(1024), f'Downloading {filename}', total=file_size, unit='B', unit_scale=True, unit_divisor=1024)
		with open(f"hacked/{filename}", 'wb') as f:
			for data in progress.iterable:
				f.write(data)
				progress.update(len(data))
		message = "☆ File {k} is saved successfully"
		animated_print(message, 0.001)
		animated_print(line, 0.001)

get_urls()
download()
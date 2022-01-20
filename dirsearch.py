import requests
import os
import sys
from threading import Thread

url,wordlist,ext = "","",""
args = sys.argv
help_message = '''
Shybert dirseach create:
USAGE > python3 pydir.py -u [URL] -w [WORDLIST PATH] -e (Not Obligatory) [EXTENSION]
EXAMPLE > python3 pydir.py -u https:// www .web .com/ -w /home/user/Desktop/wordlists/dict.txt -e php
▼ ARGS ▼
-h || --help 	 | Usage of the script
-u || --url  	 | URL 
-w || --wordlist | Your wordlist path
-e || --extension| php,html,txt ...
'''
def search_url(url,wordlist,ext):
	print(f"Target: {url}")
	with open(wordlist) as w:
		dirs = w.readlines()

		for i in dirs:
			d = i.replace("\n","")
			if ext:
				if url[-1] == "/":

					r_get = requests.get(f"{url}{d}.{ext}")
					r_post = requests.post(f"{url}{d}.{ext}")

					if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
						print(f"\nFOUND GET - {url}{d}.{ext} - {r_get.status_code}")
					elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
						print(f"\nFOUND POST - {url}{d}.{ext} - {r_post.status_code}")	
				elif url[-1] != "/":
					r_get = requests.get(f"{url}/{d}.{ext}")
					r_post = requests.post(f"{url}/{d}.{ext}")

					if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
						print(f"\nFOUND GET - {url}{d}.{ext} - {r_get.status_code}")
					elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
						print(f"\nFOUND POST - {url}{d}.{ext} - {r_post.status_code}")
			elif not ext:
				if url[-1] == "/":
					r_get = requests.get(f"{url}{d}/")
					r_post = requests.post(f"{url}{d}/")
					print(f'{url}{d}')
					if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
						print(f"\nFOUND GET - {url}{d}.{ext} - {r_get.status_code}")
					elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
						print(f"\nFOUND POST - {url}{d}.{ext} - {r_post.status_code}")	
				elif url[-1] != "/":
					r_get = requests.get(f"{url}/{d}")
					r_post = requests.post(f"{url}/{d}")

					if r_get.status_code == 200 or r_get.status_code == 301 or r_get.status_code == 403:
						print(f"\nFOUND GET - {url}{d} - {r_get.status_code}")
					elif r_post.status_code == 200 or r_post.status_code == 301 or r_post.status_code == 403:
						print(f"\nFOUND POST - {url}{d} - {r_post.status_code}")

def main(url,wordlist,ext):
	try:
		if len(args) == 1:
			print(help_message)
	
		elif args[1] == '-h' or args[1] == '--help':
			print(help_message)
		
		elif args[1] == '-u' or args[1] == '--url':
			url = str(args[2])
			
			if args[3] == '-w' or args[3] == '--wordlist':
				wordlist = str(args[4])

				if len(args) >= 7:
					if args[5] == '-e' or args[5] == '-extension':
						ext = str(args[6])
		
					else:
						print(f'{help_message}Sintax Error!')
						return
				else:
					pass
	
			else:
				print(f'{help_message}Sintax Error!')
				return

		else:
			print(f'{help_message}Sintax Error!')
			return
	
	except:
		print(f'{help_message}Sintax Error!')
		return
		
	if url != '' and wordlist != '':
		'''
		for i in range(2):
			th = Thread(target=search_url, args=(url,wordlist,ext))
			th.start()
		'''
		search_url(url, wordlist, ext)
main(url,wordlist,ext)
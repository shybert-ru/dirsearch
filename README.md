# dirsearch v0.0.1
dirsearch is a tool used to brute-force directories and files in web sites.

## Usage

```console
root@shybert:~# python3 pydir.py -u <URL> -w <WORDLIST> -e [EXTENSION]
```
```
-h     --help          Show this help message and exit
-u     --url           Target URL 
-w     --wordlist      Wordlist file path
-e     --extensions    File extension(s) to search for
```

## Examples
```console
root@shybert:~# python3 pydir.py -u https://www.google.com/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e php,html
root@shybert:~# python3 pydir.py -u https://www.google.com/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

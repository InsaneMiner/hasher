# hasher
Hacher tests hashes like hashcat.<br>
Hasher only supports utf-8 encoding types on files.<br>
Hasher only supports md5 and sha1.<br>
There is a list of 10 million passwords in the repo and a big list of english words.<br>
you can use rockyou.txt but please convert it to utf-8
with this command:<br>
`iconv -f ISO-8859-1 -t UTF-8 rockyou.txt > rockyou_utf8.txt`

----------------------------------------------------------------------------
### how to use
`python3 hasher.py wordlist.txt hashes.txt sha1 outputfile.csv`<br>
or <br>
`python3 hasher.py wordlist.txt hashes.txt md5 outputfile.csv`

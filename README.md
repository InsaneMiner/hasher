# hasher
Hasher is a project that i have been working on it tests hashes like hashcat
Hasher only supports utf-8 encoding types on files.
Hasher only supports md5 and sha1.
There is a list of 10 million passwords in the repo and a big list of english words.
you can use rockyou.txt but please convert it to utf-8
with this command:
iconv -f ISO-8859-1 -t UTF-8 rockyou.txt > rockyou_utf8.txt

----------------------------------------------------------------------------
how to use:
python3 hasher wordlist.txt hashes.txt sha1 outputfile.csv
or 
python3 hasher wordlist.txt hashes.txt md5 outputfile.csv

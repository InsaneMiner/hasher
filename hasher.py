import hashlib
import sys
import libs.colours as colours
import re
cracked = []
csv_data = []
encoding_types = ["kio8_u","utf-8","utf-16","ascii","utf-7"]
supported_hashes =["sha1","md5"]
def error(error,w):
    global cracked
    if w:
        print(colours.colors.fg.lightred+error+colours.colors.reset)
        exit();
    else:
        cracked.append(colours.colors.fg.lightred+error+colours.colors.reset)
def hasher_main(flags):
    global res
    global cracked
    hasher(flags[1],flags[2],flags[3])
    print(colours.colors.bold+"\nOUTPUT:\n"+colours.colors.reset)
    res = []
    for i in cracked: 
        if i not in res:
            res.append(i)
    if len(flags) == 5:
        with open(flags[4],"w") as cj:
            cj.write("")
        with open(flags[4],"a+") as cf:
            if len(res) > 0:
                for at in range(len(csv_data)):
                    cf.write(csv_data[at])
                for ai in range(len(res)):
                    print(res[ai])
            else:
                print("No cracked hashes")
    else:
        if len(res) > 0:
            for ai in range(len(res)):
                print(res[ai])
        else:
            print("No cracked hashes")
def hash_object(hash_type,string):
    if hash_type == "sha1":
        hash_object = hashlib.sha1(bytes(string,"utf-8"))
        return hash_object.hexdigest()
    elif hash_type == "md5":
        hash_object = hashlib.md5(bytes(string,"utf-8"))
        return hash_object.hexdigest()
    else:
        return "no hash"
def md5(data):
    valid = re.findall(r"([a-fA-F\d]{32})", data)
    if len(valid) == 0:
        return False
    else:
        if valid[0] == data:
            return True
        else:
            return False
def sha1(data):
    valid = re.findall(r"([a-fA-F\d]{40})", data)
    if len(valid) == 0:
        return False
    else:
        if valid[0] == data:
            return True
        else:
            return False
def compare_hash(file,_hashes,hash_type,i):
    global cracked
    with open(file,encoding="utf-8") as fp:
        for cnt, line in enumerate(fp):
            current_hash = hash_object(hash_type,line.strip())
            if current_hash == _hashes[i].lower():
                print (colours.colors.fg.lightblue+ "[!] Cracked hash : "+current_hash+" Hash is: "+line.strip()+colours.colors.reset)
                cracked.append(colours.colors.fg.lightblue+ "[!] Cracked hash : "+current_hash+" Hash is: "+line.strip()+colours.colors.reset+"\n")
                csv_data.append(current_hash+","+line.strip()+"\n")
                break
            else:
                print(colours.colors.fg.lightgreen+"[X] Hash: "+current_hash+" "+" Tried: "+line.strip()+colours.colors.reset)
def hasher(file,hashes,hash_type):
    global cracked
    global supported_hashes
    if hash_type in supported_hashes:
        pass
    else:
        print("Hash type not supported")
        exit()
    try:
        with open(hashes,"r",encoding="utf-8") as h:
            _hashes = h.read()
    except FileNotFoundError:
        error("[*] File "+hashes+ " not found",True)
    except Exception as e:
        try:
            with open(hashes,"r",encoding="koi8_u") as h:
                _hashes = h.read()
        except:
            try:
                with open(hashes,"r",encoding="utf_7") as h:
                    _hashes = h.read()
            except:
                try:
                    with open(hashes,"r",encoding="utf_16") as h:
                        _hashes = h.read()
                except:
                    error("[*] Error occured when trying to read file "+hashes,True)
    _hashes = _hashes.replace(" ","")
    _hashes = _hashes.split("\n")
    _hashes.remove("")
    try:
        for i in range(len(_hashes)):
            if hash_type == "md5":
                if md5(_hashes[i]) == True:
                    compare_hash(file,_hashes,hash_type,i)
                else:
                    error("[*] Not valid md5 hash: "+_hashes[i],False)
            elif hash_type == "sha1":
                if sha1(_hashes[i]) == True:
                    compare_hash(file,_hashes,hash_type,i)
                else:
                    error("[*] Not valid sha1 hash: "+_hashes[i],False)
        cracked.append(str(i))
    except KeyboardInterrupt:
        error("Shutting Down^",True)
if len(sys.argv) < 4:
    print("python3 hasher.py wordlist.txt hashlist.txt")
    exit()
else:
    hasher_main(sys.argv)

import reverse_cipher
import rot_cipher
import ss_cipher
import transposition_cipher
import os
import sys

file = input("Textfile name: ")

if not os.path.exists(file):
    sys.exit("File path does not exist")

encryptiontype = input("Encryption method(transposition, simple substitution, reverse, caesar): ")
f = open(file, 'r')
content = f.read()
f.close()
ofile_name = input("Give output file name(with extension): ")
outfile = open(ofile_name, 'w')
global output
if "transposition" in encryptiontype.lower():
    key = input("Key for transposition cipher: ")
    output = transposition_cipher.encrypt(key, content)

elif 'simple' in encryptiontype.lower() or 'substitution' in encryptiontype.lower():
    output, key = ss_cipher.encrypt(content)
    print(f"Simple substitution key: {key}")

elif 'reverse' in encryptiontype.lower():
    output = reverse_cipher.encrypt(content)

elif 'caesar' in encryptiontype.lower():
    rot = input("ROT key for caesar cipher: ")
    output = rot_cipher.encrypt(content, rot)

outfile.write(output)
outfile.close()
print(f"Encryption done. Output file saved as {ofile_name}")
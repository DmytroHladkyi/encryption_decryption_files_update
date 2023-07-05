import pyAesCrypt

password = input("Podaj hasło: ")


pyAesCrypt.encryptFile(infile, outfile, password)

pyAesCrypt.decryptFile(infile, outfile, password)
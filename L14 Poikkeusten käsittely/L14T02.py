# Tee ohjelma, jolla yrität lukea Windows-koneella kaikki tiedostot kovalevyn C:n juuresta 
# (macOS/Linux/Unix- koneilla yritä lukea käyttäjän juurihakemisto). Näytä tiedostot konsolilla. 
# Koeta sen jälkeen lisätä tiedosto 'ayho.txt' C:n juureen (macOS/Linux/Unix -koneilla käyttäjän juurihakemistoon).
# Mitä tapahtui? Korjaa ohjelma niin, ettei se kaadu.
# Tekijä: Teppo Lappalainen

import os
ROOT_DIR = os.path.abspath(os.curdir)
print(ROOT_DIR)


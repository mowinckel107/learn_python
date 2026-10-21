



# Vi skal bruge funktioner fra "sys.pyi" og "os.pyi" (.pyi betyder "python interne filer")
# Disse er automatisk installeret med python
import sys
import os


# Husk! Hvis du laver noget om. Så gem og kør dit program tit for at sikre dig at det stadig virker
# Små skridt af gangen
"""

Make video of them my politician  email finder


Talk to teacher BEFORE presentation:
  Can I just tell the kids to make groups of 2 or 3 people or
  do we need to make the groups in some way?


teaching plan so far:
intro of me
plan for what we are doing today
  double clicking on an icon is the same as running
  python on everyones PC
  tell them what a comment is
  tell them what variables are
  tell them what functions are
  get them to run the example for variables and functions
  get them to run the other example on their own

  group them up 2 and 2 or 3 and 3

  give them a task 
  
"""

# Dette er hoved-funktionen. Den tager 0 argumenter og returnerer ingenting
# HELE den her python fil er kun et funktions-kald nederst i programmet
# Dette er gjort så man kan læse koden ovenfra og ned og forstå den
# Du kan finde ud af mere ved at søge "python forward declaration" på internettet
def kør_Historieskriveren():

  # En funktion der tager 0 argumenter og returnere ingenting
  skriv_titlen_hvis_der_er_en()

  # En funktion der tager 0 argumenter og returnere en "str"
  brugerens_navn : str = læs_brugerens_navn_fra_filen()

  print("Hej " + brugerens_navn + ", velkommen til din historie")

  # Nogle funktioner der tager 0 argumenter og returnerer en "str"
  
  navneord_flertal : str = få_navneord_flertal_fra_brugere()
  en_slags_person : str = få_en_slags_person_fra_brugere()
  en_tillægsord_følelse : str = få_tillægsord_følelse_fra_brugere()
  et_sted : str = få_et_sted_fra_brugere()
  et_navneord : str = få_et_navneord_fra_brugere()
  et_tillægsord : str = få_et_tillægsord_fra_brugere()
  et_væsen : str = få_et_væsen_fra_brugere()
  et_udsagnsord : str = få_et_udsagnsord_fra_brugere()
  




  # En funktion der tager mange argumenter, alle af typen "str" og returnerer ingenting
  skriv_historien(et_væsen, et_navneord, en_tillægsord_følelse, et_sted, et_tillægsord, en_slags_person, navneord_flertal, et_udsagnsord, brugerens_navn)

  stop_programmet_fra_at_lukke()
  # Når du har læst den her funktion, kan du undersøge hvordan de enkelte funktioner virker! :D
  # Lav ting om og kør programmet efter hver ændring. :D





# En funktion der tager 0 argumenter og returnerer ingenting
def skriv_titlen_hvis_der_er_en():
  historiens_titel : str = få_historie_titlen_fra_programmets_argumenter()

  # En bool er en påstand der er sand eller falsk
  # Vi bruger den her til at finde ud af om brugeren har givet os en titel
  der_er_en_titel : bool = historiens_titel != ""

  # Hvis der er en titel
  if(der_er_en_titel):
    print("Velkommen til "+ historiens_titel)

  # Hvis du ikke har lavet om i programmet, så er der ikke nogen titel.
  # Hvis du VIL give den en titel, så åbn .bat filen og skriv titlen (1 ord, så brug _ som mellemrum) til sidst i den





# En funktion der tager 0 argumenter og returnere en "str"
def få_historie_titlen_fra_programmets_argumenter() -> str:
  en_tom_tekst_streng : str = ""

  der_er_ingen_argumenter : bool = sys.argv.__len__() == 1

  if(der_er_ingen_argumenter):
    return en_tom_tekst_streng
  else:
    historie_titlen : str = sys.argv[1]
    return historie_titlen





# En funktion der tager 0 argumenter og returnerer en "str"
def læs_brugerens_navn_fra_filen() -> str:
  placeringen_på_folderen_python_filen_er_i : str = os.path.dirname(os.path.realpath(__file__))
  
  filens_placering : str = os.path.join(placeringen_på_folderen_python_filen_er_i, "brugerens_navn.txt")

  print(filens_placering)

  filen : TextIOWrapper = open(filens_placering)

  filens_indhold : str = filen.read()

  return filens_indhold





# En funktion der tager 0 argumenter og returnerer en "str"
def få_et_væsen_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge et væsen. Skriv det og klik 'enter'")

  et_væsen : str = input()

  print("Tak!")
  print("")

  return et_væsen





# En funktion der tager 0 argumenter og returnerer en "str"
def få_et_navneord_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge et navneord i ental (bold, and). Skriv det og klik 'enter'")

  et_navneord : str = input()

  print("Tak!")
  print("")

  return et_navneord





# En funktion der tager 0 argumenter og returnerer en "str"
def få_tillægsord_følelse_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge et tillægsord der beskriver en følelse. Skriv det og klik 'enter'")

  tillægsord_følelse : str = input()

  print("Tak!")
  print("")

  return tillægsord_følelse





# En funktion der tager 0 argumenter og returnerer en "str"
def få_et_sted_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge et sted. Skriv det og klik 'enter'")

  et_sted : str = input()

  print("Tak!")
  print("")

  return et_sted





# En funktion der tager 0 argumenter og returnerer en "str"
def få_et_tillægsord_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge et tillægsord (bred, gigantisk). Skriv det og klik 'enter'")

  et_tillægsord : str = input()

  print("Tak!")
  print("")

  return et_tillægsord





# En funktion der tager 0 argumenter og returnerer en "str"
def få_en_slags_person_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge en slags person. Skriv det og klik 'enter'")

  en_slags_person : str = input()

  print("Tak!")
  print("")

  return en_slags_person



# En funktion der tager 0 argumenter og returnerer en "str"
def få_navneord_flertal_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge et navnenord i flertal (bolde, ænder). Skriv det og klik 'enter'")

  navneord_flertal : str = input()

  print("Tak!")
  print("")

  return navneord_flertal
  
  
  


# En funktion der tager 0 argumenter og returnerer en "str"
def få_et_udsagnsord_fra_brugere() -> str:
  print("")
  print("Jeg skal bruge et udsagnsord i datid (rullede, spiste). Skriv det og klik 'enter'")

  udsagnsord_datid : str = input()

  print("Tak!")
  print("")

  return udsagnsord_datid
  




# En funktion der tager mange argumenter, alle af typen "str" og returnerer ingenting
def skriv_historien(et_væsen : str, et_navneord : str, tillægsord_følelse : str, et_sted : str, et_tillægsord : str, en_slags_person : str, navneord_flertal : str, et_udsagnsord : str, brugerens_navn : str):

  print("En lille " + et_væsen + " boede i et stort " + et_navneord + ". Her var den " + tillægsord_følelse + " for at bo.")
  print("Den lille " + et_væsen + " " + et_udsagnsord + " altid hele vejen når den skulle hen til " + et_sted + ".")
  print("men en dag skete der noget mystisk. Den lille " + et_væsen + " kom frem til " + et_sted + " men noget føltes ikke")
  print("rigtigt... Der var en mærkelig stemning. Den lille " + et_væsen + " kiggede sig omkring og prøvede at finde ud af hvad der var anderledes.")
  print("Den kiggede op.. og ned. 'hey! hey du der!' Den lille " + et_væsen + " snurrede omkring og stirrede på den " + et_tillægsord + " " + en_slags_person)
  print("der tårnede sig op over den. 'har du set hvad der er sket med " + et_sted + "!?' spurgte " + en_slags_person + ". Den lille " + et_væsen + " kiggede tilbage på")
  print(et_sted + " og spærrede øjnene op. Det var jo helt vanvittigt! Det velkendte " + et_sted + " var skrumpet med ca 25%, og nu hvor " + et_væsen + " kiggede grundigt")
  print("efter, kunne den se at " + et_sted + " var fyldt med uanede mængder af " + navneord_flertal + ". Det løb den lille " + et_væsen + " koldt ned af ryggen, og den")
  print("drejede om på hælen og stak af.")
  print("")
  print("tak for at have prøvet" + brugerens_navn + "spil")


# En funktion der tager 0 argumenter og returnerer ingenting
def stop_programmet_fra_at_lukke():
  # Hvis du læser den her funktion, kan du så regne ud hvorfor vi har skrevet dem?
  print("") # Ny linje
  print("") # Ny linje
  print("") # Ny linje
  print("For at stoppe programmet fra at lukke når det er færdigt så")
  print("venter vi til allersidst på at du klikker 'enter'")
  brugerens_input : str = input()










# her er selve programmet. Det er meget meget simpelt, og kalder 1 funktion
kør_Historieskriveren()







# Vi skal bruge funktioner fra "sys.pyi" og "os.pyi" (.pyi betyder "python interne filer")
# Disse er automatisk er installeret med python
import sys
import os


"""


Show them videos of my city finder
Show them my politician  email finder

Program should have an input and an output
It should forward declare

it should have a few functions it calls
it should incorporate something visual that does not require downloading an external library

I think a text adventure thing is a good idea


Make sentences that misses words
have the user type in the missing words


Functional requirements

input and output of the program
input and output of files
input and output of text



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

# Dette er hoved-funktionen
# HELE den her python fil er kun et funktions kald neders i programmet
# Dette er gjort så man kan læse koden ovenfra og ned og forstå den
# Du kan finde ud af mere ved at søge "python forward declaration" på internettet
def kør_Historieskriveren():

  skriv_titlen_hvis_der_er_en()

  brugerens_navn : str = læs_brugerens_navn_fra_filen()

  print(f"Hej {brugerens_navn}, velkommen til din historie")


  navnord_1 : str = få_et_navnord_fra_brugeren()
  udsagnsord_1 : str = få_et_udsagnsord_fra_brugeren()
  navnord_2 : str = få_et_navnord_fra_brugeren()

  skriv_historien(navnord_1, udsagnsord_1, navnord_2)





def skriv_titlen_hvis_der_er_en():
  historiens_titel : str = få_historie_titlen_fra_programmets_argumenter()

  der_er_en_titel : bool = historiens_titel != ""

  if(der_er_en_titel):
    print(f"Velkommen til {historiens_titel}")





def få_historie_titlen_fra_programmets_argumenter() -> str:
  en_tom_tekst_streng : str = ""

  der_er_ingen_argumenter : bool = sys.argv.__len__() == 1

  if(der_er_ingen_argumenter):
    return en_tom_tekst_streng
  else:
    historie_titlen : str = sys.argv[1]
    return historie_titlen





def læs_brugerens_navn_fra_filen() -> str:
  placeringen_på_folderen_python_filen_er_i : str = os.path.dirname(os.path.realpath(__file__))
  
  filens_placering : str = os.path.join(placeringen_på_folderen_python_filen_er_i, "brugerens_navn.txt")

  filen : TextIOWrapper = open(filens_placering)

  filens_indhold : str = filen.read()





def få_et_navnord_fra_brugeren() -> str:
  print("")
  print("Jeg skal bruge et navnord. Skriv det og klik 'enter'")

  navnord : str = input()

  print("Tak!")
  print("")

  return navnord





def få_et_udsagnsord_fra_brugeren() -> str:
  print("")
  print("Jeg skal bruge et udsagnsord i nutidsform (løber, hopper, kravler). Skriv det og klik 'enter'")

  udsagnsord : str = input()

  print("Tak!")
  print("")

  return udsagnsord





def skriv_historien(navnord_1 : str, udsagnsord : str, navnord_2 : str):

  print(f"Så {navnord_1} kom {udsagnsord} en dag, og pludselig så den en {navnord_2}")

  # Hvis du læser de næste 4 linjer, kan du så regne ud hvorfor vi har skrevet dem?
  print("") # Ny linje
  print("For at stoppe programmet fra at lukke når det er færdigt så")
  print("venter vi til allersidst på at du klikker 'enter'")
  brugerens_input : str = input()









kør_Historieskriveren()
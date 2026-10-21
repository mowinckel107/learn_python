


# Hej!
# Så! Første ting. Det her er en kommentar!
# En kommentar starter med # og bliver ikke kørt som kode
# Så det er bare tekst til at forklare koden :3

# Du kan skrive dine egne kommentarer så den her fil er nemmere at
# læse næste gang du skal bruge den :3

# For at du kan begynde at lege med python, skal vi vide 2 ting
# 1: Hvad er en variabel
# 2: Hvad er en funktion

# Du kan læse programmet, og du må gerne lave om på ting og se hvad forskel det
# gør når du kører programmet :3



#----- Variabler -----

# Variabel
# Variabler er hvordan et program husker ting
# Variabler har:
# Et navn
# En type
# En værdi

# Lad os lave en variabel
et_heltal : int = 0

# Variablens navn er et_heltal
# Variablens type er int (betyder heltal)
# Variablens værdi er 0

# En variabels navn og type ændre sig ikke
# En variabels værdi ændre sig tit

# Du kan tænke på variabler som kasser som kun kan indeholde 1 slags ting
# Hvad der er i kassen ændre sig. Men kassen gør ikke


# Vi ændre en variabel ved at sætte den lig noget andet
et_heltal = 8

# Nu er variablens værdi 8
# Dens type er stadig int, og dens navn er stadig Min_heltals_variabel

# Lad os lave en anden type variable
et_kommatal : float = 0.5

# float er et... dårligt engelsk navn for komma-tal
# Programmering er på engelsk, så vi bruger et punktum i steder for et komma


jeg_er_god_til_programmering : bool = False

# en bool er en påstand som kan være sandt eller falskt

# Vi kan ændre en bools værdi ligesom alle andre variabler
jeg_er_god_til_programmering = True


# Godt arbejde at være kommet så langt!
# Sidste variabel type
# Husk, at hvis du ikke kan huske vilke typer variabler der er, så kan du bare kopiere
# navnene fra den her fil! :D

# en "str" er en "tekst streng", som betyder en mænge text symboler
mit_navn : str = "Farbaute"
# en streng kan også være 0 tekst symboler
mit_navn = ""

# Du har nu hørt om alle de typer du vil skulle bruge i python! :D
# Næste ting! Funktioner!



#----- Funktioner -----

# Så variabler er hvordan koden HUSKER ting
# Funktioner er hvordan koden GØR ting


# Lad os køre funktionen "print" med en "str" variabel
besked_til_brugeren : str = "Du har kørt et python program! :D"
print(besked_til_brugeren)
# Prøv at lave om i besked_til_brugeren variablen og kør programmet igen for
# at se dine ændringer (Husk at gemme dine ændringer)


# Vi kan også definere vores egene funktioner med order "def"

# Det gør vi med order "def"
# Derefter giver vi funktionen et navn uden mellemrum
# Derefter skriver vi hvilke argumenter funktionen tager i (parentes)
# Derefter skriver vi hvad funktionen gør
# Alt indeni funktionen starter med 2 mellemrum

# Vi definerer en funktion der dividerer 2 tal med hinanden. Den tager 2 heltal(int), og returnerer et kommatal(float)
def divider_2_tal(det_første_tal : int, det_andet_tal : int) -> float:

  # Vi gemmer resultatet i en variabel af type "float"
  resultat : float = det_første_tal / det_andet_tal
  # Vi returnerer resultatet
  return resultat


# Nu kan vi kalde funktionen! :D
resultatet_som_float : float = divider_2_tal(10, 2)
# Prøv at lave om på de tal du giver funktionen og kør programmet igen og se ændringen
# Hvad sker der hvis du dividere med 0?

# Nu vil vi gerne se resultatet når vi kører programmet
# Men man kan kun skrive "str" typer ud
# SÅ! Vi skal have lavet vores "float" om til en "str"

# Vi kan lave variabler som int, float eller bools om til "str" ved at kalde "str" funktionen:
# Vi laver en variabel som vi kan putte resultatet som str ind i
resultatet_som_str : str = ""

# Så kalder vi "str" funktionen, og lægger resultatet i "resultatet_som_str" variablen
resultatet_som_str = str(resultatet_som_float)

# Vi kan skrive en tom linje for at gøre vores tekst til brugeren pænere
print("")
# Vi kan også lave str variabler ved at lægge flere "str" typer sammen! :D
print("Ved du hvorfor jeg skriver " + resultatet_som_str + "?")
# Prøv at lave om i det der bliver skrevet ud
# Der er 3 strenge lagt sammen. Hvorfor slutter den første streng med et mellemrum?

# Så når vi kører vores program med .bat filen kan vi se at det virker!


# Hvis du ikke ved hvordan du kører den her python fil, så find og
# læs "hvordan du kører et python program.txt" som 
# hjælper dig med at køre python programmer! :D
# Dobbelt klik på den og læs den. Det tager ingen tid :3

# Prøv at køre programmet. Prøv at lave om i ting. Gæt på hvad det vil gøre, og se om det sker :3
# For eksempel, hvad sker der hvis du dividere med 0? Prøv at gætte først og så kør det


# Nu kan du gå videre til "mit første projekt"


# Hvis du læser de næste 4 linjer, kan du så regne ud hvorfor vi har skrevet dem?
print("") # Ny linje
print("For at stoppe programmet fra at lukke når det er færdigt så")
print("venter vi til allersidst på at du klikker 'enter'")
brugerens_input : str = input()


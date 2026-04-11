# natataaplikajson


Beskrivelse av løsningen din:

Dette prosjektet er en natataaplikajson der du kan se notater du har lagret i Nototer. Du kan velge med å se hele notatet eller bestemte deler av dataen.

backend surveren honterer dataen altså lagringen også ber brukeren om data fra den med todos eller notes. 

Hvordan installere og starte serveren:
for å starte klienten så må du være på programet payton og skrive i teminalen der inn "uvicorn server:app --reload" også ruller det ned et bra grunne og blå priker da er surveren på.

Hvordan starte klienten
dette er ffrontend altså det brukeren ser da tar du lenken til nettsiden. og har de ikkke den s¨går du på index.html høyerkliker og går live. eller så kopierer du lenken og butter den på en nettside øverst i URL og enter.
da kommer du til nettsiden.

så når du kommer til nettsiden er det en tomt felst der kan du skrevet en komado. det kan du velge å skrive etter det følgende valg
    1. skriv / da får du opp en melding der det står ("Hello, API!")
    2. skriv /todos da får du helle listen av notater
    3. skriv /todos/(ID) iden må være et tall og tallene du kan skrive er 0, 1, 2, 3 for å få ut bestemte notater.

Eksempler på bruk av API

Det er APIen vi bruekr for å hente data fra databasen
API komandoene jeg bruker er
 GET der jeg henter dataen som brukeren velger 
 POST bruker jeg litt der jeg da brukeren kan legge til data.

teknologivalgene:
grunnen til at jeg har valkt teknologi valget er fordi html og css er en enkelt å bruke til å lage nettsider og enkelt til å kummuisere med javascipt.

javascipt er vå funksjon og mellom bro mellom surver og klient(bruker)

jeg velger payton som er bakcend surveren vår og denne henter og ser filene til json filene.


async function getData() { //vennter på data. lager dereter funksjon som heter "getData"
  const url = "http://127.0.0.1:8000";  // her forteller vi hva URL er altså IP adressen til nettstedet
  const path = document.getElementById("input").value; // variabel navn også finner den ID (input) og henter inputen
  const baseUrl = url + path; // også setter den sammen URL og det inputen er hentet
  let = Verdi = "result"; // variabel som heter "verdi" og ineholder en tekst

  try { //prøver å kjøre ofte løres vis feil oppstår
    const response = await fetch(baseUrl); //respons(prøver å hente) vent til den har hentet data fra (url)
    if (!response.ok) { //vis feil ! (fik data) kjekk  som noe gikk galt
      throw new Error(`Response status: ${response.status}`); //sier at det ble feil.
    }

    const result = await response.json();//variabel som ikke kan endres. veneter. gjør svar om til JSON-data
    document.getElementById("Verdi").textContent = JSON.stringify(result); //sender videre til en nettside og prøver å vinne (ID i Html) som heter "Verdi". og gjør dataen() om til tekst på nettsiden
    //console.log(result);

  } catch (error) { {//hvis try går galt så kommer vi hit og tar opp feilen
    console.error(error.message); //også skriver vi i (console.error) det feilen meldingen sier til oss.
  
  }
}

//leger til todo
async function addTodo() {  
  const url = "http://127.0.0.1:8000/todos"; //vi må inn på siden URL (API til nettsiden ) og inn i dataen
  const tekst = document.getElementById("nyTodo").value; // variabel som heter (Tekxt) det som kjer her er at vi finner id html "nyTodo" og henter det brukeren skrev.
  const nyOppgave = { "tekst": text, "done": false}; //legger til en oppgave eller variablen tekst og sier denne er ikke ferdig så (false)
  try{
    const response = await fetch(url, { //sender data til URL altså til surveren
      method: "POST",//Sender den til Post funksjonen til pyton
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(nyOppgave)// gjør om til tekst
    });
    if (!response.ok) { //hvis det ikke er ok så..
      throw new Error(`Response status: ${response.status}`); ////sier at det ble feil.
    }
    const result = await response.json(); // får svar fra surver som igjen går til surver fil
    document.getElementById("Verdi").textContent = JSON.stringify(result); //  legger det i vise i liten
    document.getElementById("nTodo").value = ""; //finner html id "nyTodo" og tømer den
  } catch (error) { //når det var feil tar den opp eror
    console.error(eror.message);//sender eror meldingen i consloe
    } 
  }
  
}

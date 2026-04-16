async function getData() { //vennter på data. lager dereter funksjon som heter "getData"
  const url = "http://192.168.20.71:8000";  // her forteller vi hva URL er altså IP adressen til nettstedet
  const path = document.getElementById("input").value; // variabel navn også finner den ID (input) og henter inputen
  const baseUrl = url + path; // også setter den sammen URL og det inputen er hentet
  let Verdi = "result"; // variabel som heter "verdi" og ineholder en tekst
  

  try { //prøver å kjøre ofte løres vis feil oppstår
    const response = await fetch(baseUrl); //respons(prøver å hente) vent til den har hentet data fra (url)
    if (!response.ok) { //vis feil ! (fik data) kjekk  som noe gikk galt
      throw new Error(`Response status: ${response.status}`); //sier at det ble feil.
    }

    const result = await response.json();//variabel som ikke kan endres. veneter. gjør svar om til JSON-data
    var str = JSON.stringify(result, null, 2);
    document.getElementById("Verdi").textContent = JSON.stringify(result); //sender videre til en nettside og prøver å finne ID i (Html) som heter "Verdi". og gjør dataen() om til tekst på nettsiden
    //console.log(result);

  } catch (error) { {//hvis try går galt så kommer vi hit og tar opp feilen
    console.error(error.message); //også skriver vi i (console.error) det feilen meldingen sier til oss.
  
  }}
}

function sendpostrequesttodos() {

  let newtodo = document.getElementById("newtodo").value;//henter verddien (newtodo) som liger i html og lagrer den i en variabel
  console.log(newtodo); //skriver ut verdien i consle.log

  fetch("http://192.168.20.71:8000/newtodo", { //sende melding til API
  method: "POST", //sender daya til API
  headers: { 
    "Content-Type": "application/json"//sender til (Json-data)
  },
  body: JSON.stringify({
    todo: newtodo,
  })
}).then(response => {
    if (!response.ok) {//hvis det ikke er riktig
      throw new Error("Noe gikk galt med requesten"); //så sier den at noe gikk galt
    }
    return response.json(); // så retunerer den (response) i filen.
  }).then(data => {//data er en slags variabel men det er ikke det det henter fra response.json og det ser man ikke men det er litt komplisert
    console.log("Svar fra server:", data); //her svarer surveren og henter fra hva data svarer i console.log
  }).catch(error => {//når det ble error
    console.error("Feil:", error);//vise feilen i consol.log og si hva feilen er.
  });
}

function sendpostrequestnotes() {

  let newnote = document.getElementById("newnote").value;//henter verddien (newtodo) som liger i html og lagrer den i en variabel
  console.log(newtodo); //skriver ut verdien i consle.log

  fetch("http://192.168.20.71:8000/newnote", { //sende melding til API
  method: "POST", //sender daya til API
  headers: {
    "Content-Type": "application/json"//sender til (Json-data)
  },
  body: JSON.stringify({
    todo: newnote
  })
}).then(response => {
    if (!response.ok) {//hvis det ikke er riktig
      throw new Error("Noe gikk galt med requesten"); //så sier den at noe gikk galt
    }
    return response.json(); // så retunerer den (response) i filen.
  }).then(data => {//data er en slags variabel men det er ikke det det henter fra response.json og det ser man ikke men det er litt komplisert
    console.log("Svar fra server:", data); //her svarer surveren og henter fra hva data svarer i console.log
  }).catch(error => {//når det ble error
    console.error("Feil:", error);//vise feilen i consol.log og si hva feilen er.
  });
}



function senddeleterequestnotes() {

  let slett = document.getElementById("delete").value;//henter verddien (newtodo) som liger i html og lagrer den i en variabel
  console.log(slett); //skriver ut verdien i consle.log

  fetch("http://192.168.20.71:8000/delete/" + slett, { //sende melding til API
  method: "DELETE", //sender daya til API
  headers: {
    "false": "application/json"
  }
  
}).then(response => {
    if (!response.ok) {//hvis det ikke er riktig
      throw new Error("Noe gikk galt med requesten"); //så sier den at noe gikk galt
    }
    return response.json(); // så retunerer den (response) i filen.
  }).then(data => {//data er en slags variabel men det er ikke det det henter fra response.json og det ser man ikke men det er litt komplisert
    console.log("Svar fra server:", data); //her svarer surveren og henter fra hva data svarer i console.log
  }).catch(error => {//når det ble error
    console.error("Feil:", error);//vise feilen i consol.log og si hva feilen er.
  });
}
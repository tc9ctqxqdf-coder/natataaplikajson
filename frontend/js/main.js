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
}

function sendpostrequest() {
  /* Dra teksten ut fra tekstfeltet med getElementById("newtodo") */
  let newtodo = document.getElementById("newtodo").value;
  console.log(newtodo);

  fetch("http://localhost:8000/newtodo/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    todo: newtodo,
  })
})
  .then(response => {
    if (!response.ok) {
      throw new Error("Noe gikk galt med requesten");
    }
    return response.json();
  })
  .then(data => {
    console.log("Svar fra server:", data);
  })
  .catch(error => {
    console.error("Feil:", error);
  });
}
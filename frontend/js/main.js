
async function getData() {
  const url = "http://127.0.0.1:8000/todos";
  let = Verdi = "result";

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    document.getElementById("Verdi").textContent = JSON.stringify(result);
    //console.log(result);

  } catch (error) {
    console.error(error.message);
  }
  
 
}


document
  .getElementById("agregarFormulario")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const nombreSena = document.getElementById("nombre").value;
    const data = { nombre: nombreSena };

    fetch("/agregar/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.text())
      .then((data) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, "text/html");

        const estado = doc
          .querySelector("#alert-container")
          .getAttribute("data-estado");
        const mensaje = doc
          .querySelector("#alert-container")
          .getAttribute("data-mensaje");
       alert("guardado")
      })
  });
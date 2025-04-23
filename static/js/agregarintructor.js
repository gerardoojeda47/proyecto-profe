document.getElementById("agregarFormularios").addEventListener("submit", function (event) {
    event.preventDefault();
    const nombrecompleto = document.getElementById("nombrecompleto").value;
    const email = document.getElementById("email").value;
    const sena_id = document.getElementById("sena_id").value;
    const data = {
        nombrecompleto: nombrecompleto,
        email: email,
        sena_id: sena_id
    };
    console.log("Datos a enviar:", data); 
    fetch("/agregarintructor/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data) 
    })
    .then((response) => response.text())
    .then((data) => {
        alert("Guardado")  
        document.getElementById("agregarFormulario").reset();
    })
});

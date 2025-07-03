document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("register-form");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const data = {
            username: document.getElementById("username").value,
            email: document.getElementById("email").value,
            rut: document.getElementById("rut").value,
            phone: document.getElementById("phone").value,
            password: document.getElementById("password").value
        };

        console.log("Datos que se van a enviar:", data);  // Login antes de enviar

        try {
            const response = await fetch("/api/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            console.log("Respuesta del servidor:", result);  // Login respuesta servidor
            alert(result.message || result.error);
        } catch (err) {
            console.error("Error en la conexión con el servidor:", err);  // Login error conexión
            alert("Error de conexión con el servidor.");
        }
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

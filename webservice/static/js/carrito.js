function payWithTransfer() {
    alert('Redirigiendo a la página de pago por transferencia...');
}

document.addEventListener('DOMContentLoaded', function() {
    const quantityButtons = document.querySelectorAll('.quantity-btn');
    quantityButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const icon = this.querySelector('i');
            const originalClass = icon.className;
            icon.className = 'fas fa-spinner fa-spin';
            setTimeout(() => {
                icon.className = originalClass;
            }, 500);
        });
    });

    // Lógica para el botón de Mercado Pago
    const btnMP = document.getElementById('btn-mercadopago');
    if (btnMP) {
        btnMP.addEventListener('click', function (e) {
            if (userLoggedIn === "true") {
                pagarConMercadoPago();
            } else {
                e.preventDefault();
                // Abre el modal de login
                const loginModal = new bootstrap.Modal(document.getElementById('exampleModal'));
                loginModal.show();

                const loginBtn = document.getElementById('btn-login');
                if (!loginBtn.dataset.listenerAdded) {
                    loginBtn.addEventListener('click', async function (ev) {
                        ev.preventDefault();
                        const email = document.getElementById('loginEmail').value;
                        const password = document.getElementById('loginPassword').value;
                        const response = await fetch('/api/login/', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': getCookie('csrftoken')
                            },
                            body: JSON.stringify({ email, password })
                        });
                        const data = await response.json();
                        if (response.ok) {
                            loginModal.hide();
                            window.location.href = "/carrito/";
                        } else {
                            alert(data.error || 'Credenciales incorrectas');
                        }
                    });
                    loginBtn.dataset.listenerAdded = "true";
                }
            }
        });
    }
});

// Función para Mercado Pago
function pagarConMercadoPago() {
    fetch('/api/carrito/')
        .then(response => response.json())
        .then(data => {
            const productos = data.productos;
            return fetch('/pagar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ productos: productos }),
            });
        })
        .then(response => response.json())
        .then(data => {
            if (data.init_point) {
                window.location.href = data.init_point; // Redirigir a Mercado Pago
            } else {
                alert('Error al iniciar pago');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Función para obtener el CSRF token de la cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
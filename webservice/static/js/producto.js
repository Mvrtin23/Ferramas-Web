
        // Funcionalidad de búsqueda
        document.getElementById('searchInput').addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const productCards = document.querySelectorAll('.card-product');
            
            productCards.forEach(card => {
                const productName = card.querySelector('h3').textContent.toLowerCase();
                const productDesc = card.querySelector('p').textContent.toLowerCase();
                
                if (productName.includes(searchTerm) || productDesc.includes(searchTerm)) {
                    card.style.display = 'block';
                    card.style.animation = 'fadeInUp 0.4s ease';
                } else {
                    card.style.display = 'none';
                }
            });
        });

        // Funcionalidad de filtros
        document.querySelectorAll('.filter-tag').forEach(tag => {
            tag.addEventListener('click', function() {
                // Remover clase activa de todos los filtros
                document.querySelectorAll('.filter-tag').forEach(t => t.classList.remove('active'));
                // Agregar clase activa al filtro clickeado
                this.classList.add('active');
                
                const category = this.dataset.category;
                const productCards = document.querySelectorAll('.card-product');
                
                productCards.forEach((card, index) => {
                    if (category === 'todos' || card.dataset.category === category) {
                        card.style.display = 'block';
                        // Animación escalonada
                        setTimeout(() => {
                            card.style.animation = 'fadeInUp 0.4s ease forwards';
                        }, index * 50);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });

        // Animación inicial de carga
        document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.card-product');
            cards.forEach((card, index) => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                
                setTimeout(() => {
                    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, index * 100);
            });
        });

        document.querySelectorAll('.card-product').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-10px) scale(1.02)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });


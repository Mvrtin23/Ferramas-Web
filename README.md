# 🛠️ FERRAMAS

**Ferramax** es una plataforma de comercio electrónico especializada en ferreterías. Permite gestionar inventario, realizar pagos en línea y manejar conversiones de divisas en tiempo real gracias a la integración de APIs externas.  

---

## 🎯 Objetivo

Automatizar el proceso de ventas y mejorar la eficiencia operativa mediante la integración de servicios externos como:

- 🏦 **Webpay**
- 📈 **Banco Central de Chile**
- 💳 **Mercado Pago**

---

## 💻 Tecnologías Utilizadas

| Componente     | Tecnología               |
|----------------|--------------------------|
| 🖥️ Frontend     | HTML, CSS, JavaScript     |
| ⚙️ Backend      | Python (Django)           |
| 🗄️ Base de Datos| Supabase (PostgreSQL)     |
| 🔌 APIs         | Mercado Pago, Banco Central de Chile |
| 🛠️ Herramientas | VSCode, GitHub Desktop, Navegador |

---

## 🚀 Funcionalidades

- 🔍 API RESTful para consulta de productos.
- 💵 Integración con Mercado Pago para pagos.
- 💱 Conversión de divisas en tiempo real con datos del Banco Central.
- 🔐 Configuración con variables de entorno seguras.

---

## 🛠️ Configuración Paso a Paso

## 1️⃣ Clonar el repositorio
git clone https://github.com/tu-usuario/ferramax.git
También puedes usar GitHub Desktop para clonar el proyecto.

2️⃣ Abrir en VSCode
Abre la carpeta del proyecto en Visual Studio Code.

Abre una terminal dentro del proyecto.

3️⃣ Crear archivo .env
Ubicación requerida:

bash
Copiar
Editar
FERRAMAS_WEB_SERVICES/.env
Puedes crearlo manualmente o ejecutar:

powershell
Copiar
Editar
New-Item -Path .env -ItemType File
Pega lo siguiente en el archivo .env:

ini
Copiar
Editar
SUPABASE_URL=https://kqfhjpwxodvhbpkhotji.supabase.co/
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
DEBUG=true
SECRET_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
⚠️ Importante: Nunca subas tu archivo .env al repositorio público.

4️⃣ Instalar dependencias
bash
Copiar
Editar
pip install Pillow
pip install django
pip install supabase
pip install djangorestframework
pip install psycopg2-binary
pip install mercadopago
pip install requests
pip install python-dotenv
pip install python-decouple
5️⃣ Problemas de conexión a la base de datos
Si tienes errores de conexión con Django y Supabase, probablemente tu red esté usando solo IPv4. Supabase requiere IPv6.

🔗 Verifica tu tipo de IP aquí: https://www.whatismyip.com

En caso de problemas, usa el Pooler de Supabase modificando tu settings.py:

python
Copiar
Editar
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.kqfhjpwxodvhbpkhotji',
        'PASSWORD': 'renan12345',  # <-- Reemplaza por tu contraseña segura
        'HOST': 'aws-0-sa-east-1.pooler.supabase.com',
        'PORT': '6543',
    }
}

🧑‍💻 Autor
Martin Muñoz
📧 martinmunoze@correo.com
🌐 GitHub

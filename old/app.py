from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Información Personal</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
                padding: 20px;
                transition: background-color 0.3s, color 0.3s;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                display: inline-block;
                transition: background-color 0.3s, color 0.3s;
            }
            .profile-pic {
                border-radius: 50%;
                width: 150px;
                height: 150px;
                margin-bottom: 20px;
            }
            .dark-mode {
                background-color: #333 !important;
                color: #fff !important;
            }
            .dark-mode .container {
                background-color: #444 !important;
                color: #fff !important;
            }
        </style>
    </head>
    <body>
        <button onclick="toggleDarkMode()" style="margin-bottom: 20px; padding: 10px 20px; font-size: 16px;">Modo Noche</button>    <br>
        <div class="container">
            <img src="https://img.freepik.com/vector-premium/icono-perfil-usuario-estilo-plano-ilustracion-vector-avatar-miembro-sobre-fondo-aislado-concepto-negocio-signo-permiso-humano_157943-15752.jpg" alt="Foto de Perfil" class="profile-pic">
            <h3>Gerardo Olivares Aguilar</h3>
            <h3>Grado: 9 Grupo: B</h3>
        </div>
        <script>
            function toggleDarkMode() {
                document.body.classList.toggle('dark-mode');
            }
        </script>
    </body>
    </html>
    """
    


if __name__ == "__main__":
    app.run(debug=True)
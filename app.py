from flask import Flask, render_template

app = Flask(__name__)

# Información estructurada según la Guía de Recopilación (Docente Sandra Chávez)
empresa_data = {
    "nombre": "Mint Corner",
    "fundacion": "2024",
    "ubicacion": "Lima, Perú",
    "tipo": "Moda Urbana & Streetwear",
    "mision": "Ofrecer prendas de vestir urbanas auténticas y de alta calidad que permitan a los jóvenes expresar su identidad, actitud y pasión por la cultura callejera, el arte y la música.",
    "vision": "Convertirnos en la marca de streetwear independiente referente en Latinoamérica, reconocida por nuestros diseños originales y la comunidad que nos respalda.",
    "valores": [
        "Autenticidad y estilo propio",
        "Cultura urbana y creatividad",
        "Calidad en confección y estampados",
        "Comunidad y libertad de expresión"
    ],
    "productos": [
        {"nombre": "Oversized Hoodies", "desc": "Poleras de algodón pesado con estampados gráficos exclusivos y corte oversized confort.", "precio": "S/ 120.00"},
        {"nombre": "Streetwear Graphic Tees", "desc": "Polos 100% algodón reactivo con ilustraciones de estilo grafiti y cultura urbana.", "precio": "S/ 65.00"},
        {"nombre": "Cargo Pants & Joggers", "desc": "Pantalones holgados de alta durabilidad diseñados para máxima comodidad en la calle.", "precio": "S/ 110.00"},
        {"nombre": "Caps & Beanies", "desc": "Gorras y gorros de lana con bordados oficiales de la marca Mint Corner.", "precio": "S/ 45.00"}
    ],
    "historia": "Mint Corner nació en el 2024 como una iniciativa independiente inspirada en la música, el arte urbano y la estética de la calle. Diseñada para quienes no siguen tendencias genéricas, sino que crean su propio camino.",
    "logros": [
        "Lanzamiento exitoso de la colección 'Since 2024'",
        "Comunidad activa de más de 10,000 seguidores en redes sociales",
        "Colaboraciones independientes con artistas urbanos e ilustradores locales"
    ],
    "contacto": {
        "direccion": "Av. Larco 789, Miraflores - Lima (Showroom)",
        "telefono": "+51 912 345 678",
        "email": "contacto@mintcorner.com",
        "redes": {
            "instagram": "@mintcorner.pe",
            "tiktok": "@mintcorner.official",
            "facebook": "Mint Corner Streetwear"
        }
    }
}

@app.route("/")
def inicio():
    return render_template("index.html", empresa=empresa_data)

if __name__ == "__main__":
    app.run(debug=True)
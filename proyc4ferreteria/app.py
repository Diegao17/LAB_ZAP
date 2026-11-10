from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_secreta_para_flashed_messages"


# RUTA: INICIO
@app.route("/")
def inicio():
    return render_template("index.html")


# RUTA: DETALLES
@app.route("/detalles")
def detalles():
    return render_template("detalles.html")


# RUTA: PROMOCIONES
@app.route("/promociones")
def promociones():
    return render_template("promociones.html")


# RUTA: CONTACTO
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        asunto = request.form.get("asunto")
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        telefono = request.form.get("telefono")
        mensaje = request.form.get("mensaje")

        # Aquí puedes poner validaciones o guardar info.
        flash("Formulario enviado correctamente (simulado).")

        return redirect(url_for("contacto"))

    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)
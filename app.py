from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular():
    resultado = None
    if request.method == 'POST':
        try:
            c1 = float(request.form['corte1'].replace(',', '.'))
            c2 = float(request.form['corte2'].replace(',', '.'))
            c3 = float(request.form['corte3'].replace(',', '.'))
            meta = float(request.form['meta'].replace(',', '.'))

            promedio = (c1 * 0.20) + (c2 * 0.20) + (c3 * 0.20)
            nota_final = (meta - promedio) / 0.40

            if nota_final > 5:
                resultado = f"Necesitas más de 5.0 para alcanzar {meta:.2f} 😬"
            elif nota_final < 0:
                resultado = f"¡Ya alcanzaste la nota! 🎉 Puedes sacar 0 y aún así obtener {meta:.2f}"
            else:
                resultado = f"Necesitas al menos {nota_final:.2f} en el examen final para lograr {meta:.2f}"

        except ValueError:
            resultado = "Por favor, ingresa solo números válidos."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

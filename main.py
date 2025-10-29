from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operacion = request.form['operacion']

            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multiplicacion':
                resultado = num1 * num2
            elif operacion == 'division':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    error = "Error: división por cero."
        except ValueError:
            error = "Por favor, ingresa números válidos."

    return render_template('index.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

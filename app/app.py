from flask import Flask, render_template, request

app = Flask(__name__)

#vista que carga desde la raíz
@app.route('/')
def index():
    return render_template('index.html') #renderiza lo que está en templates

#recibe los datos del formulario
@app.route('/getData', methods = ['GET', 'POST'])
def getData():
    if request.method == 'POST':
        x = request.form['gender']
        h = request.form['height']
        w = request.form['weight']
        return calculate(x, h, w)
    else:
        return "fuck you bitch! .I."
    
def calculate(x, h, w):
    a = float(h)
    b = float(w)
    IMC = (b/(a**2))
    result = diagnosis(x, IMC)
    
    sendData = {
        'diagnóstico': result
    }
    return render_template('index.html', data = sendData)

def diagnosis(x, IMC):
    if x== 'female':
        if IMC <= 16:
            diagnosis = "tas' desnutrida ma'"
        elif IMC > 16 and IMC <=20:
            diagnosis = "tas' baja de peso ma'"
        elif IMC > 20 and IMC <=24:
            diagnosis = "tas' bien de peso ma'"
        elif IMC > 24 and IMC <=29:
            diagnosis = "tas' pasada de peso ma'"
        else:
            diagnosis = "vas a morir si sigues comiendo así ma'"
    else:
        if IMC <= 17:
            diagnosis = "tas' desnutrido pa'"
        elif IMC > 17 and IMC <=20:
            diagnosis = "tas' bajo de peso pa'"
        elif IMC > 20 and IMC <=24:
            diagnosis = "tas' bien de peso pa'"
        elif IMC > 24 and IMC <=29:
            diagnosis = "tas' pasado de peso pa'"
        else:
            diagnosis = "vas a morir si sigues comiendo así pa'"   
    return diagnosis


if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True, port=5000)
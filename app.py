from flask import Flask,render_template, request, redirect, url_for #importiamo la classe flask
app = Flask(__name__) #inizializza app flask

fat = "ffffff"
lista = [6,8,9,12,5]


@app.route("/")
def s():
    return render_template("index.html",fat = fat,lista = lista)

@app.route("/profilo")
def profilo():

    return "questa è la pagina profilo"
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista.append(elemento)
    return redirect(url_for('s'))
if __name__ == '__main__':
    app.run(debug=True)


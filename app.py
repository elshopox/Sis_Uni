from flask import Flask, render_template, request

app = Flask(__name__)

universidades = {
    'UMSA': '/universidades/publicas/universidad1',
    'UPEA': '/universidades/publicas/universidad2',
    'UABJB': '/universidades/publicas/universidad3',
    'UASB': '/universidades/publicas/universidad4',
    'UNSXX': '/universidades/publicas/universidad5',
    'EMI': '/universidades/privadas/universidad1',
    'UCB': '/universidades/privadas/universidad2',
    'UNICEN': '/universidades/privadas/universidad3',
    'UDABOL': '/universidades/privadas/universidad4',
    'UPB': '/universidades/privadas/universidad5',
    'UNIVALLE': '/universidades/privadas/universidad6',
    'UNIFRANZ': '/universidades/privadas/universidad7',
    'ULS': '/universidades/privadas/universidad8',
    'UBI': '/universidades/privadas/universidad9',
    'UMMBBR': '/universidades/privadas/universidad10',
    'UN': '/universidades/privadas/universidad11',
    'LOYOLA': '/universidades/privadas/universidad12',
    'UNSLP': '/universidades/privadas/universidad13',
    'USFA': '/universidades/privadas/universidad14',
    'UREAL': '/universidades/privadas/universidad15',
    'USALESIANA': '/universidades/privadas/universidad16',
    'UDELOSANDES': '/universidades/privadas/universidad17',
    'UPIEB': '/universidades/privadas/universidad18',
    'UTB': '/universidades/privadas/universidad19',
    'UB': '/universidades/privadas/universidad20',
    'USP': '/universidades/privadas/universidad21',
    'UCORDILLERA': '/universidades/privadas/universidad22',
    'UPDS': '/universidades/privadas/universidad23',
    'UNITEPC': '/universidades/privadas/universidad24',
    'UIBATK': '/universidades/privadas/universidad25',
    'UIT': '/universidades/privadas/universidad26',
    'UP': '/universidades/privadas/universidad27'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/universidades/publicas')
def publicas():
    return render_template('publicas.html')

@app.route('/universidades/privadas')
def privadas():
    return render_template('privadas.html')

@app.route('/universidades/publicas/universidad1')
def universidad_publica1():
    return render_template('universidad_publica1.html')

@app.route('/universidades/publicas/universidad2')
def universidad_publica2():
    return render_template('universidad_publica2.html')

@app.route('/universidades/publicas/universidad3')
def universidad_publica3():
    return render_template('universidad_publica3.html')

@app.route('/universidades/publicas/universidad4')
def universidad_publica4():
    return render_template('universidad_publica4.html')

@app.route('/universidades/publicas/universidad5')
def universidad_publica5():
    return render_template('universidad_publica5.html')

@app.route('/universidades/privadas/universidad1')
def universidad_privada1():
    return render_template('universidad_privada1.html')

@app.route('/universidades/privadas/universidad2')
def universidad_privada2():
    return render_template('universidad_privada2.html')

@app.route('/universidades/privadas/universidad3')
def universidad_privada3():
    return render_template('universidad_privada3.html')

@app.route('/universidades/privadas/universidad4')
def universidad_privada4():
    return render_template('universidad_privada4.html')

@app.route('/universidades/privadas/universidad5')
def universidad_privada5():
    return render_template('universidad_privada5.html')

@app.route('/universidades/privadas/universidad6')
def universidad_privada6():
    return render_template('universidad_privada6.html')

@app.route('/universidades/privadas/universidad7')
def universidad_privada7():
    return render_template('universidad_privada7.html')

@app.route('/universidades/privadas/universidad8')
def universidad_privada8():
    return render_template('universidad_privada8.html')

@app.route('/universidades/privadas/universidad9')
def universidad_privada9():
    return render_template('universidad_privada9.html')

@app.route('/universidades/privadas/universidad10')
def universidad_privada10():
    return render_template('universidad_privada10.html')

@app.route('/universidades/privadas/universidad11')
def universidad_privada11():
    return render_template('universidad_privada11.html')

@app.route('/universidades/privadas/universidad12')
def universidad_privada12():
    return render_template('universidad_privada12.html')

@app.route('/universidades/privadas/universidad13')
def universidad_privada13():
    return render_template('universidad_privada13.html')

@app.route('/universidades/privadas/universidad14')
def universidad_privada14():
    return render_template('universidad_privada14.html')

@app.route('/universidades/privadas/universidad15')
def universidad_privada15():
    return render_template('universidad_privada15.html')

@app.route('/universidades/privadas/universidad16')
def universidad_privada16():
    return render_template('universidad_privada16.html')

@app.route('/universidades/privadas/universidad17')
def universidad_privada17():
    return render_template('universidad_privada17.html')

@app.route('/universidades/privadas/universidad18')
def universidad_privada18():
    return render_template('universidad_privada18.html')

@app.route('/universidades/privadas/universidad19')
def universidad_privada19():
    return render_template('universidad_privada19.html')

@app.route('/universidades/privadas/universidad20')
def universidad_privada20():
    return render_template('universidad_privada20.html')

@app.route('/universidades/privadas/universidad21')
def universidad_privada21():
    return render_template('universidad_privada21.html')

@app.route('/universidades/privadas/universidad22')
def universidad_privada22():
    return render_template('universidad_privada22.html')

@app.route('/universidades/privadas/universidad23')
def universidad_privada23():
    return render_template('universidad_privada23.html')

@app.route('/universidades/privadas/universidad24')
def universidad_privada24():
    return render_template('universidad_privada24.html')

@app.route('/universidades/privadas/universidad25')
def universidad_privada25():
    return render_template('universidad_privada25.html')

@app.route('/universidades/privadas/universidad26')
def universidad_privada26():
    return render_template('universidad_privada26.html')

@app.route('/universidades/privadas/universidad27')
def universidad_privada27():
    return render_template('universidad_privada27.html')
    
@app.route('/buscador', methods=['POST'])
def buscar():
    query = request.form['query'].lower()
    resultados = {nombre: enlace for nombre, enlace in universidades.items() if query in nombre.lower()}
    
    return render_template('resultados_busqueda.html', query=query, resultados=resultados)


if __name__ == '__main__':
    app.run(debug=True)

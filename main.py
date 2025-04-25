
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/converter_moeda', methods=['POST'])
def converter_moeda():
    try:
        reais = float(request.form['reais'])
        dolar = 5.69

        converterUSD = round(reais / dolar, 2)




        return render_template('index.html', converterUSD=converterUSD)
    except Exception as e:
        converterUSD = f'Ocorreu um erro inesperado {e}'

        return render_template('index.html', converterUSD=converterUSD)

if __name__ == '__main__':
    app.run(debug=True)



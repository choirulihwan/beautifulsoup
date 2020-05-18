from flask import Flask, render_template, request
from test_scraping_haji import scrap_haji

app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    # return "Bismillah"
    data = {}
    if request.method == 'POST':
        no_porsi = request.form['no_porsi']
        data['no_porsi'] = no_porsi
        data_haji = scrap_haji(no_porsi)

    return render_template('index_haji.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)


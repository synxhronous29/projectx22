from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/mahasiswa')
def getmahasiswa():
    kelas = 'IF-4201'
    return render_template('mahasiswa.html', kelas=kelas)

@app.route('/dosen')
def getdosen():
    hobi = ['membaca', 'jalan-jalan', 'nonton']
    return render_template('dosen.html', hobi=hobi)

if __name__ == '__main__':
    app.run(debug=True)

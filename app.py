from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('penjumlahan.html')

@app.route('/perkalian')
def kali():
    return render_template('perkalian.html')

@app.route('/pengurangan')
def kurang():
    return render_template('pengurangan.html')

@app.route('/pembagian')
def bagi():
    return render_template('pembagian.html')

@app.route('/penjumlahan', methods=['POST'])
def save_penjumlahan():
    bil1 = int(request.form['bil1'])
    bil2 = int(request.form['bil2'])
    hasil = bil1+bil2
    print(hasil)
    return jsonify({'message': hasil})
    
@app.route('/perkalian', methods=['POST'])
def save_perkalian():
    bil1 = int(request.form['bil1'])
    bil2 = int(request.form['bil2'])
    hasil = bil1*bil2
    print(hasil)
    return jsonify({'message': hasil})

@app.route('/pengurangan', methods=['POST'])
def save_pengurangan():
    bil1 = int(request.form['bil1'])
    bil2 = int(request.form['bil2'])
    hasil = bil1-bil2
    print(hasil)
    return jsonify({'message': hasil})
    
@app.route('/pembagian', methods=['POST'])
def save_pembagian():
    bil1 = int(request.form['bil1'])
    bil2 = int(request.form['bil2'])
    hasil = bil1 / bil2
    print('%.2f' % hasil)
    return jsonify({'message': '%.2f' % hasil})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
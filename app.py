from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    # Aquí puedes agregar lógica para manejar el formulario (por ejemplo, guardar en base de datos)
    return jsonify({'status': 'success', 'message': 'Mensaje enviado con éxito'})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

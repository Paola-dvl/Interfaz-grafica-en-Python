from flask import Flask, jsonify, request

app = Flask(__name__)
clientes = []

class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit
        
def validar_nit(nit):
    try:
        int(nit)
        return True
    except ValueError:
        return False


@app.route('/getClientes', methods=['GET'])
def get_clientes():
    global clientes
    table_html = '<table style="margin: auto; width: 50%;" border="1"><tr><th>Nombre</th><th>Correo</th><th>NIT</th></tr>'
    for cliente in clientes:
        table_html += f'<tr><td>{cliente.nombre}</td><td>{cliente.correo}</td><td>{cliente.nit}</td></tr>'
    table_html += '</table>'
    return table_html

@app.route('/agregarCliente', methods=['POST'])
def agregar_cliente():
    global clientes
    data = request.json
    correo_cliente = data.get('correo')
    nit_cliente = data.get('nit')

    if not validar_nit(nit_cliente):
        return jsonify({'error': 'El NIT solo permite ingresar numeros.'}), 400
        
    if any(cliente.nit == nit_cliente and cliente.correo == correo_cliente for cliente in clientes):
        return jsonify({'error': 'El NIT y el correo electronico ya estan siendo utilizados.'}), 400
    
    if any(cliente.nit == nit_cliente for cliente in clientes):
        return jsonify({'error': 'El NIT ya esta siendo utilizado.'}), 400

    if any(cliente.correo == correo_cliente for cliente in clientes):
        return jsonify({'error': 'El correo electronico ya esta siendo utilizado.'}), 400

    nuevo_cliente = Cliente(data['nombre'], correo_cliente, nit_cliente)
    clientes.append(nuevo_cliente)
    return jsonify({'message': 'Cliente agregado correctamente.'}), 200


if __name__ == '__main__':
    app.run(port=5000)

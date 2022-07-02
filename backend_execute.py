from app import *
from Client import Client

# Rota Inicial
@app.route("/")
def route_index():
    clientes = Client.query.all()
    return render_template("index.html",clientes = clientes)

# Rota para adição de clientes
@app.route("/add",methods = ['GET','POST'])
def route_add():
    if request.method == 'POST':
        cliente = Client(request.form['nome'], request.form['email'])
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('route_index'))
    return render_template('add.html')

# Rota para exclusão de clientes
@app.route('/delete/<int:id>')
def route_delete(id):
    cliente = Client.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('route_index'))

'''
Rota para edição de atributos de um cliente já existente
Rota Inacabada
'''
@app.route('/edit/<int:id>', methods = ['GET','POST'] )
def route_edit(id):
    cliente = Client.query.filter_by(id=id).first()
    if request.method == 'POST':
        return redirect(url_for('route_index'))
    return render_template('edit.html',cliente = cliente)

if __name__== '__main__':
    db.create_all()
    app.run(debug=True)
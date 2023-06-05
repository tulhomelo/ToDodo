import os
import psycopg2
from flask import Flask, render_template, request, url_for, flash, redirect


# cria a conexao com o BD
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="tododo",
        user=os.getenv('DB_USERNAME'),
        password=os.environ['DB_PASSWORD']
    )
    return conn

# query todos os todo no banco
def get_todo(todo_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todo WHERE id = %s', (todo_id,))
    todo = cur.fetchone()
    cur.close()
    conn.close()
    return todo

# cria o serviço
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY_DEV')

# definicao das rotas
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM todo')
    todo = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', todo=todo)

@app.route('/<int:todo_id>')
def todo(todo_id):
    todo = get_todo(todo_id)
    if todo is None:
        return render_template('404.html')
    return render_template('todo.html', todo=todo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['titulo']
        descricao = request.form['descricao']

        if not title:
            flash('Título é obrigatório!')
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO todo (titulo, descricao) VALUES (%s, %s)',
                         (titulo, descricao))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    todo = get_todo(id)

    if todo is None:
        return render_template('404.html')

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']

        if not titulo:
            flash('Título é obrigatório!')
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('UPDATE todo SET titulo = %s, descricao = %s'
                         ' WHERE id = %s',
                         (titulo, descricao, id))
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', todo=todo)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    todo = get_todo(id)
    if todo is None:
        return render_template('404.html')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM todo WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    flash('"{}" foi removido!'.format(todo[2]))
    return redirect(url_for('index'))

# inicia servico
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
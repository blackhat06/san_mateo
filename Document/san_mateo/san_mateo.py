from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        db = MySQLdb.connect(user="root", passwd="", db="cs324", host="127.0.0.1")
        c=db.cursor()
        c.executemany('''select * from student where name = %s''', request.form['search'])
        for r in c.fetchall():
            print r[0],r[1],r[2]
            return redirect(url_for('search')) # <- Here you jump away from whatever result you create
    return render_template('search.html')


if __name__ == '__main__':
    app.run()

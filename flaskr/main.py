import sqlite3
import re
import hashlib
import arrow
from flaskr import app
from flask import session
from flask import render_template, request, redirect, url_for

DATABASE = 'bbs.db'

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/add')
def add():
    return render_template(
        'add.html'
    )

@app.route('/check', methods=['POST'])
def check():
    mail_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    password_pattern = r'^(?=.*[0-9a-zA-Z\W]).{6,}$'

    userName = request.form['userName']
    password1 = request.form['password1']
    password2 = request.form['password2']
    mail = request.form['mail']
    flg = False

    if(not userName or not password1 or not password2 or not mail):
        error = '全ての項目を入力してください。'
        flg = True

    if(not password1 == password2 and flg == False):
        error = '入力されたパスワードが確認用のパスワードと異なります。'
        flg = True

    if(not re.match(password_pattern, password1) and flg == False):
        error = 'パスワードは以下の条件を満たしている必要があります。<br>- 半角英数字記号を使用<br>- 6文字以上'
        flg = True

    if(not re.match(mail_pattern, mail) and flg == False):
        error = '正しいメールアドレスの形式ではありません。'
        flg = True

    if(flg):
        return render_template(
            'add.html',
            error=error
        )
    else:
        user = {
            'userName' : request.form['userName'],
            'password' : request.form['password1'],
            'mail' : request.form['mail']
        }

        session['user'] = user

        return render_template(
            'check.html',
            user=user
        )

@app.route('/comp', methods=['POST'])
def comp():
    user = session.get('user')

    con = sqlite3.connect(DATABASE)
    existing_user = con.execute("SELECT id FROM user WHERE id = ?", (user['userName'],)).fetchone()

    if(existing_user):
        error = 'ユーザーIDが既に存在します。別のユーザーIDを設定してください。'
        con.close()
        return render_template(
            'add.html',
            error=error
        )
    else:
        hashed_password = hashlib.sha256(user['password'].encode()).hexdigest()
        con.execute('INSERT INTO user VALUES(?, ?, ?)',
                    (user['userName'], hashed_password, user['mail']))
        con.commit()
        con.close()
        return render_template(
            'comp.html'
        )
    
@app.route('/bbs', methods=['POST'])
def bbs():
    con = sqlite3.connect(DATABASE)

    userID = request.form['userID']
    password = request.form['password']

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    existing_user = con.execute("SELECT id FROM user WHERE id = ? AND pass = ?", (userID, hashed_password)).fetchone()

    con.close()

    if(existing_user):
        session['userID'] = userID

        return render_template(
            'bbs.html',
            userID=userID
        )
    else:
        error = 'ユーザーIDかパスワードが間違っています。'
        
        return render_template(
            'index.html',
            error=error
        )
    
@app.route('/all')
def all():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_all').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'all.html',
        userID=userID,
        posts=posts
    )

@app.route('/music')
def music():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_music').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'music.html',
        userID=userID,
        posts=posts
    )

@app.route('/animal')
def animal():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_animal').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'animal.html',
        userID=userID,
        posts=posts
    )

@app.route('/cooking')
def cooking():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_cooking').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'cooking.html',
        userID=userID,
        posts=posts
    )

@app.route('/travel')
def travel():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_travel').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'travel.html',
        userID=userID,
        posts=posts
    )

@app.route('/sports')
def sports():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_sports').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'sports.html',
        userID=userID,
        posts=posts
    )

@app.route('/politics')
def politics():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_politics').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'politics.html',
        userID=userID,
        posts=posts
    )

@app.route('/technology')
def technology():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_technology').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'technology.html',
        userID=userID,
        posts=posts
    )

@app.route('/others')
def others():
    userID = session.get('userID')

    con = sqlite3.connect(DATABASE)
    post_data = con.execute('SELECT * FROM bbs_others').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'others.html',
        userID=userID,
        posts=posts
    )

@app.route('/all_add', methods=['POST'])
def all_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_all (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_all').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'all.html',
        userID=userID,
        posts=posts
    )

@app.route('/music_add', methods=['POST'])
def music_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_music (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_music').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'music.html',
        userID=userID,
        posts=posts
    )

@app.route('/animal_add', methods=['POST'])
def animal_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_animal (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_animal').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'animal.html',
        userID=userID,
        posts=posts
    )

@app.route('/cooking_add', methods=['POST'])
def cooking_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_cooking (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_cooking').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'cooking.html',
        userID=userID,
        posts=posts
    )

@app.route('/travel_add', methods=['POST'])
def travel_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_travel (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_travel').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'travel.html',
        userID=userID,
        posts=posts
    )

@app.route('/sports_add', methods=['POST'])
def sports_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_sports (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_sports').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'sports.html',
        userID=userID,
        posts=posts
    )

@app.route('/politics_add', methods=['POST'])
def politics_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_politics (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_politics').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'politics.html',
        userID=userID,
        posts=posts
    )

@app.route('/technology_add', methods=['POST'])
def technology_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_technology (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_technology').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'technology.html',
        userID=userID,
        posts=posts
    )

@app.route('/others_add', methods=['POST'])
def others_add():
    userID = session.get('userID')
    post = request.form['post']
    
    now = arrow.now()
    current_date = now.format('YYYY-MM-DD')
    current_time = now.format('HH:mm:ss')
    
    con = sqlite3.connect(DATABASE)
    
    con.execute("INSERT INTO bbs_others (id, date, time, post) VALUES (?, ?, ?, ?)",
                (userID, current_date, current_time, post))
    con.commit()
    
    post_data = con.execute('SELECT * FROM bbs_others').fetchall()
    con.close()

    posts = []
    for row in post_data:
        posts.append({'no': row[0], 'id': row[1], 'date': row[2], 'time': row[3], 'post': row[4]})
    
    return render_template(
        'others.html',
        userID=userID,
        posts=posts
    )

@app.route('/index_back')
def index_back():
    return redirect(
        url_for('index')
    )

@app.route('/add_back')
def add_back():
    return redirect(
        url_for('add')
    )

@app.route('/bbs_back')
def bbs_back():
    userID = session.get('userID')
    return render_template(
        'bbs.html',
        userID=userID
    )

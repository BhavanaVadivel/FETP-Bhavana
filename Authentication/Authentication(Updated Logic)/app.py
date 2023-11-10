from flask import Flask, render_template, redirect, url_for, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        session['user'] = {
            "name": username,
            "email": email,
        }

        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    user = session['user']
    current_time = get_current_time()

    return render_template('home.html', user=user, current_time=current_time)

@app.route('/logout')
def logout():
    if 'user' in session:
        user_name = session['user']['name']
        print(f"User '{user_name}' has logged out.")
        session.pop('user', None)

    return redirect(url_for('login'))

def get_current_time():
    # To get the current Indian time
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

if __name__ == '__main__':
    app.run(debug=True)

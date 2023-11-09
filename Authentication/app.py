from flask import Flask, render_template, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'  

# User data 
user = {
    "name": "Bhavana Vadivel",
    "email": "bhavanavadivel02@gmail.com",
   # "profile_picture": "icon.jpg",  
}

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    return render_template('index.html', user=session['user'], current_time=get_current_time())
    return redirect(url_for('home'))


@app.route('/login')
def login():
    session['user'] = user 
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    if 'user' in session:
        # Perform additional logout actions here
        user_name = session['user']['name']
        print(f"User '{user_name}' has logged out.")

        # Clear the user session
        session.pop('user', None)

    # Redirect to the home page
    return redirect(url_for('home'))



def get_current_time():
    # To get the current Indian time
      return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

if __name__ == '__main__':
    app.run(debug=True)
   


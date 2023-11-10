from flask import Flask, render_template, request

app = Flask(__name__)

def generate_pattern(text):
    letters = text.upper()
    index = len(letters)

    pattern = ""
    for i in range(1, index * 2):
        if i <= index:
            line = letters[index - i:index]
        else:
            line = letters[i - index:i - index + index]
        pattern += line.center(index * 2 - 1) + "\n"

    return pattern

@app.route('/')
def home():
    authenticated = True  
    return render_template('index.html', authenticated=authenticated)

@app.route('/display', methods=['POST'])
def display():
    if request.method == 'POST':
        user_text = request.form['user_text']
        pattern = generate_pattern(user_text)
        return render_template('display.html', pattern=pattern)

if __name__ == "__main__":
    app.run(debug=True)








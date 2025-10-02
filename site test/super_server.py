import serial
from flask import Flask, render_template, request, redirect, url_for

# arduino = serial.Serial(port='COM35',  baudrate=115200, timeout=.1)
app = Flask(__name__)

LedState = False
# Dummy credentials
VALID_USERNAME = 'rigby'
VALID_PASSWORD = 'rigby'
def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return  data

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return redirect(url_for('connected', username=username))
        else:
            return redirect(url_for('error'))

    return render_template('login.html', error=error)

@app.route('/connected', methods=['GET'])
def connected():
    username = request.args.get('username', 'Admin')
    return render_template('connected.html', username=username)


@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/map')
def map():
    return render_template('rigbyMap.hmtl')

if __name__ == '__main__':
    app.run(debug=True)
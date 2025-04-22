from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login')  # Add the /login route
def maintenance():
    return render_template('maintenance.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  # Use 8000 or 3000 depending on your Koyeb setup
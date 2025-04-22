from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login')  # Serve maintenance page at /login as requested
def maintenance():
    return render_template('maintenance.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Changed to port 3000
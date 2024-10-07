from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<room_name>')
def index(room_name):
    return render_template('index.html', room_name=room_name.capitalize(), reserved=False)

@app.route('/<room_name>/reserve', methods=['POST'])
def reserve(room_name):
    duration = int(request.form.get('duration', 0))
    return render_template('index.html', room_name=room_name.capitalize(), reserved=True, duration=duration)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

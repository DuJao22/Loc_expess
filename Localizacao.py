from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Store the latest location
latest_location = {'latitude': 0, 'longitude': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    global latest_location
    data = request.json
    latest_location = {
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }
    return jsonify(success=True)

@app.route('/get_location', methods=['GET'])
def get_location():
    return jsonify(latest_location)

if __name__ == '__main__':
    app.run(debug=True)
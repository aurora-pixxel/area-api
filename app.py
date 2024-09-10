from flask import Flask, request, jsonify
from area import area

app = Flask(__name__)

@app.route('/calculate-area', methods=['POST'])
def calculate_area():
    try:
        # The GeoJSON data is expected in the request body
        geojson = request.json
        polygon_area = area(geojson)
        return jsonify({'area': polygon_area})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import compare  # your compare.py script

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare_image():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No image uploaded'}), 400

    filepath = 'temp.jpg'
    file.save(filepath)

    result = compare.find_best_match(filepath)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Conversion data
conversion_factors = {
    "length": {"meter": 1, "kilometer": 0.001, "mile": 0.000621371, "foot": 3.28084},
    "weight": {"kilogram": 1, "gram": 1000, "pound": 2.20462, "ounce": 35.274},
    "temperature": {},  # Handled separately
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    return value  # No conversion needed

@app.route('/convert', methods=['GET'])
def convert():
    category = request.args.get('category')
    value = float(request.args.get('value'))
    from_unit = request.args.get('from')
    to_unit = request.args.get('to')

    if category == "temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        factor = conversion_factors.get(category, {}).get(to_unit, 1) / conversion_factors.get(category, {}).get(from_unit, 1)
        result = value * factor

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

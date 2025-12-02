from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Helper functions to read files
def read_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv_file(filename):
    products = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert price and id to proper types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')

    products_list = []
    error = None

    # Validate source and read data
    if source == 'json':
        products_list = read_json_file('products.json')
    elif source == 'csv':
        products_list = read_csv_file('products.csv')
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Filter by ID if provided
    if id_param:
        try:
            id_int = int(id_param)
            filtered = [p for p in products_list if p['id'] == id_int]
            if not filtered:
                error = "Product not found"
            products_list = filtered
        except ValueError:
            error = "Invalid ID"

    return render_template('product_display.html', products=products_list, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

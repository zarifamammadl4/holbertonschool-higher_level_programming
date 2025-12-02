from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Helper functions
def read_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def read_csv_file(filename):
    products = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite_db(db_file):
    products = []
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')
    products_list = []
    error = None

    # Read data based on source
    if source == 'json':
        products_list = read_json_file('products.json')
    elif source == 'csv':
        products_list = read_csv_file('products.csv')
    elif source == 'sql':
        products_list = read_sqlite_db('products.db')
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

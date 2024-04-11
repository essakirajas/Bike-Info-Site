from flask import Flask, render_template, request

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bikes')
def bikes():
    # Logic to fetch bike data from the database
    bikes_data = [
        {'name': 'Road Bike 1', 'brand': 'Brand A', 'type': 'Road', 'price': 1000},
        {'name': 'Mountain Bike 1', 'brand': 'Brand B', 'type': 'Mountain', 'price': 1500},
        {'name': 'Hybrid Bike 1', 'brand': 'Brand C', 'type': 'Hybrid', 'price': 800}
    ]
    return render_template('bikes.html', bikes=bikes_data)

@app.route('/bike/<bike_id>')
def bike_details(bike_id):
    # Logic to fetch bike details from the database based on the bike_id
    bike_details = {'name': 'Road Bike 1', 'brand': 'Brand A', 'type': 'Road', 'price': 1000, 'description': 'Lorem ipsum dolor sit amet...'}
    return render_template('bike_details.html', bike=bike_details)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        # Logic to perform the search in the bike database based on the search_query
        search_results = [
            {'name': 'Road Bike 1', 'brand': 'Brand A', 'type': 'Road', 'price': 1000},
            {'name': 'Road Bike 2', 'brand': 'Brand B', 'type': 'Road', 'price': 1200}
        ]
        return render_template('search_results.html', search_results=search_results, query=search_query)
    else:
        return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)

from pyrebase import pyrebase

config = {
	"apiKey": "#############",
  "authDomain": "##########",
  "projectId": "########",
  "databaseURL": "$$$$$$$",
  "storageBucket": "$$$$$$$$$",
  "messagingSenderId": "$$$$$$$$$$",
  "appId": "$$$$$$$$$",
  "measurementId": "$$$$$$$$$$$"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def browse_brands():
    brands = db.child('brands').get().val()
    return render_template('index.html', brands=brands)

@app.route('/brand/<brand>', methods=['GET', 'POST'])
def brand_bikes(brand):
    brand_details = db.child('bikes').child(brand).get().val()
    bikes = db.child('bikes').child(brand).get().val()
    return render_template('brand_bikes.html', brand=brand_details, bikes=bikes)

@app.route('/bike/<bike_id>', methods=['GET', 'POST'])
def bike_details(bike_id):
    bike = db.child('bike').child(bike_id).get().val()
    reviews = db.child('reviews').child(bike_id).get().val()
    if request.method == 'POST':
        user = request.form['user']
        rating = request.form['rating']
        comment = request.form['comment']
        review = {
            'user': user,
            'rating': rating,
            'comment': comment
        }
        db.child('bikes').child(bike_id).child('reviews').push(review)
        
        flash('Your review has been submitted!', 'success')
        return redirect(url_for('bike_details', bike_id=bike_id))
    
    return render_template('bike_details.html', bike=bike, reviews=reviews)



if __name__ == '__main__':
    app.secret_key = '1234567890'
    app.run(debug=True)

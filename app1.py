from flask import Flask, render_template, request

app = Flask(__name__)


# Bike brands and their details
brand = {
    'Brand1': {
        'name': 'Brand 1',
        'description': 'Brand 1 is known for its high-quality mountain and road bikes. With their innovative designs and durable components, Brand 1 bikes offer a thrilling riding experience.',
        'logo_url': "{{ url_for('static', filename='re.jpg') }}"
    },
    'Brand2': {
        'name': 'Brand 2',
        'description': 'Brand 2 specializes in hybrid and electric bikes, catering to urban commuters and eco-conscious riders. Their bikes combine style, functionality, and sustainability.',
        'logo_url': 'brand2_logo.png'
    },
    'Brand3': {
        'name': 'Brand 3',
        'description': 'Brand 3 is a renowned name in the cruiser and BMX bike industry. Their bikes are known for their retro designs, comfort, and versatility, making them ideal for casual rides and stunts.',
        'logo_url': 'brand3_logo.png'
    },
    'Brand4': {
        'name': 'Brand 3',
        'description': 'Brand 3 is a renowned name in the cruiser and BMX bike industry. Their bikes are known for their retro designs, comfort, and versatility, making them ideal for casual rides and stunts.',
        'logo_url': 'brand3_logo.png'
    },
    'Brand5': {
        'name': 'Brand 3',
        'description': 'Brand 3 is a renowned name in the cruiser and BMX bike industry. Their bikes are known for their retro designs, comfort, and versatility, making them ideal for casual rides and stunts.',
        'logo_url': 'brand3_logo.png'
    },
    'Brand6': {
        'name': 'Brand 3',
        'description': 'Brand 3 is a renowned name in the cruiser and BMX bike industry. Their bikes are known for their retro designs, comfort, and versatility, making them ideal for casual rides and stunts.',
        'logo_url': 'brand3_logo.png'
    }
}

# Route for the browse brands page
@app.route('/')
def browse_brands():
    return render_template('index.html')

# Route for the brand bikes listing page
@app.route('/brand/<brand>')
def brand_bikes(brand):
    # Here, you would query your database or data source to retrieve the bikes for the selected brand
    # You can pass the list of bikes to the template for rendering
    bikes = get_bikes_by_brand(brand)  # Replace this with your own logic
    brands=get_bikes_by_det(brand)

    return render_template('brand_bikes.html', brand=brands, bikes=bikes)

def get_bikes_by_det(brand):
    brands=[]
    if brand == 'Brand1':
        brands={
        'name': 'Royal Enfield Bikes',
        'description': 'Royal Enfield bike price starts from Rs. 1,49,900. Royal Enfield offers 9 new models in India with most popular bikes being Hunter 350, Classic 350 and Bullet 350. The upcoming bikes of Royal Enfield include Bullet 350 Next Gen, Himalayan 650 and Himalayan 450. Most expensive Royal Enfield bike is Super Meteor 650, which is priced at Rs. 3,54,398.',
        'logo_url': 're.jpg'
    }
        
    elif brand == 'Brand2':
        brands={
        'name': 'Bajaj',
        'description': 'Bajaj bike price starts from Rs. 65,943. Bajaj offers 20 new models in India with most popular bikes being Pulsar 125, Pulsar 150 and Pulsar N160. Most expensive Bajaj bike is Dominar 400, which is priced at Rs. 2,24,916.Bajaj Motorcycles is one of the largest motorcycle manufacturers in India. Based out of Pune, Bajaj has manufacturing plants in Chakan, Waluj in Maharashtra and Pantnagar in Uttarakhand. Its oldest plant in Akurdi, Pune currently houses company’s corporate office and research & development centre.',
        'logo_url': 'bajaj.jpg'
    }
    elif brand == 'Brand3':
        brands={
        'name': 'KTM',
        'description': 'KTM bike price starts from Rs. 1,78,984. KTM offers 10 new models in India with most popular bikes being 200 Duke, 390 Duke and 250 Duke. The upcoming bikes of KTM include 390 Duke [2024] and 650 Duke. Most expensive KTM bike is 390 Adventure, which is priced at Rs. 3,39,247.In 1953, businessman Ernst Kronreif became a sizable shareholder Kraftfahrzeug Trunkenpolz Mattighofen which was then renamed and registered as Kronreif and Trunkenpolz Mattighofen. KTM started serial production of R100 in 1954. With just 20 employees, motorcycles were built at the rate of three per day.',
        'logo_url': 'ktm.jpg'
    }
    elif brand == 'Brand4':
        brands={
        'name': 'TVS',
        'description': 'TVS bike price starts from Rs. 44,227. TVS offers 18 new models in India with most popular bikes being Raider 125, Apache RTR 160 and Apache RTR 160 4V. The upcoming bikes of TVS include Apache RTR 310 and Creon. Most expensive TVS bike is Apache RR310, which is priced at Rs. 2,71,825.TVS was established by T. V. Sundaram Iyengar. He was born in 1877 in Thirukkurungudi in the Tirunelveli district of Madras Presidency, British India. He began with Madurai first bus service in 1911 and founded T.V.Sundaram Iyengar and Sons Limited, a company in the transportation business with a large fleet of trucks and buses under the name of Southern Roadways Limited.',
        'logo_url': 'tvs.jpg'
    }
    elif brand == 'Brand5':
        brands={
        'name': 'Suzuki',
        'description': 'Suzuki bike price starts from Rs. 81,698. Suzuki offers 11 new models in India with most popular bikes being Gixxer SF, Access 125 and Burgman Street 125. The upcoming bikes of Suzuki include Burgman Street Electric, Suzuki GSX-8S and V-Strom 800DE. Most expensive Suzuki bike is Hayabusa, which is priced at Rs. 16,97,240.Suzuki Motor Corporation (SMC), a global giant of motorcycle manufacturing is headquartered in Japan. It holds major stake in its Indian subsidiary, Suzuki Motorcycle India Private Limited (SMIL). SMIL was set up after Suzuki re-entry into the Indian two-wheeler market after it severed ties with partner TVS in 2000-01. Suzuki was then the technology provider in the former joint venture company TVS Suzuki.',
        'logo_url': 'suzuki.jpg'
    }
    elif brand == 'Brand6':
        brands={
        'name': 'Yamaha',
        'description': 'Yamaha bike price starts from Rs. 80,970. Yamaha offers 11 new models in India with most popular bikes being MT 15 V2, FZ S FI and FZ FI. The upcoming bikes of Yamaha include MT-03, YZF-R3 and YZF-R7. Most expensive Yamaha bike is R15 V4, which is priced at Rs. 1,81,704.Yamaha derived its name from Torakusu Yamaha, the company’s founder. It started off by manufacturing Western musical instruments in Japan back 1887, and it wasn’t till 1955 that the company’s motorcycle division was set up. While Yamaha still manufactures musical instruments, with the distinction of being regarded as one of the leading names in the field, it also forms one fourth of the big four Japanese manufacturers in the two-wheeler industry.',
        'logo_url': 'yamaha.jpg'
    }
    
    return brands


# Helper function to get bikes by brand from the database or data source
# Helper function to get bikes by brand from the database or data source
def get_bikes_by_brand(brand):
    # Replace this with your own logic to fetch the bikes from your data source
    # Return a list of bikes for the specified brand
    # Each bike should be a dictionary with attributes like 'name', 'image_url', 'type', 'price', etc.
    # Example:
    bikes = []

    if brand == 'Brand1':

        bikes = [
            {
                'name': 'Royal Enfield Hunter 350 ',
                'image_url': 're1.webp',
                'type': 'Retro Factory',
                'price': '₹ 1,49,900 onwards'
            },
            {
                'name': 'Royal Enfield Classic 350',
                'image_url': 're2.webp',
                'type': 'Redditch - Single Channel ABS',
                'price': '₹ 1,93,080'
            },
             {
                'name': 'Royal Enfield Bullet 350',
                'image_url': 're3.webp',
                'type': 'Standard',
                'price': '₹ 1,50,894'
            },
            {
                'name': 'Royal Enfield Continental GT 650',
                'image_url': 're4.webp',
                'type': 'Standard - BS VI',
                'price': '₹ 3,18,417 '
            },
            {
                'name': 'Royal Enfield Himalayan',
                'image_url': 're5.webp',
                'type': 'Standard - BS VI',
                'price': '₹ 2,15,881'
            }
            # Add more bikes for Brand1 here
        ]
    elif brand == 'Brand2':
        bikes = [
            {
                'name': 'Bike3',
                'image_url': 'brand2_bike1.jpg',
                'type': 'Hybrid Bike',
                'price': 800
            },
            {
                'name': 'Bike4',
                'image_url': 'brand2_bike2.jpg',
                'type': 'Electric Bike',
                'price': 2000
            },
            # Add more bikes for Brand2 here
        ]
    elif brand == 'Brand3':
        bikes = [
            {
                'name': 'Bike5',
                'image_url': 'brand3_bike1.jpg',
                'type': 'Cruiser Bike',
                'price': 700
            },
            {
                'name': 'Bike6',
                'image_url': 'brand3_bike2.jpg',
                'type': 'BMX Bike',
                'price': 500
            },
            # Add more bikes for Brand3 here
        ]
    elif brand == 'Brand4':
        bikes = [
            {
                'name': 'Bike5',
                'image_url': 'brand3_bike1.jpg',
                'type': 'Cruiser Bike',
                'price': 700
            },
            {
                'name': 'Bike6',
                'image_url': 'brand3_bike2.jpg',
                'type': 'BMX Bike',
                'price': 500
            },
            # Add more bikes for Brand3 here
        ]

    elif brand == 'Brand5':
        bikes = [
            {
                'name': 'Bike5',
                'image_url': 'brand3_bike1.jpg',
                'type': 'Cruiser Bike',
                'price': 700
            },
            {
                'name': 'Bike6',
                'image_url': 'brand3_bike2.jpg',
                'type': 'BMX Bike',
                'price': 500
            },
            # Add more bikes for Brand3 here
        ]
    elif brand == 'Brand6':
        bikes = [
            {
                'name': 'Bike5',
                'image_url': 'brand3_bike1.jpg',
                'type': 'Cruiser Bike',
                'price': 700
            },
            {
                'name': 'Bike6',
                'image_url': 'brand3_bike2.jpg',
                'type': 'BMX Bike',
                'price': 500
            },
            # Add more bikes for Brand3 here
        ]

    return bikes




if __name__ == '__main__':
    app.run(debug=True)

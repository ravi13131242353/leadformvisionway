from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://ravi1901275:arsh143ravi@cluster0.awcacoq.mongodb.net/")
db = client["formdata"]  # Change to your database name
collection = db["DATA"]

# Route for login page (POST for form submission)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']

        # Check if the password matches
        if password != '1234':  # Change to the correct password logic
            return render_template("login.html", error="Invalid credentials")
        else:
            return redirect(url_for('index'))  # Redirect to index after successful login
    return render_template("login.html")

# Route for the index page (Form submission page)
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect form data
        first_name = request.form.get('f_name', '')
        last_name = request.form.get('l_name', '')
        email = request.form.get('email', '')
        phone_number = request.form.get('p_number', '')
        # Collect other fields...

        document = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            # Add other fields here...
        }

        try:
            # Insert data into MongoDB
            collection.insert_one(document)
        except Exception as e:
            print(f"Error inserting document: {e}")
            return "Error inserting data"

        return redirect(url_for('thank_you'))  # Redirect to the thank_you page after form submission

    return render_template('index.html')

# Route for the thank you page
@app.route('/thank_you')
def thank_you():
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

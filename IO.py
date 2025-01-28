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
        first_name = request.form.get('f_name', '')
        middle_name = request.form.get('m_name', '')
        last_name = request.form.get('l_name', '')
        date_of_birth = request.form.get('dob', '')
        email = request.form.get('email', '')
        phone_number = request.form.get('p_number', '')
        whatsapp_number = request.form.get('w_number', '')
        marital_status = request.form.get('marital_status', '')
        address = request.form.get('address', '')
        citizenship_country = request.form.get("citizenship_country", '')
        pin_code = request.form.get('pin_code', '')
        state = request.form.get("state", '')
        city = request.form.get("city", '')
        country_of_interest = request.form.get("country_of_interest", '')
        gender = request.form.get("gender", '')
        referral = request.form.get("referral", '')
        lead_status = request.form.get("lead_status", '')
        service_interest = request.form.get("service_interest", '')
        visa_type = request.form.get("visa_type", '')
        higher_qualification = request.form.get("higher_qualification", '')
        highest_qualification = request.form.get("highest_qualification", '')
        education_level = request.form.get("education_level", '')
        qualification = request.form.get("qualification", '')
        sub_discipline = request.form.get("subDiscipline", '')
        pass_status = request.form.get("pass_status", '')
        grading_scheme = request.form.get("grading_scheme", '')
        gpa = request.form.get("gpa", '')
        cgpa = request.form.get("cgpa", '')
        percentage = request.form.get("percentage", '')
        grade = request.form.get("grade", '')
        institute_name = request.form.get("institute_name", '')
        edu_start_date = request.form.get("edu_start_date", '')
        edu_level = request.form.get("edu_level", '')
        institution_country = request.form.get("institution_country", '')
        visa_rejection = request.form.get("visa_rejection", '')
        visa_rejection_reason = request.form.get("visa_rejection_reason", '') if visa_rejection == "Yes" else ""
        
        # Other form fields
        ielts_overall_score = request.form.get("ielts_overall", '')
        ielts_listening_score = request.form.get("ielts_listening", '')
        # ... (handle all other form fields similarly)

        document = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'email': email,
            'phone_number': phone_number,
            'whatsapp_number': whatsapp_number,
            'marital_status': marital_status,
            'address': address,
            'citizenship_country': citizenship_country,
            'pin_code': pin_code,
            'state': state,
            'city': city,
            'country_of_interest': country_of_interest,
            'gender': gender,
            'referral': referral,
            'lead_status': lead_status,
            'service_interest': service_interest,
            'visa_type': visa_type,
            'higher_qualification': higher_qualification,
            'highest_qualification': highest_qualification,
            'education_level': education_level,
            'qualification': qualification,
            'sub_discipline': sub_discipline,
            'pass_status': pass_status,
            'grading_scheme': grading_scheme,
            'gpa': gpa,
            'cgpa': cgpa,
            'percentage': percentage,
            'grade': grade,
            'institute_name': institute_name,
            'edu_start_date': edu_start_date,
            'edu_level': edu_level,
            'institution_country': institution_country,
            'visa_rejection': visa_rejection,
            'visa_rejection_reason': visa_rejection_reason,
            'ielts_overall_score': ielts_overall_score,
            'ielts_listening_score': ielts_listening_score,
            # Add other fields similarly...
        }

        try:
            collection.insert_one(document)
        except Exception as e:
            print(f"Error inserting document: {e}")
            return "Error inserting data"

        return redirect(url_for('thank_you'))  # Redirect to the thank_you page
    return render_template('index.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

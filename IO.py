from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://ravi:arsh143ravi@cluster0.awcacoq.mongodb.net/")  # Change the MongoDB URI as needed
db = client["formdata"]  # Change to your database name
collection = db["gagan"] 

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['uname']
    password = request.form['psw']

    # Replace 'your_password' with the correct password
    if password != '1234':
         return render_template("login.html")
    else:
        return redirect(url_for('index'))

@app.route('/index',methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form['f_name']
        middle_name = request.form['m_name']
        last_name = request.form['l_name']
        date_of_birth = request.form['dob']
        email = request.form['email']
        phone_number = request.form['p_number']
        whatsapp_number = request.form['w_number']
        marital_status = request.form['marital_status']
        address = request.form['address']
        citizenship_country = request.form.get("citizenship_country")
        pin_code = request.form['pin_code']
        state = request.form.get("state")
        city = request.form.get("city")
        country_of_interest = request.form.get("country_of_interest")
        gender = request.form.get("gender")
        referral = request.form.get("referral")
        lead_status = request.form.get("lead_status")
        service_interest = request.form.get("service_interest")
        visa_type = request.form.get("visa_type")
        higher_qualification = request.form.get("higher_qualification")
        highest_qualification = request.form.get("highest_qualification")
        education_level = request.form.get("education_level")
        qualification = request.form.get("qualification")
        sub_discipline = request.form.get("subDiscipline")
        pass_status = request.form.get("pass_status")
        grading_scheme = request.form.get("grading_scheme")
        gpa = request.form.get("gpa")
        cgpa = request.form.get("cgpa")
        percentage = request.form.get("percentage")
        grade = request.form.get("grade")
        institute_name = request.form.get("institute_name")
        edu_start_date = request.form.get("edu_start_date")
        edu_level = request.form.get("edu_level")
        institution_country = request.form.get("institution_country")
        visa_rejection = request.form.get("visa_rejection")
        visa_rejection_reason = request.form.get("visa_rejection_reason")
        ielts_overall_score = request.form.get("ielts_overall")
        ielts_listening_score = request.form.get("ielts_listening")
        ielts_reading_score = request.form.get("ielts_reading")
        ielts_writing_score = request.form.get("ielts_writing")
        ielts_writing_score = request.form.get("ielts_speaking")
        toefl_overall_score = request.form.get("toefl_overall")
        toefl_listening_score = request.form.get("toefl_listening")
        toefl_reading_score = request.form.get("toefl_reading")
        toefl_writing_score = request.form.get("toefl_writing")
        toefl_writing_score = request.form.get("toefl_speaking")
        pte_overall_score = request.form.get("pte_overall")
        pte_listening_score = request.form.get("pte_listening")
        pte_reading_score = request.form.get("pte_reading")
        pte_writing_score = request.form.get("pte_writing")
        pte_writing_score = request.form.get("pte_speaking")
        ielts_ukvi_overall_score = request.form.get("ielts_ukvi_overall")
        ielts_ukvi_listening_score = request.form.get("ielts_ukvi_listening")
        ielts_ukvi_reading_score = request.form.get("ielts_ukvi_reading")
        ielts_ukvi_writing_score = request.form.get("ielts_ukvi_writing") 
        pte_ukvi_overall_score = request.form.get("pte_ukvi_overall")
        pte_ukvi_listening_score = request.form.get("pte_ukvi_listening") 
        pte_ukvi_reading_score = request.form.get("pte_ukvi_reading")
        pte_ukvi_writing_score = request.form.get("pte_ukvi_writing")
        duolingo_overall_score = request.form.get("duolingo_overall")
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
            "citizenship_country": citizenship_country,
            "state": state,
            "city": city,
            "pin_code":pin_code,
            "country_of_interest": country_of_interest,
            "gender": gender,
            "referral": referral,
            "lead_status": lead_status,
            "service_interest": service_interest,
            "visa_type": visa_type,
            "higher_qualification": higher_qualification,
            "highest_qualification": highest_qualification,
            "education_level": education_level,
            "sub_discipline": sub_discipline,
            "pass_status": pass_status,
            "grading_scheme": grading_scheme,
            "gpa": gpa,
            "cgpa": cgpa,
            "percentage": percentage,
            "grade": grade,
            "institute_name": institute_name,
            "edu_start_date": edu_start_date,
            "edu_level": edu_level,
            "institution_country": institution_country,
            "visa_rejection": visa_rejection,
            "visa_rejection_reason": visa_rejection_reason if visa_rejection == "Yes" else "",
            "ielts_overall_score": ielts_overall_score,
    "ielts_listening_score": ielts_listening_score,
    "ielts_reading_score": ielts_reading_score,
    "ielts_writing_score": ielts_writing_score,
    "toefl_overall_score": toefl_overall_score,
    "toefl_listening_score": toefl_listening_score,
    "toefl_reading_score": toefl_reading_score,
    "toefl_writing_score": toefl_writing_score,
    "pte_overall_score": pte_overall_score,
    "pte_listening_score": pte_listening_score,
    "pte_reading_score": pte_reading_score,
    "pte_writing_score": pte_writing_score,
    "ielts_ukvi_overall_score": ielts_ukvi_overall_score,
    "ielts_ukvi_listening_score": ielts_ukvi_listening_score,
    "ielts_ukvi_reading_score": ielts_ukvi_reading_score,
    "ielts_ukvi_writing_score": ielts_ukvi_writing_score,
    "pte_ukvi_overall_score": pte_ukvi_overall_score,
    "pte_ukvi_listening_score": pte_ukvi_listening_score,
    "pte_ukvi_reading_score": pte_ukvi_reading_score,
    "pte_ukvi_writing_score": pte_ukvi_writing_score,
    "duolingo_overall_score": duolingo_overall_score
        }
    
        collection.insert_one(document)
        return redirect(url_for('thank_you'))  # Redirect to the thank_you page

    return render_template("index.html")  # Render the HTML form

@app.route('/thank_you', methods=['GET'])
def thank_you():
    return render_template("thanks.html")  # Render the thank_you.html template

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

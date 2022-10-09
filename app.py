import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
        annual_inc = float(request.form["annual_inc"])
        fico_range_high = float(request.form["fico_range_high"])
        int_rate = float(request.form["int_rate"])
        loan_amnt = float(request.form["loan_amnt"])
        num_actv_bc_tl = float(request.form["num_actv_bc_tl"])
        mort_acc = float(request.form["mort_acc"])
        tot_cur_bal = float(request.form["tot_cur_bal"])
        open_acc = float(request.form["open_acc"])
        pub_rec = float(request.form["pub_rec"])
        revol_bal = float(request.form["revol_bal"])
        revol_util = float(request.form["revol_util"])
        term = float(request.form["term"])
        total_acc = float(request.form["total_acc"])
        installment = float(request.form["installment"])
        dti = float(request.form["dti"])

        grade = request.form["grade"]

        if (grade=='B'):
            grade_B = 1
            grade_C = 0
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 0
        elif (grade=='C'):
            grade_B = 0
            grade_C = 1
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 0
        elif (grade=='D'):
            grade_B = 0
            grade_C = 0
            grade_D = 1
            grade_E = 0
            grade_F = 0
            grade_G = 0
        elif (grade=='E'):
            grade_B = 0
            grade_C = 0
            grade_D = 0
            grade_E = 1
            grade_F = 0
            grade_G = 0
        elif (grade=='F'):
            grade_B = 0
            grade_C = 0
            grade_D = 0
            grade_E = 0
            grade_F = 1
            grade_G = 0
        elif (grade=='G'):
            grade_B = 0
            grade_C = 0
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 1
        else :
            grade_B = 0
            grade_C = 0
            grade_D = 0
            grade_E = 0
            grade_F = 0
            grade_G = 0
        initial_list_status = request.form['initial_list_status']
        if initial_list_status == 'W':
            initial_list_status_w = 1
        else:
            initial_list_status_w = 0

        home_ownership = request.form['home_ownership']
        if home_ownership == 'Mortage':
            home_ownership_RENT = 0
            home_ownership_OWN = 0
            home_ownership_OTHER = 0
        elif home_ownership == 'Rent':
            home_ownership_RENT = 1
            home_ownership_OWN = 0
            home_ownership_OTHER = 0
        elif home_ownership == 'Own':
            home_ownership_RENT = 0
            home_ownership_OWN = 1
            home_ownership_OTHER = 0
        elif home_ownership == 'Other':
            home_ownership_RENT = 0
            home_ownership_OWN = 0
            home_ownership_OTHER = 1
        else :
            home_ownership_RENT = 0
            home_ownership_OWN = 0
            home_ownership_OTHER = 0

        application_type = request.form['application_type']
        if application_type == 'Joint App':
            application_type_JointApp = 1
        else:
            application_type_JointApp = 0

        verification_status = request.form['verification_status']
        if verification_status == 'Verified':
            verification_status_SourceVerified = 0
            verification_status_Verified = 1
        elif verification_status == 'Not Verified':
            verification_status_SourceVerified = 1
            verification_status_Verified = 0
        else:
            verification_status_SourceVerified = 0
            verification_status_Verified = 0

        purpose = request.form['purpose']
        if purpose == 'Credit Card':
            purpose_credit_card = 1
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'Debt Consolidation':
            purpose_credit_card = 0
            purpose_debt_consolidation = 1
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'Educational':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 1
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'Home Improvement':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 1
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'House':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 1
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'Major Purchase':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 1
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'Medical':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 1
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'Moving':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 1
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0
        elif purpose == 'Other':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 1
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0        
        elif purpose == 'Renewable Energy':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 1
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0     
        elif purpose == 'Small Business':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 1
            purpose_vacation = 0
            purpose_wedding = 0  
        elif purpose == 'Vacation':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 1
            purpose_wedding = 0   
        elif purpose == 'Wedding':
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 1
        else:
            purpose_credit_card = 0
            purpose_debt_consolidation = 0
            purpose_educational = 0
            purpose_home_improvement = 0
            purpose_house = 0
            purpose_major_purchase = 0
            purpose_medical = 0
            purpose_moving = 0
            purpose_other = 0
            purpose_renewable_energy = 0
            purpose_small_business = 0
            purpose_vacation = 0
            purpose_wedding = 0

        features = [annual_inc, fico_range_high, int_rate, loan_amnt,
       num_actv_bc_tl,mort_acc, tot_cur_bal, open_acc,
       pub_rec, revol_bal, revol_util, term, total_acc,
       installment, dti, grade_B, grade_C, grade_D, grade_E,
       grade_F, grade_G, verification_status_SourceVerified,
       verification_status_Verified, purpose_credit_card,
       purpose_debt_consolidation, purpose_educational,
       purpose_home_improvement, purpose_house, purpose_major_purchase,
       purpose_medical, purpose_moving, purpose_other,
       purpose_renewable_energy, purpose_small_business,
       purpose_vacation, purpose_wedding, initial_list_status_w,
       application_type_JointApp, home_ownership_OTHER,
       home_ownership_OWN, home_ownership_RENT]

        features1 = [np.array(features)]
        prediction = model.predict(features1)

        if prediction == 0:
            output = 'High Risk'
        elif prediction == 1:
            output = 'Low Risk'
        return render_template('index.html', prediction_text="Status of the loan is {}".format(output))



if __name__ == "__main__":
    app.run(debug=True)

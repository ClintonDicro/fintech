from Teams.Member.Models import Member_Profile
from settings import *
from Funds.Santha_payment.Models import *



@app.route("/santha_payment/<int:page>/<int:data>",methods=["GET"])
def all_santha_payments(page,data):
    try:
        all_santha_payments = Santha_Payment.query.paginate(page=page,per_page=data, error_out=False)
        santha_payment_count=Santha_Payment.query.count()
        if all_santha_payments:
            return jsonify({"data":[Santha_Payment.json(data) for data in all_santha_payments.items],"status":True,"Total count":santha_payment_count})
        else:
            return jsonify({"message":"No data","status":False})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))



@app.route("/santha_payment/<int:id>",methods=["GET"])# we should pass the member id
def santha_payments_by_id(id):
    try: 
        santha_payments = Santha_Payment.query.filter_by(members_profile_id=id).all()
        santha_payments_count = Santha_Payment.query.filter_by(members_profile_id=id).count()
        # print(santha_payments)
        if santha_payments:
            
            return jsonify({"data":[Santha_Payment.json(i) for i in santha_payments],"status":True,"Total":santha_payments_count})
        else:
            return jsonify({"message":"please check id","status":False})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))




@app.route('/santha_payment',methods=['POST'])
def add_santha_payment():
    try:
        data=request.get_json()
        today=date.today()
        
        if not Member_Profile.query.filter_by(id=data['member_id']).first():
            return jsonify({"message":"member data not found"})

        if data:
            santha_payment_details=Santha_Payment(
                members_profile_id =data['member_id'],
                santha_for_year=data['year'],
                santha_amount_received=float(data['santha_received_amount']),
                received_date=today
            )
            db.session.add(santha_payment_details)
            db.session.commit()
            return jsonify({"data":Santha_Payment.json(santha_payment_details),"message":"santha payment successfully paid","status":True})
        else:
            return jsonify({"message":"something went wrong to add santha payment","status":False})
    except Exception as e:
        return jsonify({"message":str(e)})        





@app.route('/santha_payment/<int:id>',methods=['PUT'])
def update_santha_payment(id):
    try:
        data=request.get_json()
        if not Member_Profile.query.filter_by(id=data['member_id']).first():
            return jsonify({"message":"member data not found"})
        if data:
            santha_payment_details=Santha_Payment.query.filter_by(id=id).first()
            if santha_payment_details:
                santha_payment_details.santha_for_year=data['year'],
                santha_payment_details.santha_amount_received=float(data['santha_received_amount'])
                db.session.commit()
                return jsonify({"data":Santha_Payment.json(santha_payment_details),"message":"santha payment successfully paid","status":True})
            else:
                return jsonify({"message":"something went wrong in santha payment details"})    
        else:
            return jsonify({"message":"something went wrong in your data","status":False})
    except Exception as e:
        return jsonify({"message":str(e)})        







@app.route('/santha_payment/<int:id>',methods=['DELETE'])
def delete_santha_payment(id):
    try:
        santha_payment_details=Santha_Payment.query.filter_by(id=id).first()
        if santha_payment_details:
            db.session.delete(santha_payment_details)
            db.session.commit()
            return jsonify({"message":"santha payment successfully removed","status":True})
        else:
            return jsonify({"message":"something went wrong to delete payment","status":False})    
    except Exception as e:
        return jsonify({"message":str(e)})    

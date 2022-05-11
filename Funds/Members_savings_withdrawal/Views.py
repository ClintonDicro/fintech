from settings import *
from Funds.Member_savings.Models import * 
from Teams.Member.Models import *
from Funds.Member_savings.Views import *


@app.route("/member_savings_withdraw_details/<int:id>",methods=["GET"])# we should pass the member id
def all_member_savings_withdraw(id):
    try:
        member_savings_=Member_Savings.query.filter_by(members_profile_id=id).all()  
        if member_savings_:
            return jsonify({"data":[Member_Savings.json(i) for i in member_savings_ if 0>i.payment_amount]})
        else:
            return jsonify({"message":" No data"})

    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))



@app.route("/all_member_savings_withdrawal/<int:id>",methods=["GET"])
def one_member_savings_withdraw(id):
    try:
        member_profile=Member_Profile.query.filter_by(id=id).first()
        if member_profile:
            member_savings=Member_Savings.query.filter_by(members_profile_id=member_profile.id)
           
            if member_savings:
                data=[]
                for i in member_savings:
                    if 0>i.payment_amount:
                        id=i.id
                        created_date=i.created_on
                        amount=i.payment_amount
                        member_savings_date=get_week_of_month(created_date.year,created_date.month,created_date.day)
                        month_name=created_date.strftime('%B')
                        data.append({
                            "member_savings_id":id,
                            "payment_amount":amount,
                            "month":f"{month_name}-{created_date.year}",
                            "week_no":int(member_savings_date),
                            "received_date":created_date
                        })    
                if data:
                    return jsonify({"data":data})    
                else:
                    return jsonify({"message":"No data"}) 
            else:
                return jsonify({"message":"No member savings withdrawal details "})                   
        else:
            return jsonify({"message":"something went wrong"})

    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))





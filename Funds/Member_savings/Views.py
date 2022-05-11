from settings import *
from Funds.Member_savings.Models import *
from Teams.Member.Models import *
import json


import calendar
import numpy as np
calendar.setfirstweekday(6)

def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    return(week_of_month)

# print((get_week_of_month(2022,6,1)))



@app.route('/member_savings_list',methods=['GET'])
def all_member_savings_details():
    try:
        member_profile=Member_Profile.query.all()
        # print(member_profile)
        if member_profile:
            data=[]
            for i in member_profile:
                # print(i)
                member_savings_=Member_Savings.query.filter_by(members_profile_id=i.id).all()
            
                total_savings=0
                total_withdraw=0
                month_name=""
                week=0
                due=0
                savings=0
                previous_payment=0
                received_date=0
                total_amount=0
                days_elapsed=0
                total_amount=0
                created_date=""
                previous_withdraw=0
            
                if member_savings_:
                    # print(member_savings_[-1].created_on)
                    todays=date.today()
                    # previous_withdraw=0
                    # print(member_savings_[-1].created_on)

                    created_date=member_savings_[-1].created_on

                    start_date=member_savings_[0].created_on

                    print(member_savings_[-1].payment_amount)
                    if 0>member_savings_[-1].payment_amount:
                        previous_withdraw=member_savings_[-1].payment_amount

                    if 0<member_savings_[-1].payment_amount:
                        previous_payment=member_savings_[-1].payment_amount

                    

                    month_name=created_date.strftime('%B')

                    savings_end_date = date(start_date.year,start_date.month,start_date.day)

                    current_date = date(todays.year,todays.month,todays.day)

                    days_elapsed=(current_date-savings_end_date).days

                    week=(days_elapsed//7)+1

                    total_savings=member_savings_[-1].final_balance

                    due=0
                    

                    total_amount=0
                    
                    if (week*100)==member_savings_[-1].final_balance:
                        due=0
                    elif (week*100)>member_savings_[-1].final_balance:
                        due=(week*100)-member_savings_[-1].final_balance 
                    else:
                        due=0
                    for j in member_savings_:
                        if 0>j.payment_amount:
                            total_amount+=abs(j.payment_amount)
                            total_withdraw=total_amount
                data.append({
                    "name":i.name,
                    "member_id":i.id,
                    "ref_no":i.user_id,
                    "day_elasped":days_elapsed,
                    "due":due,
                    "week":week,
                    "month":month_name,
                    "total_withdraw":total_withdraw,
                    "previous_withdraw":previous_withdraw,
                    "total_savings":total_savings,
                    "previous_payment":previous_payment,
                    "create_date":created_date
                })
            print(data)            
        if data:
            return jsonify({"data":data})
        else:
            return jsonify({"message":"no data"})     
                    
    except Exception as e:
         return jsonify({"sdfs":str(e)})   










#for header
@app.route("/member_savings_details/<int:id>",methods=["GET"])# we should pass the member id
def all_member_savings(id):
    try:
        member_profile=Member_Profile.query.filter_by(id=id).first()
        if member_profile:  
            member_savings=Member_Savings.query.filter_by(members_profile_id=member_profile.id)
            # print(member_savings[0].created_on)
            data=[]
            days_elapsed=0
            due=0
            week=0
            total_amount=0
            if member_savings:

                todays=date.today()

                start_date=member_savings[0].created_on

                savings_end_date = date(start_date.year,start_date.month,start_date.day)

                current_date = date(todays.year,todays.month,todays.day)

                days_elapsed=(current_date-savings_end_date).days

                week=(days_elapsed//7)+1

                total_amount=member_savings[-1].final_balance
                
                if (week*100)==member_savings[-1].final_balance:
                    due=0
                elif (week*100)>=member_savings[-1].final_balance:     
                    due=(week*100)-member_savings[-1].final_balance
                else:
                    due=0   
            else:
                return jsonify({"message":"something went wrong in member savings "})         
            data.append(
                {
                    "day_elapsed":days_elapsed,
                    "due":due,
                    "refer_id":member_profile.user_id,
                    "member_name":member_profile.name,
                    "member_id":member_profile.id,
                    "total_amount":total_amount
                }
            )  
            if data:
                return jsonify({"data":data})
            else:
                return jsonify({"message":"No data"})    
             
                    
        else:
            return jsonify({"message":"something went wrong in member profile "})            

    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))


















# @app.route("/member_savings_payment_details/<int:id>",methods=["GET"])# we should pass the member id
# def all_member_savings_payment(id):
#     try:
#         member_savings_=Member_Savings.query.filter_by(members_profile_id=id).all()  
#         if member_savings_:
#             return jsonify({"data":[Member_Savings.json(i) for i in member_savings_ if 0<i.payment_amount]})
#         else:
#             return jsonify({"message":" No data"})

#     except Exception as e:
#         return make_response(jsonify({"error_message":str(e)}))









@app.route("/all_member_savings_payment/<int:id>",methods=["GET"])
def one_member_profile_savings(id):
    try:
        member_profile=Member_Profile.query.filter_by(id=id).first()
        if member_profile:
            member_savings=Member_Savings.query.filter_by(members_profile_id=member_profile.id).all()
           
            if member_savings:
                data=[]
                for i in member_savings:
                    print(i)
                    if 0<i.payment_amount:
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
                return jsonify({"message":"No member savings in payment details"})                   
        else:
            return jsonify({"message":"something went wrong"})

    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))










# @app.route("/member_savings/<int:id>",methods=["GET"])
# def member_savings_(id):
#     try: 
#         member_savings = Member_Savings.query.filter_by(id=id).first()
#         if member_savings:
#             get_data = Member_Savings.json(member_savings)
#             return jsonify({"data":get_data})
#         else:
#             return jsonify({"message":"please check id"})
#     except Exception as e:
#         return make_response(jsonify({"error_message":str(e)}))






@app.route("/member_savings/<int:id>",methods=["GET"])
def member_savings_by_id(id):
    try: 
        member_savings = Member_Savings.query.filter_by(id=id).first()
        if member_savings:
            get_data = Member_Savings.json(member_savings)
            return jsonify({"data":get_data})
        else:
            return jsonify({"message":"please check id"})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))












@app.route("/member_savings/<int:id>",methods=["DELETE"])
def delete_savings_by_id(id):
    try: 
        member_savings = Member_Savings.query.filter_by(id=id).first()
        if member_savings:
            db.session.delete(member_savings)
            db.session.commit()
            return jsonify({"data":"deleted member savings"})
        else:
            return jsonify({"message":"please check id"})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))












@app.route('/member_savings',methods=['POST'])
def add_member_savings():
    try:
        data=request.get_json()
        if not Member_Profile.query.filter_by(id=data['member_id']).first():
            return jsonify({"message":"member data not found"})


        if data:
            total=Member_Savings.query.filter_by(members_profile_id = data['member_id']).all()

        

            if 0>int(data['payment_amount']):
                
                if (total[-1].final_balance-500)>=abs(int(data['payment_amount'])):# getting negative value and abs convert negative number to positive value
                    withdraw=Member_Savings(
                        members_profile_id=data['member_id'],
                        date=date.today(),#date doubt
                        payment_amount=int(data['payment_amount']),
                        final_balance = int(total[-1].final_balance)+int(data['payment_amount'])
                    )

                    if withdraw:
                        db.session.add(withdraw)
                        db.session.commit()
                        return jsonify({"data":Member_Savings.withdraw(withdraw),"status":True})
                    else:
                        return jsonify({"data":"something went wrong in withdrawal","status":False})
                else:
                    posible_amount=total[-1].final_balance-500
                    return jsonify({"message":f"you hove no money to withdrawal you can only withdraw {posible_amount}"})
            else:
                total=Member_Savings.query.filter_by(members_profile_id = data['member_id']).all()
                final_balance_=int(data['payment_amount'])
                if total:
                    
                    final_balance_=total[-1].final_balance+int(data['payment_amount'])


                member_save = Member_Savings(
                    members_profile_id = data['member_id'],
                    date=date.today(),
                    payment_amount=int(data['payment_amount']),
                    final_balance=final_balance_
                    )

                if member_save:
                    db.session.add(member_save)
                    db.session.commit()
                    return jsonify({"data":Member_Savings.json(member_save),"status":True})
                else:
                    return jsonify({"message":"something wrong in adding payment"})    

                # pass  
    except Exception as e:
        return make_response(jsonify({"error":str(e)}))








# @app.route('/member_savings/<int:id>',methods=['PUT'])
# def update_member_savings(id):
#     try:
#         data=request.get_json()
#         if not Member_Profile.query.filter_by(id=data['member_id']).first():
#             return jsonify({"message":"member data not found"})


#         if data:
#             total=Member_Savings.query.filter_by(id=id).first()

        

#             if 0>int(data['payment_amount']):
                
#                 if (total.final_balance-500)>=abs(int(data['payment_amount'])):# getting negative value and abs convert negative number to positive value
#                     # withdraw=Member_Savings(
#                     #     members_profile_id=data['member_id'],
#                     #     date=date.today(),#date doubt
#                     #     payment_amount=int(data['payment_amount']),
#                     #     final_balance = int(total[-1].final_balance)+int(data['payment_amount'])
#                     # )

#                     if total:
#                         total.members_profile_id=data['member_id'],
#                         total.date=date.today(),#date doubt
#                         total.payment_amount=int(data['payment_amount']),
#                         total.final_balance = int(total[-1].final_balance)+int(data['payment_amount'])
#                         # db.session.add(withdraw)
#                         total.db.session.commit()
#                         return jsonify({"data":Member_Savings.withdraw(withdraw),"status":True})
#                     else:
#                         return jsonify({"data":"something went wrong in withdrawal","status":False})
#                 else:
#                     posible_amount=total[-1].final_balance-500
#                     return jsonify({"message":f"you hove no money to withdrawal you can only withdraw {posible_amount}"})
#             else:
#                 total=Member_Savings.query.filter_by(members_profile_id = data['member_id']).all()
#                 final_balance_=int(data['payment_amount'])
#                 if total:
                    
#                     final_balance_=total[-1].final_balance+int(data['payment_amount'])


#                 member_save = Member_Savings(
#                     members_profile_id = data['member_id'],
#                     date=date.today(),
#                     payment_amount=int(data['payment_amount']),
#                     final_balance=final_balance_
#                     )

#                 if member_save:
#                     db.session.add(member_save)
#                     db.session.commit()
#                     return jsonify({"data":Member_Savings.json(member_save),"status":True})
#                 else:
#                     return jsonify({"message":"something wrong in adding payment"})    

#                 # pass  
#     except Exception as e:
#         return make_response(jsonify({"error":str(e)}))

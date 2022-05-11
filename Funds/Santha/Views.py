from flask_sqlalchemy import Pagination
from Teams.Member.Models import *
from Funds.Santha_payment.Models import *





#for creating pagination the santha
def get_rows(sequence, num):
    count = 1
    rows = list()
    cols = list()
    for item in sequence:
        if count == num:
            cols.append(item)
            rows.append(cols)
            cols = list()
            count = 1
        else:
            cols.append(item)
            count += 1
    if count > 0:
        rows.append(cols)
    return rows



# today = date.today()
# join_date="12-01-2020"
# con=datetime.strptime(join_date,"%d-%m-%Y")

# print(today.year,con.month,con.day)


# # def numOfDays(date1, date2):
# #     return (date2-date1).days
     
# # Driver program
# date1 = date(today.year,con.month,con.day)
# date2 = date(today.year,today.month,today.day)
# days=(date2-date1).days
# print(days, "days")

# if 30<115:
#     v=115-30
#     print(v)






@app.route('/santha/<int:page>/<int:per_page>',methods=['GET'])
def get_santha(page,per_page):
    try:
    
        
        santha=Member_Profile.query.all()
        santha_count=Member_Profile.query.count()
        santha_payment=Santha_Payment.query.all()

    

        data=[]
        # print(santha)
        if santha:
            for i in santha:
                # print(i)
                
                # #for checking is there in any members or leaders dues and how much amount they have due balance
                santha_payment_=Santha_Payment.query.filter_by(members_profile_id=i.id).all()
                if santha_payment_:
                    received_amount=0
                    due_amount=0
                    is_due="No"
                    santha_amount=100


                    #getting current date,month and year
                    today = date.today()

                    #getting join date all santha beneficier
                    join_date=i.join_date
                    date_of_join=i.join_date
                    days_elapsed=0
                    santha_end_date = date(today.year,date_of_join.month,date_of_join.day)
                    current_date = date(today.year,today.month,today.day)
                    days_elapsed=(current_date-santha_end_date).days 
                    print(days_elapsed)




                    #calculation for year count
                    term = today.year - join_date.year -((today.month, today.day) < (join_date.month, join_date.day))
                    terms=term+1
                    for j in santha_payment_:
                        received_amount+=float(j.santha_amount_received)
                        santha_end_dates = date(today.year,date_of_join.month,date_of_join.day)
                        current_dates = date(today.year,today.month,today.day)
                        days_elapseds=(current_dates-santha_end_dates).days 
                        
                    due_amount=terms*santha_amount-received_amount
                    # print(due_amount)   
                    if (terms*santha_amount)==received_amount:
                        is_due="No"
                        days_elapsed=0 
                    elif (terms*santha_amount)>received_amount:
                        is_due="Yes"
                    else:
                        is_due="No"
                        days_elapsed=0 
                        amount_balance=received_amount-(terms*santha_amount)
                        due_amount=0

                    # print(days_elapsed)
                    data.append({
                        "member_profile":i.name,
                        "member_id":i.id,
                        "term":terms,
                        "total_received_amount":float(received_amount),
                        "due_amount":float(due_amount),
                        "is_due":is_due,
                        "days elasped":days_elapsed
                        })
                else:
                    data.append(
                        {
                            "member_profile":i.name,
                            "member_id":i.id,
                            "term":1,
                            "total_received_amount":0,
                            "due_amount":0,
                            "is_due":0,
                            "days elasped":0
                            }
                    )
           
        #for getting pagination from get_row manual function    
        my_paginated_sequence = get_rows(data, per_page)
        if my_paginated_sequence:

            return jsonify({"data":my_paginated_sequence[page-1],"Total count":santha_count})
        else:
            return jsonify({"message":"No data in santha"})

    except Exception as e:
        return jsonify({"message":str(e)}) 
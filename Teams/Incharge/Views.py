from itertools import count
from settings import *
from Teams.Incharge.Models import *





@app.route('/incharge_list',methods=['GET'])
def get_employee_list():
    try:
        employee_profile_list=Employees.query.all()
        if employee_profile_list:
            return jsonify({"data":[Employees.employee_list_json(i) for i in employee_profile_list if i.employee_type==0],"status":True})
        else:
            return jsonify({"message":"No member list","status":False})    
    except Exception as e:
        return jsonify({"message":str(e)})




@app.route("/employee/<int:page>/<int:data>",methods=["GET"])
def all_employees(page,data):
    try:
        all_employees = Employees.query.paginate(page=page,per_page=data, error_out=False)
        employee_count=Employees.query.count()
        if all_employees:
            return jsonify({"data":[Employees.json(datas) for datas in all_employees.items],"status":False,"Total count":employee_count})
        else:
            return jsonify({"message":"No data","status":False})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))





@app.route("/employee/<int:id>",methods=["GET"])
def employees_by_id(id):
    try:
        employees = Employees.query.filter_by(id=id).first()
        if employees:
            get_data = Employees.json(employees)
            return jsonify({"data":get_data})
        else:
            return jsonify({"message":"please check id"})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))





@app.route('/employee',methods=['POST'])
def add_employee():
    try:
        data=request.get_json()

        if Employees.query.filter_by(mobile_no=data['mobile_no']).first():
            return jsonify({"message":"employee mobile already exist"})

        if Employees.query.filter_by(aadhar_no=data['aadhar_no']).first():
            return jsonify({"message":"employee aadhar data already exist"})

        if data:
            employee_data=Employees(
                employee_type=0,
                name=data['name'],
                dob=datetime.strptime(data['dob'],"%Y-%m-%d"),
                gender=data['gender'],
                image_path=data['image_path'],
                address=data['address'],
                district=data['district'],
                city=data['city'],
                state=data['state'],
                pincode=data['pincode'],
                aadhar_no=data['aadhar_no'],
                mobile_no=data['mobile_no'],
                join_date=datetime.strptime(data['join_date'],"%Y-%m-%d"),
                salary=data['salary'],
                # relieving_date=datetime.strptime(data['relieving_date'],"%d-%m-%Y"),
            )        
            db.session.add(employee_data)
            db.session.commit()
            return jsonify({"data":Employees.json(employee_data),"message":"Successsfully added","status":True})
        else:
            return jsonify({"message":"something went wrong adding employee","status":True})
    except Exception as e:
        return jsonify({"message":str(e)})





@app.route('/employee/<int:id>',methods=['POST'])
def update_employee(id):
    try:
        data=request.get_json()


        if Employees.query.filter_by(mobile_no=data['mobile_no']).first():
            return jsonify({"message":"employee mobile already exist"})

        if Employees.query.filter_by(aadhar_no=data['aadhar_no']).first():
            return jsonify({"message":"employee aadhar data already exist"})
            
        incharge=Employees.query.filter_by(id=id).first()
        if data:
            if incharge:
                incharge.employee_type=0,
                incharge.name=data['name'],
                incharge.dob=datetime.strptime(data['dob'],"%Y-%m-%d"),
                incharge.gender=data['gender'],
                incharge.image_path=data['image_path'],
                incharge.address=data['address'],
                incharge.district=data['district'],
                incharge.city=data['city'],
                incharge.state=data['state'],
                incharge.pincode=data['pincode'],
                incharge.aadhar_no=data['aadhar_no'],
                incharge.mobile_no=data['mobile_no'],
                incharge.join_date=datetime.strptime(data['join_date'],"%Y-%m-%d"),
                incharge.salary=data['salary'],
                incharge.relieving_date=datetime.strptime(data['relieving_date'],"%Y-%m-%d"),
                db.session.commit()
                return jsonify({"data":Employees.json(id),"message":"Successsfully updated","status":True})
            else:
                return jsonify({"message":"please check your leader id"})    

        else:
            return jsonify({"message":"something went wrong adding employee","status":True})
    except Exception as e:
        return jsonify({"message":str(e)})




@app.route("/employee/<int:id>",methods=["DELETE"])
def delete_employee(id):
    try:
        employees = Employees.query.filter_by(id=id).first()
        if employees:
            db.session.delete(employees)
            db.session.commit()
            return jsonify({"data":"employee detail deleted"})
        else:
            return jsonify({"message":"please check id"})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))

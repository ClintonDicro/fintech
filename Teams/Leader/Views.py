from Teams.Incharge.Models import Employees
from settings import *
from Teams.Member.Models import *



@app.route('/leader_list',methods=['GET'])
def get_leader_list():
    try:
        leader_profile_list=Member_Profile.query.filter_by(is_leader=1)
        if leader_profile_list:
            return jsonify({"data":[Member_Profile.leader_list_json(i) for i in leader_profile_list if i.status==0],"status":True})
        else:
            return jsonify({"message":"No leader list","status":False})    
    except Exception as e:
        return jsonify({"message":str(e)})






@app.route('/leader/<int:page_no>/<int:per_page_no>',methods=['GET'])
def get_leader_profile(page_no,per_page_no):
    try:
        leader_data=Member_Profile.query.filter_by(is_leader=1).paginate(page=page_no,per_page=per_page_no,error_out=False)
        leader_count=Member_Profile.query.count()
        if leader_data:
            return jsonify({"data":[Member_Profile.leader_json(i) for i in leader_data.items],"status":True,"Total count":leader_count})
        else:
            return jsonify({"message":"No data in member","status":False})    
    except Exception as e:
        return jsonify({"message":str(e)})        







@app.route('/leader/<int:id>',methods=['GET'])
def get_by_leader_profile(id):
    try:
        leader_data=Member_Profile.query.filter_by(id=id).first()

        if leader_data:
            return jsonify({"data":Member_Profile.leader_json(leader_data),"status":True})
        else:
            return jsonify({"message":"No data in member","status":False})    
    except Exception as e:
        return jsonify({"message":"something went wrong in member"})        







@app.route('/leader',methods=['POST'])
def add_leader_profile():
    try:
        data=request.get_json() 


        if not Employees.query.filter_by(id=data['incharge_id']).first():
            return jsonify({"message":"incharge does not exist"})

        if Member_Profile.query.filter_by(mobile_no=data['mobile_no']).first():
            return jsonify({"message":"mobile nummber already exist"})


        if Member_Profile.query.filter_by(auth_data=data['auth_data']).first():
            return jsonify({"message":"auth data  already exist"})    


        if data:
            member_data=Member_Profile(
                user_id=Random_number(),
                name=data['name'],
                dob=datetime.strptime(data['dob'],"%Y-%m-%d"),
                image_path=data['image_path'],
                gender=data['gender'],
                address=data['address'],
                city=data['city'],
                state=data['state'],
                district=data['district'],
                pincode=data['pincode'],
                auth_type_id=data['auth_type_id'],
                auth_data=data['auth_data'],
                auth_path=data['auth_path'],
                mobile_no=data['mobile_no'],
                join_date=datetime.strptime(data['join_date'],"%Y-%m-%d"),
                is_leader=1,
                incharge_id=data['incharge_id'],
                nominee_name=data['nominee_name'],
                nominee_dob=datetime.strptime(data['nominee_dob'],"%Y-%m-%d"),
                nominee_relation=data['nominee_relation'],
                nominee_mobile_number=data['nominee_mobile_number'],
                nominee_aadhar_no=data['nominee_aadhar_no'],
            )


            if member_data:
                db.session.add(member_data)
                db.session.commit()
                return jsonify({"data":Member_Profile.leader_json(member_data),"status":True})
            else:
                return jsonify({"message":"something wrong in adding member","status":False})


        else:
            return jsonify({"message":"something wrong in getting member info","status":False})


    except Exception as e:
        return jsonify({"message":str(e)})





@app.route('/leader/<int:id>',methods=['PUT'])
def update_leader_profile(id):
    try:
        data=request.get_json()

        if not Employees.query.filter_by(id=data['incharge_id']).first():
            return jsonify({"message":"incharge does not exist"})

        # for mombile is exist or not
        if Member_Profile.query.filter_by(mobile_no=data['mobile_no']).first():
            return jsonify({"message":"mobile nummber already exist"})

        # for auth data is exist or not
        if Member_Profile.query.filter_by(auth_data=data['auth_data']).first():
            return jsonify({"message":"auth data  already exist"})

        leader=Member_Profile.query.filter_by(id=id).first()

        if data:
            if leader:
                    leader.name=data['name'],
                    leader.dob=datetime.strptime(data['dob'],"%Y-%m-%d"),
                    leader.image_path=data['image_path'],
                    leader.gender=data['gender'],
                    leader.address=data['address'],
                    leader.city=data['city'],
                    leader.state=data['state'],
                    leader.district=data['district'],
                    leader.pincode=data['pincode'],
                    leader.auth_type_id=data['auth_type_id'],
                    leader.auth_data=data['auth_data'],
                    leader.auth_path=data['auth_path'],
                    leader.mobile_no=data['mobile_no'],
                    leader.join_date=datetime.strptime(data['join_date'],"%Y-%m-%d"),
                    leader.is_leader=0,
                    leader.incharge_id=data['incharge_id'],
                    leader.nominee_name=data['nominee_name'],
                    leader.nominee_dob=datetime.strptime(data['nominee_dob'],"%Y-%m-%d"),
                    leader.nominee_relation=data['nominee_relation'],
                    leader.nominee_mobile_number=data['nominee_mobile_number'],
                    leader.nominee_aadhar_no=data['nominee_aadhar_no'],
                    db.session.commit()
                    return jsonify({"data":Member_Profile.member_json(id),"message":"leader details updated","status":True})
               
            else:
                return jsonify({"message":"leader does not exist","status":False})        

        else:
            return jsonify({"message":"something wrong in getting member info","status":False})


    except Exception as e:
        return jsonify({"message":str(e)})





@app.route('/leader/<int:id>',methods=['DELETE'])
def delete_leader(id):
    try:
        leader_delete=Member_Profile.query.filter_by(id=id).first()
        if leader_delete:
            db.session.delete(leader_delete)
            db.session.commit()
            return jsonify({"message":"member deleted","status":False})
        else:    
            return jsonify({"message":"no id to delete","status":False})
    except Exception as e:
        return jsonify({"message":str(e)})
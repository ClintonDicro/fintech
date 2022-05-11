from Teams.Incharge.Models import Employees
from settings import *
from Teams.Member.Models import *




@app.route('/member_list',methods=['GET'])
def get_member_list():
    try:
        member_profile_list=Member_Profile.query.filter_by(is_leader=0)
        if member_profile_list:
            return jsonify({"data":[Member_Profile.member_list_json(i) for i in member_profile_list if i.status==0],"status":True})
        else:
            return jsonify({"message":"No member list","status":False})    
    except Exception as e:
        return jsonify({"message":str(e)})




@app.route('/member/<int:page_no>/<int:per_page_no>',methods=['GET'])
def get_member_profile(page_no,per_page_no):
    try:
        member_data=Member_Profile.query.filter_by(is_leader=0).paginate(page=page_no,per_page=per_page_no,error_out=False)
        member_count=Member_Profile.query.count()
        if member_data:
            return jsonify({"data":[Member_Profile.member_json(i) for i in member_data.items],"status":True,"Total count":member_count})
        else:
            return jsonify({"message":"No data in member","status":False})    
    except Exception as e:
        return jsonify({"message":str(e)}) 






@app.route('/member/<int:id>',methods=['GET'])
def get_by_member_profile(id):
    try:
        member_data=Member_Profile.query.filter_by(id=id).first()

        if member_data:
            return jsonify({"data":Member_Profile.member_json(member_data),"status":True})
        else:

            return jsonify({"message":"No data in member","status":False})    
    except Exception as e:
        return jsonify({"message":str(e)})        









@app.route('/member',methods=['POST'])
def add_menber_profile():
    try:
        data=request.get_json()

        if not Employees.query.filter_by(id=data['incharge_id']).first():
            return jsonify({"message":"incharge does not exist"})

        if not Member_Profile.query.filter_by(id=data['leader_id']).first():
            return jsonify({"message":"leader does not exist"})

        # for mombile is exist or not
        if Member_Profile.query.filter_by(mobile_no=data['mobile_no']).first():
            return jsonify({"message":"mobile nummber already exist"})

        # for auth data is exist or not
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
                is_leader=0,
                leader_id=data['leader_id'],
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
                return jsonify({"data":Member_Profile.member_json(member_data),"status":True})
            else:
                return jsonify({"message":"something wrong in adding member","status":False})


        else:
            return jsonify({"message":"something wrong in getting member info","status":False})


    except Exception as e:
        return jsonify({"message":str(e)})





@app.route('/member/<int:id>',methods=['PUT'])
def update_member_profile(id):
    try:
        data=request.get_json()

       

        # for mombile is exist or not
        if Member_Profile.query.filter_by(mobile_no=data['mobile_no']).first():
            return jsonify({"message":"mobile nummber already exist"})

        # for auth data is exist or not
        if Member_Profile.query.filter_by(auth_data=data['auth_data']).first():
            return jsonify({"message":"auth data  already exist"})

        member=Member_Profile.query.filter_by(id=id).first()

        if data:
            if member:
                    member.name=data['name'],
                    member.dob=datetime.strptime(data['dob'],"%Y-%m-%d"),
                    member.image_path=data['image_path'],
                    member.gender=data['gender'],
                    member.address=data['address'],
                    member.city=data['city'],
                    member.state=data['state'],
                    member.district=data['district'],
                    member.pincode=data['pincode'],
                    member.auth_type_id=data['auth_type_id'],
                    member.auth_data=data['auth_data'],
                    member.auth_path=data['auth_path'],
                    member.mobile_no=data['mobile_no'],
                    member.join_date=datetime.strptime(data['join_date'],"%Y-%m-%d"),
                    member.is_leader=0,
                    member.leader_id=data['leader_id'],
                    member.incharge_id=data['incharge_id'],
                    member.nominee_name=data['nominee_name'],
                    member.nominee_dob=datetime.strptime(data['nominee_dob'],"%Y-%m-%d"),
                    member.nominee_relation=data['nominee_relation'],
                    member.nominee_mobile_number=data['nominee_mobile_number'],
                    member.nominee_aadhar_no=data['nominee_aadhar_no'],
                    db.session.commit()
                    return jsonify({"data":Member_Profile.member_json(id),"message":"member details updated","status":True})
               
            else:
                return jsonify({"message":"member does not exist","status":False})        

        else:
            return jsonify({"message":"something wrong in getting member info","status":False})


    except Exception as e:
        return jsonify({"message":str(e)})








@app.route('/member/<int:id>',methods=['DELETE'])
def delete_member(id):
    try:
        member_delete=Member_Profile.query.filter_by(id=id).first()
        if member_delete:
            db.session.delete(member_delete)
            db.session.commit()
            return jsonify({"message":"member deleted","status":False})
        else:    
            return jsonify({"message":"no id to delete","status":False})
    except Exception as e:
        return jsonify({"message":str(e)})    

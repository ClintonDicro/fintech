from settings import *
from Authentication.App_user.Models import *





@app.route("/app_users/<int:page>/<int:data>",methods=["GET"])
def all_app_users(page,data):
    try:
        all_users = App_Users.query.all().paginate(page=page,per_page=data, error_out=False)
        if all_users:
            return jsonify({"data":[App_Users.json(data) for data in all_users.items]})
        else:
            return jsonify({"message":"No data"})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))





@app.route("/app_users/<int:id>",methods=["GET"])
def app_user_by_id(id):
    try:
        user = App_Users.query.filter_by(id=id).first()
        if user:
            get_data = App_Users.json(user)
            return jsonify({"data":get_data})
        else:
            return jsonify({"message":"please check id"})
    except Exception as e:
        return make_response(jsonify({"error_message":str(e)}))




@app.route('/app_user',methods=['POST'])
def add_app_user():
    try:
        data=request.get_json()
        
        email_check = App_Users.query.filter_by(email=data['email']).first()
        if email_check:
            return jsonify({
                "message":"this email already exist"
            })
        mobile_check = App_Users.query.filter_by(email=data['email']).first()
        if mobile_check:
            return jsonify({
                "message":"this mobile already exist"
            })

        user = App_Users.query.filter_by(email=data.get('user_name')).first()
        if not user:
            new_user=App_Users(
                role_id=data['role_id'],
                user_name=data['user_name'],
                image_path=data['image_path'],
                mobile=data['mobile'],  
                name=data.get("name"),
                email=data.get("email"),
                encrypted_password=generate_password_hash(data.get("password"))
            )
            db.session.add(new_user)
            db.session.commit()
    
            return jsonify({"message":"app user successfully added","staus":True})
        else:
            return jsonify({ "message":'user already exist !!!',"status":False})
    
    except Exception as e:
        # logger.warning({"message":str(e)})
        return make_response(jsonify({"message":str(e)}))
        

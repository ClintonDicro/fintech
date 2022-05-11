from settings import *
from Authentication.App_user.Models import *
from Authentication.login.token import *
from datetime import datetime,timedelta
# from authentication.login.validation import *
# from log.log_file import *




@app.route('/user_login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        # val = validation(data)
        # if val:
        #     logger.warning({"message":val})
        #     return jsonify({
        #         "message":val
        #     })
        
        filter_user = App_Users.query.filter_by(email=data.get("email")).first()
        if filter_user:
            if check_password_hash(filter_user.encrypted_password,data.get("password")):
                db.session.commit()
                token = jwt.encode({
                    'id':filter_user.id,
                    'exp':datetime.utcnow() + timedelta(minutes=180)
                }, app.config['SECRET_KEY'])
                # logger.info({ "token":token,
                #     "status":True,
                #     "user_name":filter_user.name,
                #     "message":"login successfully"})

                return jsonify({
                    "token":token,
                    "status":True,
                    "user_name":filter_user.name,
                    "message":"login successfully"
                })
            else:
                # logger.warning({"message":"wrong password"}) 
                return jsonify({"message":"wrong password","status":False})    
        else:
            # logger.warning({"status":False,
                # "message":"login failed"})
            return jsonify({
                "status":False,
                "message":"login failed"
            })   
    
    except Exception as e:
        # logger.warning({"message":str(e)})
        return make_response(jsonify({"message":str(e)}))

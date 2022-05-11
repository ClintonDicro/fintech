from settings import *
from functools import wraps
from Authentication.App_user.Models import *
# from user_role_mapping.model import *
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if 'access_token' in request.headers:
            token = request.headers['access_token']
        if not token:
            return jsonify({'message':'Token is missing!'})
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            try:
                current_user = App_Users.query.filter_by(id=data['id']).first()
            except:
                 return jsonify({
                'message':'Token is invalid'
                })
            
        except:
            return jsonify({
                'message':'Token is invalid'
            })
        
        return f(*args, **kwargs)
    return decorated


# def permission_required(*arguments):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             token=request.headers.get('access-token')
#             data_one=jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
#             current_member = App_Users.query.filter_by(role_id=data_one['role_id']).first()
#             user_role = User_role_mapping.query.filter_by(role_id=data_one['role_id']).first()
#             for i in user_role:
#                 if i.role_id == current_member:
#                       return func(*args,**kwargs)  
#                 else:
#                     return jsonify({"message":"he is not admin"})
        
#             return make_response(jsonify({"Message":"You cannot access this content."})) 
#         return wrapper
#     return decorator

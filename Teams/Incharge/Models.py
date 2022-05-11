
from settings import *



class Employees(db.Model):
    __tablename__="employees"
    id=db.Column(db.BigInteger(),primary_key=True)
    emp_type=[
        (0,"incharge")
    ]
    employee_type=db.Column(db.Integer(),ChoiceType(emp_type),default=0)
    name=db.Column(db.String(50),nullable=False)
    dob=db.Column(db.Date(),nullable=False)
    gen=[
        (0,"male"),(1,"female")
    ]
    gender=db.Column(db.Integer(),ChoiceType(gen),default=0)
    image_path=db.Column(db.String(255),nullable=True)
    address=db.Column(db.String(255),nullable=True)
    district=db.Column(db.String(120),nullable=False)
    city=db.Column(db.String(120),nullable=True)
    state=db.Column(db.String(120),nullable=True)
    pincode=db.Column(db.Integer(),nullable=True)
    aadhar_no=db.Column(db.BigInteger(),nullable=True)
    mobile_no=db.Column(db.BigInteger(),nullable=True)
    join_date=db.Column(db.Date())
    salary=db.Column(db.Float(precision=32,decimal_return_scale=None),nullable=True)
    relieving_date=db.Column(db.String(10),nullable=True)
    created_on=db.Column(db.DateTime(timezone=True),nullable=True,server_default=func.now())
    

    
    def json(self):
        return {
            "app_user_id":self.id,
            "employee_type":self.employee_type,
            "district":self.district,
            "name":self.name,
            "dob":self.dob,
            "gender":self.gender,
            "image_path":self.image_path,
            "address":self.address,
            "city":self.city,
            "state":self.state,
            "pincode":self.pincode,
            "aadhar_no":self.aadhar_no,
            "mobile_no":self.mobile_no,
            "join_date":self.join_date,
            "salary":self.salary,
            "relieving_date":self.relieving_date,
            "creadted_on":self.created_on,
           
        }
    def employee_list_json(self):
        return {
            "incharge_id":self.id,
            "name":self.name,

        }    
        
    
    def __repr__(self):
        return f"{self.name}"     
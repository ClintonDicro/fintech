from settings import *



class Member_Profile(db.Model):
    __tablename__ = 'member_profile'
    id=db.Column(db.BigInteger(),primary_key=True)
    user_id=db.Column(db.String(10),nullable=False,unique=True)   #doubt user_id but string
    name=db.Column(db.String(50),nullable=False)
    dob=db.Column(db.Date(),nullable=False)
    image_path=db.Column(db.String(255),nullable=True)
    gen=[
        (0,"male"),(1,"female")
    ]
    gender=db.Column(db.Integer(),ChoiceType(gen),default=0)
    address=db.Column(db.String(255),nullable=False)
    city=db.Column(db.String(120),nullable=False)
    state=db.Column(db.String(120),nullable=False)
    district=db.Column(db.String(120),nullable=False)
    pincode=db.Column(db.Integer(),nullable=False)
    auth_type=[
        (0,"Aadhar"),(1,"Driving")   
    ]
    auth_type_id=db.Column(db.Integer(),ChoiceType(auth_type),nullable=False,default=0)
    auth_data=db.Column(db.String(100),nullable=True)
    auth_path=db.Column(db.String(255),nullable=True)
    mobile_no=db.Column(db.BigInteger(),nullable=False)
    join_date=db.Column(db.Date(),nullable=False)
    santha_amount=db.Column(db.Float(precision=32,decimal_return_scale=None),nullable=True)
    Is_Leader=[
        (0,"No"),(1,"Yes")   
    ]
    is_leader=db.Column(db.Integer(),ChoiceType(Is_Leader),nullable=False,default=0)
    leader_id=db.Column(db.BigInteger(),nullable=True)
    incharge_id=db.Column(db.BigInteger(),nullable=True)
    status_=[
        (0,"active"),(1,"closed"),(2,"suspended")
    ]
    status=db.Column(db.Integer(),ChoiceType(status_),nullable=False,default=0)
    last_status_change_date=db.Column(db.Date(),nullable=True)
    comments=db.Column(db.String(255),nullable=True)
    nominee_name=db.Column(db.String(255),nullable=True)
    nominee_dob=db.Column(db.Date(),nullable=True)
    nominee_relation=db.Column(db.String(255),nullable=True)
    nominee_mobile_number=db.Column(db.BigInteger(),nullable=True)
    nominee_aadhar_no=db.Column(db.BigInteger(),nullable=True)
    created_on=db.Column(db.DateTime(timezone=True),server_default=func.now())
    
    # terms=db.Column(db.Integer(),default=0)
    # Is_Due=[
    #     (0,"No"),(1,"Yes")   
    # ]
    # is_due=db.Column(db.Integer(),ChoiceType(Is_Due),default=0)
    # terms=db.Column(db.Integer(),default=0)
    
  
    
    
    # fk_benefit_details = db.relationship("Benefits",back_populates='fk_member_profile_details',cascade="all, delete")
    
    
    #relation connected from santha payment
    fk_santha_payment_details = db.relationship("Santha_Payment",back_populates='fk_members_profile_details',cascade="all, delete")
    
    #relation connected from member savings
    fk_members_savings_details = db.relationship("Member_Savings",back_populates='fk_members_profile_details',cascade="all, delete")
    
    
    #relation connected from pension
    # fk_pension_details = db.relationship("Pension",back_populates='fk_members_profile_details',cascade="all, delete")
    
    
    #relation connected from loan request
    # fk_loan_request_details = db.relationship("Loan_Request",back_populates='fk_requested_by_details',cascade="all, delete")
    
    #relation connected from savings loan
    # fk_savings_loan_details = db.relationship("Savings_Loan",back_populates='fk_members_profile_details',cascade="all, delete")
    
    #relation connected from savings loan payment
    # fk_savings_loan_payment_details = db.relationship("Savings_loan_payment",back_populates='fk_member_profile_details')
    
    #relation connected from education loan
    # fk_education_loan_details = db.relationship("Education_loans",back_populates='fk_members_profile_details',cascade="all, delete")
    
    #relation connected from education loan payment
    # fk_education_loan_payment_details = db.relationship("Education_loan_payment",back_populates='fk_members_profile_details')
    
    #relation connected from business loan
    # fk_business_loan_details = db.relationship("Business_loans",back_populates='fk_members_profile_details')
    
  
    
    def json(self):
        return {
            "all_profile_id":self.id,
            "user_id":self.user_id,
            "name":self.name,
            "dob":self.dob,
            "image_path":self.image_path,
            "gender":self.gender,
            "address":self.address,
            "city":self.city,
            "state":self.state,
            "district":self.district,
            "pincode":self.pincode,
            "auth_type_id":self.auth_type_id,
            "auth_data":self.auth_data,
            "auth_path":self.auth_path,
            "mobile_no":self.mobile_no,
            "join_date":self.join_date,
            "santha_amount":self.santha_amount,
            "leader_id":self.leader_id,
            "is_leader":self.is_leader,
            "incharge_id":self.incharge_id,
            "status":self.status,
            "last_status_change_date":self.last_status_change_date,
            "comments":self.comments,
            "nominee_name":self.nominee_name,
            "nominee_dob":self.nominee_dob,
            "nominee_relation":self.nominee_relation,
            "nominee_mobile_number":self.nominee_mobile_number,
            "nominee_aadhar_no":self.nominee_aadhar_no,
            "created_on":self.created_on,
        }
        
    def member_json(self):
        return {
            "member_profile_id":self.id,
            "member_profile_id":self.id,
            "user_id":self.user_id,
            "is_leader":self.is_leader,
            "name":self.name,
            "dob":self.dob,
            "image_path":self.image_path,
            "gender":self.gender,
            "address":self.address,
            "city":self.city,
            "state":self.state,
            "district":self.district,
            "pincode":self.pincode,
            "auth_type_id":self.auth_type_id,
            "auth_data":self.auth_data,
            "auth_path":self.auth_path,
            "mobile_no":self.mobile_no,
            "join_date":self.join_date,
            "leader_id":self.leader_id,
            "incharge_id":self.incharge_id,
            "nominee_name":self.nominee_name,
            "nominee_dob":self.nominee_dob,
            "nominee_relation":self.nominee_relation,
            "nominee_mobile_number":self.nominee_mobile_number,
            "nominee_aadhar_no":self.nominee_aadhar_no,
        }   

    def leader_json(self):
        return {
            "leader_profile_id":self.id,
            "user_id":self.user_id,
            "is_leader":self.is_leader,
            "name":self.name,
            "dob":self.dob,
            "image_path":self.image_path,
            "gender":self.gender,
            "address":self.address,
            "city":self.city,
            "state":self.state,
            "district":self.district,
            "pincode":self.pincode,
            "auth_type_id":self.auth_type_id,
            "auth_data":self.auth_data,
            "auth_path":self.auth_path,
            "mobile_no":self.mobile_no,
            "join_date":self.join_date,
            "incharge_id":self.incharge_id,
            "status":self.status,
            "comments":self.comments,
            "nominee_name":self.nominee_name,
            "nominee_dob":self.nominee_dob,
            "nominee_relation":self.nominee_relation,
            "nominee_mobile_number":self.nominee_mobile_number,
            "nominee_aadhar_no":self.nominee_aadhar_no,
        }         



    def member_list_json(self):
        return {
            "member_profile_id":self.id,
            "name":self.name
        }        


    def leader_list_json(self):
        return {
            "leader_profile_id":self.id,
            "name":self.name
        }         
     
        
    def __repr__(self):
        return f"<Member_profile>{self.id}"
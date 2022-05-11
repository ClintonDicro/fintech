from settings import *



class App_Users(db.Model):
    __tablename__="app_users"
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(70),nullable=False)
    role=[
        (0,"user"),(1,"adimn"),(2,"finance")
    ]
    role_id=db.Column(db.Integer(),ChoiceType(role),nullable=False,default=0)
    user_name=db.Column(db.String(70),nullable=False,unique=True)
    image_path=db.Column(db.String(255),nullable=True)
    encrypted_password=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(70),nullable=True)
    mobile=db.Column(db.String(10),nullable=True,unique=True)
    created_on=db.Column(db.DateTime(timezone=True),nullable=True,server_default=func.now())
    
    # #relation to benefits
    # fk_benefits_details = db.relationship("Benefits",back_populates="fk_approval_by_details")

    # #relation connected from loan request
    # fk_loan_request_details = db.relationship("Loan_Request",back_populates='fk_action_by_user_details')
    
    
    # #relation connected from savings loan
    # fk_savings_loan_details = db.relationship("Savings_Loan",back_populates='fk_app_user_details')
     
    # #relation connected from education loan
    # fk_education_loan_details = db.relationship("Education_loans",back_populates='fk_app_user_details')
     
    # #relation connected from business loan
    # fk_business_loan_details = db.relationship("Business_loans",back_populates='fk_app_user_details')

    
      
    
    def json(self):
        return {
            "app_user_id":self.id,
            "name":self.name,
            "role_id":self.role_id,
            "user_name":self.user_name,
            "image_path":self.image_path,
            "email":self.email,
            "mobile":self.mobile,
            "created_on":self.created_on,
        }
        
    
    def __repr__(self):
        return f"{self.user_name}"
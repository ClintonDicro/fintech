from settings import *




class Member_Savings(db.Model):
    __tablename__="member_savings"
    id=db.Column(db.BigInteger(),primary_key=True)
    # member_id=db.Column(db.BigInteger(),nullable=False)
    date=db.Column(db.Date(),nullable=False)
    # initial_amount=db.Column(db.Float(precision=32,decimal_return_scale=None),nullable=False)
    payment_amount=db.Column(db.Float(precision=32,decimal_return_scale=None),nullable=False,default=0)
    final_balance=db.Column(db.Float(precision=32,decimal_return_scale=None),nullable=False,default=0)
    created_on=db.Column(db.DateTime(timezone=True),server_default=func.now())
    
    
    
    #foreign key has connected from member profile
    members_profile_id = db.Column(db.BigInteger(),db.ForeignKey('member_profile.id',ondelete="CASCADE"),nullable=False)
    fk_members_profile_details = db.relationship("Member_Profile",back_populates='fk_members_savings_details')
    
    
    
    def json(self):
        return {
            "member_savings_id":self.id,
            "member_id":self.members_profile_id,
            "date":self.date,
            "payment_amount":self.payment_amount,
            "final_balance":self.final_balance,
            "created_on":self.created_on,
        }
    
    def withdraw(self):
        return {
            "member_savings_id":self.id,
            "member_id":self.members_profile_id,
            "date":self.date,
            "payment_amount":self.payment_amount,
            "final_balance":self.final_balance,
            "created_on":self.created_on,
        }

        
    def __repr__(self):
        return f"{self.id}"     
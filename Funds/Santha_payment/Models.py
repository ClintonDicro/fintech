from settings import *




class Santha_Payment(db.Model):
    __tablename__="santha_payments"
    id=db.Column(db.BigInteger(),primary_key=True)
    santha_for_year=db.Column(db.Integer(),nullable=False)
    santha_amount_received=db.Column(db.Float(precision=32,decimal_return_scale=None),nullable=False)
    received_date=db.Column(db.Date(),nullable=False)
    created_on=db.Column(db.DateTime(timezone=True),server_default=func.now())
    
    
    #foreign key has connected from member profile
    members_profile_id = db.Column(db.BigInteger(),db.ForeignKey('member_profile.id',ondelete="CASCADE"),nullable=False)
    fk_members_profile_details = db.relationship("Member_Profile",back_populates='fk_santha_payment_details')
    
    
    
    def json(self):
        return {
            "santha_payments_id":self.id,
            "member_id":self.members_profile_id,
            "santha_for_year":self.santha_for_year,
            "santha_amount_received":self.santha_amount_received,
            "received_data":self.received_date,
            "created_on":self.created_on,
        }
        
    def __repr__(self):
        return f"{self.id}"     
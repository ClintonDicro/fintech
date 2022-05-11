from settings import *

# from bank_accounts.model import *
# from bank_transactions.model import *
# from business_loans.model import *
# from business_loans_payment.model import *
# from category_subcategory.model import *
# from education_loan_payment.model import *
# from education_loans.model import *
# from expense.model import *
# from income.model import *
# from payable.model import *
# from receivable.model import *
from Authentication.App_user.Models import *
# from Benefits.Models import *
from Teams.Incharge.Models import *
# from Loan_request.Models import *
# from Master_data.Models import *
from Teams.Member.Models import *
from Funds.Santha_payment.Models import *
from Funds.Member_savings.Models import *
# from Member_savings.Models import *
# from Pension_payments.Models import *
# from Pensions.Models import *

from Funds.Santha_payment.Models import *
# from Savings_loan_payment.Models import *
# from Savings_loans.Models import *
# from user_role_mapping.model import *



from Teams.Member.Views import *
from Teams.Leader.Views import *
from Authentication.App_user.Views import *
from Authentication.login.Views import *
from Teams.Incharge.Views import *
from Funds.Santha.Views import *
from Funds.Santha_payment.Views import *
from Funds.Member_savings.Views import *
from Funds.Members_savings_withdrawal.Views import *





if '__main__' == __name__:
    app.run(debug=True)
#host:'192.168.18.39'



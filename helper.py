"""Assign scores to the sales growth"""
def assign_score_sales_growth(val):
    if val >=0.06:
        return 1
    elif val >= 0.04 and val < 0.06:
        return 2
    elif val >= 0.03 and val < 0.04:
        return 3
    elif val >=0.025 and  val < 0.03:
        return 4
    elif val >=0.02 and val < 0.025:
        return 5
    elif val >=0.015 and val < 0.02:
        return 6
    elif val >=0.01 and  val < 0.015:
        return 7
    elif val >=0.00  and val < 0.01:
        return 8
    else:
        return 11

"""Assign scores to the gross profit margin"""
def assign_score_gross_profit_margin(val):
    if val >=0.4:
        return 1
    elif val >= 0.35 and val < 0.4:
        return 2
    elif val >= 0.3 and val < 0.35:
        return 3
    elif val >=0.25 and val < 0.3:
        return 4
    elif val >=0.2 and val < 0.25:
        return 5
    elif val >=0.15 and val < 0.2:
        return 6
    elif val >=0.075 and val < 0.15:
        return 7
    elif val >=0.05  and val < 0.075:
        return 8
    else:
        return 11
    
"""Assign scores to the normalised ebita margin"""
def assign_score_noramlised_ebita_margin(val):
    if val >=0.15:
        return 1
    elif val >= 0.125 and val < 0.15:
        return 2
    elif val >= 0.15 and val < 0.1:
        return 3
    elif val >=0.1 and val < 0.08:
        return 4
    elif val >=0.06 and val < 0.08:
        return 5
    elif val >=0.04 and val < 0.06:
        return 6
    elif val >=0.04 and val < 0.02:
        return 7
    elif val >=0.02  and val < 0.04:
        return 8
    elif val >=0.01 and val < 0.02:
        return 9
    else:
        return 10


"""Assign scores to the net profit margin"""
def assign_score_net_profit_margin(val):
    if val >=0.1:
        return 1
    elif val >= 0.08 and val < 0.1:
        return 2
    elif val >= 0.06 and val < 0.08:
        return 3
    elif val >=0.04 and val < 0.06:
        return 4
    elif val >=0.03 and val < 0.04:
        return 5
    elif val >=0.02 and val < 0.03:
        return 6
    elif val >=0.005 and val < 0.02:
        return 7
    elif val >=0.0  and val < 0.005:
        return 8
    else:
        return 9

"""Assign scores to the tangible net worth (KES in millions) margin"""
def assign_score_tangible_net_worth(val):
    if val >=1:
        return 1
    elif val >=  0.75 and val < 1:
        return 2
    elif val >= 0.5 and val < 0.75:
        return 3
    elif val >=0.25 and val < 0.5:
        return 4
    elif val >=0.1 and val < 0.25:
        return 5
    elif val >=0.05  and val < 0.25:
        return 6
    elif val >=0.02 and val < 0.01:
        return 7
    else:
        return 9
    
"""Assign scores to the adjusted working capital margin"""
def assign_score_adjusted_working_capital(val):
    if val >50000000:
        return 1
    elif val <=  50000000 and val > 10000000:
        return 2
    elif val <=10000000 and val > 5000000:
        return 3
    elif val <= 5000000 and val > 1000000:
        return 4
    elif val <= 1000000 and val > 500000:
        return 5
    elif val <=500000  and val >250000:
        return 6
    elif val <=250000 and val > 100000:
        return 7
    else:
        return 9

"""Assign scores to the receivable days"""
def assign_scores_receivable_days(val):
    if val <30:
        return 1
    elif val >=30 & val <45:
        return 2
    elif val >= 45 & val < 60:
        return 3
    elif val >= 60& val < 75:
        return 4
    elif val >=75 & val < 90:
        return 5
    elif val >=90  & val < 105:
        return 6
    elif val >=105 & val < 120:
        return 7
    elif val >=120 & val < 150:
        return 8
    elif val >=150 & val < 180:
        return 9
    elif val >=180 & val <210:
        return 10
    else:
        return 11


"""Assign scores to the inventory days"""
def assign_scores_inventory_days(val):
    if val <30:
        return 1
    elif val >=30 & val <45:
        return 2
    elif val >= 45 & val < 60:
        return 3
    elif val >= 60& val < 75:
        return 4
    elif val >=75 & val < 90:
        return 5
    elif val >=90  & val < 105:
        return 6
    elif val >=105 & val < 120:
        return 7
    elif val >=120 & val < 150:
        return 8
    elif val >=150 & val < 180:
        return 9
    elif val >=180 & val <210:
        return 10
    else:
        return 11

"""Assign scores to the payable days"""
def assign_scores_payable_days(val):
    if val >180:
        return 1
    elif val > 120 & val <=180:
        return 2
    elif val > 90 & val <= 120:
        return 3
    elif val > 75  & val <= 90:
        return 4
    elif val > 60 & val <= 75:
        return 5
    elif val > 45  & val <=60:
        return 6
    elif val > 30 & val <= 45:
        return 7
    elif val > 15 & val <= 30:
        return 8
    elif val >=10 & val < 15:
        return 9
    else:
        return 10

"""Assign scores to cash equivalents/sales *365"""
def assign_scores_cash_equivalent(val):
    if val >60:
        return 1
    elif val > 45 & val <=60:
        return 2
    elif val > 35 & val <= 45:
        return 3
    elif val > 25 & val <= 35:
        return 4
    elif val > 20 & val <= 25:
        return 5
    elif val > 15  & val <=20:
        return 6
    elif val > 10 & val <= 15:
        return 7
    elif val > 5 & val <= 10:
        return 8
    elif val >=2 & val <= 5:
        return 9
    else:
        return 10
    
"""Assign scores to current liabiities"""
def assign_scores_current_liabilities(val):
    if val >60:
        return 1
    elif val > 45 & val <=60:
        return 2
    elif val > 35 & val <= 45:
        return 3
    elif val > 25 & val <= 35:
        return 4
    elif val > 20 & val <= 25:
        return 5
    elif val > 15  & val <=20:
        return 6
    elif val > 10 & val <= 15:
        return 7
    elif val > 5 & val <= 10:
        return 8
    elif val >=2 & val <= 5:
        return 9
    else:
        return 10


"""Assign scores to st_debt"""
def assign_scores_st_debt(val):
    if val >125:
        return 1
    elif val > 100 & val <=125:
        return 2
    elif val > 80 & val <= 100:
        return 3
    elif val > 60 & val <= 80:
        return 4
    elif val > 50 & val <= 60:
        return 5
    elif val > 40  & val <=50:
        return 6
    elif val > 30  & val <= 40:
        return 7
    elif val > 25 & val <= 30:
        return 8
    elif val >=20 & val <= 25:
        return 9
    else:
        return 10


"""Assign scores to equity"""
def assign_scores_equity(val):
    if val >10:
        return 1
    elif val < 20 & val <=10:
        return 2
    elif val < 30 & val <= 20:
        return 3
    elif val < 40 & val <= 30:
        return 4
    elif val < 60 & val <= 40:
        return 5
    elif val < 60  & val <=80:
        return 6
    elif val < 100 & val <= 80:
        return 7
    elif val > 125 & val <= 100:
        return 8
    elif val <150 & val <= 125:
        return 9
    else:
        return 10

"""Assign scores to total current assets"""
def assign_scores_total_current_assets(val):
    if val < 2.5:
        return 1
    elif val >=2.5 and val <5:
        return 2
    elif val >=5 and val < 7.5:
        return 3
    elif val >= 7.5 and val < 10:
        return 4
    elif val >= 10  and val < 15:
        return 5
    elif val >= 15  and val < 20:
        return 6
    elif val >= 20  and val < 30:
        return 7
    elif val >= 30 and val < 40:
        return 8
    elif val >= 40 and val < 50:
        return 9
    else:
        return 10

"""Assign scores to net worth"""
def assign_scores_net_worth(val):
    if val >=0.15:
        return 1
    elif val >= 0.125 and val < 0.15:
        return 2
    elif val >= 0.15 and val < 0.1:
        return 3
    elif val >=0.1 and val < 0.08:
        return 4
    elif val >=0.06 and val < 0.08:
        return 5
    elif val >=0.04 and val < 0.06:
        return 6
    elif val >=0.04 and val < 0.02:
        return 7
    elif val >=0.02  and val < 0.04:
        return 8
    elif val >=0.01 and val < 0.02:
        return 9
    else:
        return 10

"""Assign scores to current ratio"""
def assign_scores_current_ratio(val):
    if val >2:
        return 1
    elif val > 1.5 and val <=2:
        return 2
    elif val > 1.3 and val <= 1.4:
        return 3
    elif val > 1.2 and val <= 1.3:
        return 4
    elif val > 1.1 and val <= 1.2:
        return 5
    elif val > 1.0 and val <=1.1:
        return 6
    elif val > 0.9 and val <= 1.0:
        return 7
    elif val > 0.8 and val <= 0.9:
        return 8
    elif val >=0.8 and val <= 0.5:
        return 9
    else:
        return 10

"""Assign scores to total debt"""
def assign_scores_total_debt(val):
    if val >60:
        return 1
    elif val > 45 & val <=60:
        return 2
    elif val > 35 & val <= 45:
        return 3
    elif val > 25 & val <= 35:
        return 4
    elif val > 20 & val <= 25:
        return 5
    elif val > 15  & val <=20:
        return 6
    elif val > 10 & val <= 15:
        return 7
    elif val > 5 & val <= 10:
        return 8
    elif val >=2 & val <= 5:
        return 9
    else:
        return 10

"""Assign scores interest expense"""
def assign_scores_interest_expense(val):
    if val >15:
        return 1
    elif val > 10 and val <=15:
        return 2
    elif val > 8 and val <= 10:
        return 3
    elif val > 7 and val <= 8:
        return 4
    elif val > 6 and val <= 7:
        return 5
    elif val > 5 and val <=6:
        return 6
    elif val > 4 and val <= 5:
        return 7
    elif val > 3 and val <= 4:
        return 8
    elif val >=2 and val <= 3:
        return 9
    else:
        return 10

"""Assign scores to net income"""
def assign_scores_net_income(val):
    if val >90:
        return 1
    elif val > 80 & val <=90:
        return 2
    elif val > 70 & val <= 80:
        return 3
    elif val > 60 & val <= 70:
        return 4
    elif val > 50 & val <= 60:
        return 5
    elif val > 40  & val <=50:
        return 6
    elif val > 25  & val <= 40:
        return 7
    elif val > 20 & val <= 25:
        return 8
    elif val >=15 & val <= 20:
        return 9
    else:
        return 10

"""Assign scores to the stability"""
def assign_scores_stability(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='weak':
        return 3
    else:
        return 4
    
"""Assign scores to economic sensitivity"""
def assign_scores_econ_sensitivity(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5
"""Assign scores to capital intensity"""
def assign_scores_capital_intensity(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5

"""Assign scores to utilization_capacity"""
def assign_scores_utilization_capacity(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5

"""Assign scores to market_growth"""
def assign_scores_market_growth(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5
"""Assign scores to how_regulated """
def assign_scores_how_regulated(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5
"""Assign scores to how_competitive """
def assign_scores_how_competitive(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5

"""Assign scores to how_diverse  """
def assign_scores_how_diverse(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5 

"""Assign scores to how_mature """
def assign_scores_how_mature(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5 

"""Assign scores to product_substitution """
def assign_scores_product_substitution(val):
    if val=='outstanding':
        return 1
    elif val =='high':
        return 2
    elif val =='medium':
        return 3
    elif val =='weak':
        return 4
    else:
        return 5 

"""Assign risk classes based on the total scores"""
def assign_risk_classes(val):
    if val >0.8:
        return "A"
    elif val >=0.6  and  val < 0.8:
        return "B"
    elif val >=0.4 and val < 0.6:
        return "C"
    elif val >= 0.3 and val < 0.4:
        return "D"
    elif val >= 0.2 and val < 0.2:
        return "E"
    elif val >= 0.1 and val <0.2:
        return "F"
    else:
        return "Z"

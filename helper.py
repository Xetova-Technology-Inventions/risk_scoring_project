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
    if val <= 0.1:
        return 1
    elif val <=  0.15 & val < 0.1:
        return 2
    elif val >= 0.2 & val < 0.15:
        return 3
    elif val <=0.25 & val < 0.2:
        return 4
    elif val <=0.30 & val < 0.25:
        return 5
    elif val <=0.35  & val < 0.3:
        return 6
    elif val <=0.4 & val < 0.01:
        return 7
    else:
        return 9

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
    if val >0.6:
        return 1
    elif val > 0.5 & val <=0.6:
        return 2
    elif val > 0.4 & val <= 0.5:
        return 3
    elif val > 0.3 & val <= 0.4:
        return 4
    elif val > 0.25 & val <= 0.3:
        return 5
    elif val > 0.2  & val <=0.25:
        return 6
    elif val > 0.15 & val <= 0.20:
        return 7
    elif val > 0.1 & val <= 0.15:
        return 8
    elif val >=0.05 & val <= 0.1:
        return 9
    else:
        return 10

"""Assign scores to total current assets"""
def assign_scores_total_current_assets(val):
    if val < 0.1:
        return 1
    elif val < 0.2 & val >=0.1:
        return 2
    elif val < 0.3 & val >= 0.2:
        return 3
    elif val > 0.4 & val >= 0.3:
        return 4
    elif val > 0.6 & val >= 0.4:
        return 5
    elif val > 0.8  & val <=0.6:
        return 6
    elif val > 1 & val <= 1.25:
        return 7
    elif val > 1.25 & val <= 1.5:
        return 8
    else:
        return 9

"""Assign scores to total liabilities"""
def assign_scores_total_liabilities(val):
    if val < 0.0025:
        return 1
    elif val < 0.005 & val >=0.0025:
        return 2
    elif val < 0.0075 & val >= 0.005:
        return 3
    elif val > 0.01 & val >= 0.0075:
        return 4
    elif val > 0.01 & val >= 0.015:
        return 5
    elif val > 0.015  & val <=0.02:
        return 6
    elif val > 0.02 & val <= 0.025:
        return 7
    elif val > 0.025 & val <= 0.03:
        return 8
    elif val > 0.03 & val <= 0.035:
        return 9
    else:
        return 10


"""Assign risk classes based on the total scores"""
def assign_risk_classes(val):
    if val < 11:
        return "A"
    elif val >=13  and  val < 15:
        return "B"
    elif val >=15 and val < 18:
        return "C"
    elif val >= 18 and val < 22:
        return "D"
    elif val >= 22 and val < 25:
        return "E"
    elif val >= 25 and val <30:
        return "F"
    else:
        return "Z"

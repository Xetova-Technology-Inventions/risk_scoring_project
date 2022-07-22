 # importing neccesary
import pandas as pd
import pandas as pd
import datetime
from helper import *

## read sample data
df = pd.read_csv("data/risk_scoring_mock_data_guyo.csv")

"""
Write the data into the database
"""

"""
Read the data from the databse
"""
# transform columns if neccesary
# Assign scores based on the current credit assesment system
""" 
Asess the  business operation.
We use the following data points to obtain operational assessment scores;
1. Sales growth
2. Profit margin
3. Normalised ebita margin
4. Normalised profit margin
We then assign weights to each of this to obtain an overall score for the operational assessment of the business.
"""
# Assign scores to the selected columns under operation_assessment scores.
df['sales_growth_scores'] = df['sales_growth'].apply(assign_score_sales_growth)
df['profit_margin_scores'] = df['profit_margin'].apply(assign_score_gross_profit_margin)
df['normalised_ebita_margin_scores'] = df['normalised_ebita_margin'].apply(assign_score_noramlised_ebita_margin)
df['net_profit_margin_scores'] = df['net_profit_margin'].apply(assign_score_net_profit_margin)

# Define weights for operation_assessment scores columns
sales_growth_wght = 0.1
gross_profit_margin_wght = 0.2
normalized_ebita_margin_wght = 0.35
net_profit_margin = 0.1
# Define the overall operation_assessment scores
df['operational_assement_score'] = (sales_growth_wght*df['sales_growth_scores']) + (gross_profit_margin_wght*df['profit_margin_scores']) + (normalized_ebita_margin_wght*df['normalised_ebita_margin_scores']) + (net_profit_margin*df['net_profit_margin_scores'])

""" 
Assess the working capital management, liquidity & asset quality of the business.
We use the following data points to obtain operational assessment scores;
1. Tangible Net Worth (KES in millions)
2. Adjusted working capital/sales
3. Receivable days
4. Payable days
5. Cash equivalents
6. Current liabilities
7. ST debt
We then assign weights to each of this to obtain an overall score for the operational assessment of the business.
"""

df['net_worth_scores'] = df['net_profit_margin'].apply(assign_score_tangible_net_worth)
df['Workng_capital_scores'] = df['working_capital'].apply(assign_score_adjusted_working_capital)
df['receivable_day_scores'] = df['receivable_day'].apply(assign_scores_receivable_days)
df['inventory_days_scores'] = df['inventory_days'].apply(assign_scores_inventory_days)
df['payable_days_scores'] = df['payable_days'].apply(assign_scores_inventory_days)
df['cash_equivalents_scores'] = df['cash_equivalents'].apply(assign_scores_cash_equivalent)
df['current_liabilities_scores'] = df['current_liabilities'].apply(assign_scores_current_liabilities)
df['st_debt_scores'] = df['st_debt'].apply(assign_scores_st_debt)

## Data points weight
net_worth_wght= 0.1
working_capital_wght = 0.15
receivable_days_wght = 0.1
inventory_days_wght = 0.1
payable_days_wght = 0.1
cash_equivalents_wght = 0.15
current_liability_wght = 0.15
st_debt_wght = 0.15

## score under working capital management
df['working_capital_management_score'] = (net_worth_wght* df['net_worth_scores']) + (working_capital_wght * df['Workng_capital_scores']) + (receivable_days_wght* df['receivable_day_scores']) + (inventory_days_wght* df['inventory_days_scores']) + (payable_days_wght* df['payable_days_scores']) 
+  (cash_equivalents_wght* df['cash_equivalents_scores']) + (current_liability_wght * df['current_liabilities_scores']) +  (st_debt_wght*df['st_debt_scores'])

""" 
Assess the financing structure of the business.
We use the following data points;
1. Total debt/Equity
2. ST Debt/Total current assets
3. Net worth
4. Current ratio
"""

df['equity_score'] = df['equity'].apply(assign_scores_equity)
df['total_current_assets_score'] =df['total_current_assets'].apply(assign_scores_total_current_assets)
df['net_worth_score'] = df['net_worth'].apply(assign_scores_net_worth)
df['current_ratio_score'] = df['net_worth'].apply(assign_scores_net_worth)

equity_wght= 0.33
total_current_assets_wght = 0.22
total_net_worth_wght = 0.33
current_ratio_wght = 0.11

df['financing_structure_score']  = (equity_wght * df['equity_score']) + (total_current_assets_wght*df['total_current_assets_score']) + (total_net_worth_wght*df['net_worth_score']) + (current_ratio_wght *df['current_ratio_score'])

""" 
Assess the cash flow & debt capacity of the business.
We use the following data points;
1. Ebita/total debt
2. Interest expense
3. Net income
4. stability and sustainbility of cash flow
"""
df['total_debts_score'] = df['total_debts'].apply(assign_scores_total_debt)
df['interest_expense_score'] =df['interest_expense'].apply(assign_scores_interest_expense)
df['net_income_score'] = df['net_income'].apply(assign_scores_net_income)
df['stability_score'] = df['stability'].apply(assign_scores_stability)

total_debts_wght= 0.40
interest_expense_wght = 0.4
net_income_wght = 0.20
stability_wght = 0.25

df['cash_flow_capacity_score'] = (total_debts_wght*df['total_debts_score']) + (interest_expense_wght*df['interest_expense_score']) + (net_income_wght*df['net_income_score']) + (stability_wght*df['stability_score'])

""" 
Assess the business risk (industry/market/competitive position)
We use the following data points;
1. Economic sensitivity
2. capital intensity
3. capacity utilization
4. Market growth
4. How regulated
5. How competitive
6. How diverse
7. How mature
8. product substitution
"""
df['economic_sensitivity_score'] = df['economic_sensitivity'].apply(assign_scores_econ_sensitivity)
df['capital_intensity_score'] = df['capital_intensity'].apply(assign_scores_capital_intensity)
df['utilization_capacity_score'] = df['utilization_capacity'].apply(assign_scores_utilization_capacity)
df['market_growth_score'] = df['market_growth'].apply(assign_scores_market_growth)
df['how_regulated_score'] = df['how_regulated'].apply(assign_scores_how_regulated)
df['how_competitive_score'] = df['how_competitive'].apply(assign_scores_how_competitive)
df['how_diverse_score'] = df['how_diverse'].apply(assign_scores_how_diverse)
df['how_mature_score'] = df['how_mature'].apply(assign_scores_how_mature)
df['product_substitution_score'] =  df['product_substitution'].apply(assign_scores_product_substitution)

economic_sensitivity_wght= 0.1
capital_intensity_wght = 0.1
utilization_capacity_wght = 0.1
market_growth_wght = 0.1
how_regulated_wght= 0.1
how_competitive_wght = 0.1
how_diverse_wght = 0.1
how_mature_wght = 0.1
product_substitution_wght = 0.2

df['business_risk_score']  = (economic_sensitivity_wght * df['economic_sensitivity_score']) + (capital_intensity_wght*df['capital_intensity_score']) + \
(utilization_capacity_wght * df['utilization_capacity_score']) + (market_growth_wght*df['market_growth_score']) + (how_regulated_wght*df['how_regulated_score'])  + \
(how_competitive_wght*df['how_competitive_score']) + (how_diverse_wght*df['how_diverse_score']) + (how_mature_wght*df['how_mature_score']) + (product_substitution_wght*df['product_substitution_score'])

# get a subset of data with the selected columns
output = df[['supplier_id', 'operational_assement_score', 'working_capital_management_score',
       'financing_structure_score', 'cash_flow_capacity_score','business_risk_score']]
## Give weights to each metric
operational_assement_wght= 0.2
working_capital_management_wght = 0.2
financing_structure_wght = 0.20
cash_flow_capacity_wght = 0.25
business_risk_wght= 0.15

# get total scores
output['total_scores'] = (operational_assement_wght*output['operational_assement_score']) + (working_capital_management_wght*output['working_capital_management_score']) + \
     (financing_structure_wght*output['financing_structure_score']) + (cash_flow_capacity_wght*output['cash_flow_capacity_score']) + (business_risk_wght*output['business_risk_score'])

min = output['total_scores'].min()
max = output['total_scores'].max()
output['total_scores_scaled'] = output['total_scores'].transform(lambda x: ((x-min) /(max-min)))
# output['total_scores'].apply(lambda x: (x - min)/(max-min))
# assign risk classes based on risk score
output['risk_class'] = output["total_scores_scaled"].apply(assign_risk_classes)
timestamp = pd.Timestamp(datetime.datetime(2021, 10, 10))
res = timestamp.today()
output['scoring_time'] = res

##show the data
pd.set_option('display.max_columns', None)
print(output.head())
#write to csv
output.to_csv('data/output.csv')
# Write this into a database


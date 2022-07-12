# importing neccesary
import pandas as pd
from helper import *

## read sample data
df = pd.read_csv("risk_scoring_mock_data.csv")

# transform the columns
df['sales_growth'] = df['sales_growth']/100
df['profit_margin'] = df['profit_margin']/100
df['normalised_ebita_margin'] = df['normalised_ebita_margin']/100
df['net_profit_margin'] = df['net_profit_margin']/100
df['net_profit_margin'] = df['net_profit_margin']/100
df['net_worth'] = df['net_worth']/100

# assign scores to the selected columns using the columns
df['sales_growth_scores'] = df['sales_growth'].apply(assign_score_sales_growth)
df['profit_margin_scores'] = df['profit_margin'].apply(assign_score_gross_profit_margin)
df['normalised_ebita_margin_scores'] = df['normalised_ebita_margin'].apply(assign_score_noramlised_ebita_margin)
df['net_profit_margin_scores'] = df['net_profit_margin'].apply(assign_score_net_profit_margin)
df['net_worth_scores'] = df['net_profit_margin'].apply(assign_score_tangible_net_worth)
df['inventory_days_scores'] = df['inventory_days'].apply(assign_scores_inventory_days)
df['payable_days_scores'] = df['payable_days'].apply(assign_scores_inventory_days)
df['receivable_day_scores'] = df['receivable_day'].apply(assign_scores_inventory_days)

# get a subset of data with the selected columns
sub_df = df[['supplier_id', 'sales_growth_scores', 'profit_margin_scores',
       'normalised_ebita_margin_scores', 'net_profit_margin_scores',
       'net_worth_scores', 'inventory_days_scores', 'payable_days_scores',
       'receivable_day_scores']]
sub_df

# get total scores
sub_df['total_scores'] = sub_df['sales_growth_scores'] + sub_df['profit_margin_scores'] + sub_df['normalised_ebita_margin_scores'] + sub_df['net_profit_margin_scores']
+ sub_df['net_worth_scores'] + sub_df['inventory_days_scores'] + sub_df['payable_days_scores'] + sub_df['receivable_day_scores']
sub_df['total_scores']

## assign risk classes based on risk score
sub_df['risk_class'] = sub_df["total_scores"].apply(assign_risk_classes)

## Write this into a database


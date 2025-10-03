import pandas as pd

location_path = "C:/Users/Jesse/Desktop/ATM_Project/atm_location.csv"
cash_needs_path = "C:/Users/Jesse/Desktop/ATM_Project/atm_cash_needs.csv"

location_df = pd.read_csv(location_path)
cash_needs_df = pd.read_csv(cash_needs_path)

cash_needs_df['date'] = pd.to_datetime(cash_needs_df['date'])

atm_capacity = 20000
max_deposit = 50000 

def predict_refill_days(atm_df):
    atm_df = atm_df.sort_values('date')
    
    
    atm_df['cumulative_withdrawals'] = atm_df['total_withdrawals'].cumsum()
    atm_df['remaining_cash'] = atm_capacity - atm_df['cumulative_withdrawals']
    
    
    atm_df['cumulative_deposits'] = atm_df['total_deposits'].cumsum()
    atm_df['remaining_capacity'] = max_deposit - atm_df['cumulative_deposits']
    
    
    threshold = 5000  
    
    
    refill_days = atm_df[(atm_df['remaining_cash'] <= threshold) | 
                         (atm_df['remaining_capacity'] <= threshold)]['date']
    
    return refill_days


refill_schedule = cash_needs_df.groupby('atm_id').apply(predict_refill_days).reset_index()
refill_schedule.columns = ['atm_id', 'refill_index', 'refill_date']


refill_schedule = refill_schedule[['atm_id', 'refill_date']]

print(refill_schedule)
#output_path = "C:/Users/Jesse/Desktop/ATM_Project/atm_refill_schedule.csv"
#refill_schedule.to_csv(output_path, index=False)
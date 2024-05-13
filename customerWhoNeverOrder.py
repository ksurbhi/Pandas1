#Problem 4 :Customer Who Never Order
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # df = pd.merge(customers, orders, left_on = 'id',
    # right_on = 'customerId', how = 'left')
    # df = df[(df['customerId'].isna())]
    # return df[['name']].rename(columns = {'name':'Customers'})

    # We can also use merge() as below
    df = customers.merge(orders, left_on = 'id', 
    right_on= 'customerId', how = 'left')
    df = df[(df['customerId'].isna())]
    return df[['name']].rename(columns = {'name':'Customers'})

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result=pd.merge(customers,orders,left_on="id",right_on="customerId",how="left")
    result=result[result["customerId"].isna()][["name"]]
    result=result.rename(columns={"name":"customers"})
    return result
    
'''
leetcode link =https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
here merging is usued to join two tables
isna() means null values
["name"] is used to select the "name" column from the DataFrame created in step 2. The double brackets [["name"]] are used to indicate that you want to select a DataFrame with a single column, "name"
'''

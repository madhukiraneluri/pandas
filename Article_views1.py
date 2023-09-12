import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result=views[views["author_id"]==views["viewer_id"]]["author_id"]
    result=result.unique()
    result=sorted(result)
    return pd.DataFrame({'id':result})
  '''
  leetcode link:
  https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
  here in this code in note itself given we have to slect when author id is equal to viewer id 
  sql query : select distinct author_id from views order by author_id
  result=views[views["author_id"]==views["viewer_id"]] # it return a data frame with that rows which followed those constraints
  result=result["author_id"]
  it returns a series 
  to make distinct elements we didnt converted that series to a column or list
  to make distinct elements we have used unique keyword 
  after using unique keyword to a series it returns an numpy array
  so thats why we have used sorted instead of sort i.e., numpy array
  so given numpy array as a data to result datafram
  '''

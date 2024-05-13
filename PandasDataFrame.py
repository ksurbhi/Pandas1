#Problem 1 : Make a Pandas DataFrame with two-dimensional list
import pandas as pd
my_list = [['A',12,'NY'],['B',13,'LA'],['C',11,'SF']]
df = pd.DataFrame(my_list, columns = ['Name','Age','City']) 
print(df)

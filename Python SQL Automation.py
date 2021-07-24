import pyodbc
import pandas as pd
import os
from datetime import datetime
from plyer import notification

# create SQL connection
connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',
                           host = 'DESKTOP-NAKP5E5',
                           database = "Test",
                           trusted_connection = 'yes')
                           
# SQL Command to read the data
sqlQuery = "select * from dbo.SalesOrder where Region = 'South'"

# Getting the data from sql into pandas dataframe
df = pd.read_sql(sql = sqlQuery, con = connection)

# Export the data on the Desktop
df.to_csv(os.environ["userprofile"] + "\\Desktop\\PythonScript\\" + "SQL_OrderData_" +
 datetime.now().strftime("%d-%b-%Y %H%M%S")
         + ".csv", index = False)

# Display Notifiction to User
notification.notify(title="Report Status!!!",
                   message=f"Sales data has been successfully saved into Excel.\
                   \nTotal Rows: {df.shape[0]}\nTotal Columns: {df.shape[1]}",
                   timeout = 10)

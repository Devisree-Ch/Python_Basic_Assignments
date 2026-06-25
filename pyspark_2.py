# Create a new column username by converting the name column to lowercase and replacing spaces with underscores (_).
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Assignment").getOrCreate()
data = [
    ("Rahul Naik",),
    ("Priya Subramaniam",),
    ("Ali Hussain",)
    ]
df= spark.createDataFrame(data, ["name"])
df.show()
from pyspark.sql.functions import udf
from pyspark.sql.functions import StringType
def lowercase(name):
  new_name=name.replace(" ","_")
  return new_name.lower()

lower1=udf(lowercase,StringType())
new_df=df.withColumn("Lowercase_name",lower1("name"))
new_df.show()
# Create a new column new_salary by adding a fixed bonus of 5000 to the existing salary column.
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Demo").getOrCreate()
data =[
    ("Abhi",4000),
    ("Mabhi",5000),
    ("Jabhi",6000)
]
columns =["name","salary"]
df=spark.createDataFrame(data,columns)
df.show()
def bonus(salary):
  return salary+5000
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
new_sal=udf(bonus,IntegerType())
new_df=df.withColumn("new_salary",new_sal("salary"))
new_df.show()
# Create a new column city_updated where if the city column is NULL, it should be replaced with "Unknown"; otherwise, keep the original city value.
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("New").getOrCreate()
data = [
    ("Nama","Delhi"),
    ("Sama",None),
    ("Rama","Hyd"),
]
columns = ["name","city"]
df=spark.createDataFrame(data,columns)
df.show()
updated_city=lambda city: "Unknown" if city==None else city
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

new_city=udf(updated_city,StringType())
df2=df.withColumn("Updated_city",new_city("city"))
df2.show() 
# Generate a user_id column in the format EMP_<name_in_uppercase> from the name column.
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("New").getOrCreate()
data=[
    ("Divya",),
    ("Bhavya",),
    ("Sravya",)
]
df=spark.createDataFrame(data, ["name"])
df.show()
user=lambda name : "EMP_<"+name.upper()+">"
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
usertype=udf(user,StringType())
df2=df.withColumn("user_id",usertype("name"))
df2.show()
# Create a salary_category column where salaries greater than 50000 are labeled "High" and all others are labeled "Low".
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("New").getOrCreate()
data = [
    ("Bhuvana",65000),
    ("Ramana",27000),
    ("Madana",50000),
]
cols=["name","salary"]
df=spark.createDataFrame(data,cols)
df.show()
salaries= lambda salary : "High" if salary>50000 else "Low"
from pyspark.sql.functions import udf
catg=udf(salaries)
df2=df.withColumn("salary_category",catg("salary"))
df2.show()
# Create a display_name column that contains the employee's name in title case (for example, "rahul sharma" → "Rahul Sharma").
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("new").getOrCreate()
df=spark.createDataFrame([("rama raavi",),("suma kanakala",),("sam raj",)],["names"])
df.show()
def titlecase(names):
  return names.title()
from pyspark.sql.functions import udf
new=udf(titlecase)
df2=df.withColumn("Display_Name",new("names"))
df2.show()
# Create a contact_status column that returns "No Email" if the email column is NULL; otherwise, return "Email Available".
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("New").getOrCreate()
data=[
    ("sana","s12@gmail.com"),
    ("rana",None),
    ("gana",None),
]
cols=["name","emailid"]
df=spark.createDataFrame(data,cols)
df.show()
mailid=lambda emailid:"Email Available" if emailid else "No Email"
from pyspark.sql.functions import udf
catg=udf(mailid)
df2=df.withColumn("contact_status",catg("emailid"))
df2.show()
# Create a bonus_percentage column by calculating 10% of the salary and storing the result in a new column.
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("new").getOrCreate()
data=[
    (20000,),
    (30000,),
    (50000,),
]
df=spark.createDataFrame(data,["salary"])
df.withColumn("bonus_percentage",df.salary*10/100).show()
# Create a city_code column by taking the first three characters of the city name and converting them to uppercase.
from pyspark.sql import SparkSession
from pyspark.sql.functions import substring
from pyspark.sql.functions import upper
spark = SparkSession.builder.appName("nava").getOrCreate()
data=[
    ("Hyderabad",),
    ("Chennai",),
   ("Bangalore",), 
]
df=spark.createDataFrame(data,["city"])
df.show()
df2=df.withColumn("city_code",upper(substring(df.city,1,3)))
df2.show()
# Create a masked_username column by keeping the first three characters of the username and replacing the remaining characters with ****.
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("new").getOrCreate()
data=[
    ("Divya",),
    ("Bhavya",),
    ("Sravya",)
]
df=spark.createDataFrame(data,["name"])
df.show()
def masked(name):
  actual_length=len(name)-3
  return name[:3]+"x"*actual_length
from pyspark.sql.functions import udf
privat=udf(masked)
df2=df.withColumn("masked_username",privat("name"))
df2.show()
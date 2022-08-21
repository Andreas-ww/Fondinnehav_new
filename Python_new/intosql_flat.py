import os 
from Flat_all import read_quarters
from sqlalchemy import create_engine

os.chdir(r"C:\Users\awestroth\Privat\Fondinnehav_new\Python_new")

engine = create_engine("mssql+pyodbc://AAP-5CG1248DY5/Fondinnehav_DB?driver=SQL Server?Trusted_Connection=yes")

#Get all quarters 
filer_path = r"C:\Users\awestroth\Privat\Fondinnehav_new\download_files_new"

filer = os.listdir(filer_path)

new_filer = []
for fil in filer:
    if ".zip" not in fil:
        new_filer.append(fil)

quarters = [filer_path + "/" +  s for s in new_filer]
#Här har vi pathen till alla kvartal 
#Funktion för att gå igenom ett kvartal 

for quarter in reversed(quarters):
    

    read_quarters(quarter = quarter, engine = engine)
    print(quarter)


#%%
#Start
# import os 
# from Flat_all import read_quarters
# from sqlalchemy import create_engine

# os.chdir(r"C:\Users\awestroth\Privat\Fondinnehav_new\Python_new")

# engine = create_engine("mssql+pyodbc://AAP-5CG1248DY5/Fondinnehav_DB?driver=SQL Server?Trusted_Connection=yes")

# #Get all quarters 
# filer_path = r"C:\Users\awestroth\Privat\Fondinnehav_new\download_files_new"

# filer = os.listdir(filer_path)

# new_filer = []
# for fil in filer:
#     if ".zip" not in fil:
#         new_filer.append(fil)
# quarters = [filer_path + "/" +  s for s in new_filer]


# quarter = quarters[1]
# read_quarters(quarter = quarter, engine = engine)


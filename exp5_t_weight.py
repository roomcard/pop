import csv

file_path ='exp5_input.csv'

data ={}
row ={}
col ={}

with open(file_path,'r') as file :
    reader =csv.reader(file)
    header =next(reader)
    for r in reader :
        region,company,sales = r
        sales =int(sales)

        if region not in data :
              data[region]={}
        
        data[region][company]=sales
        row[region]=row.get(region,0)+sales
        col[company]=col.get(company,0)+sales
    print(data)
    print(row)
    print(col)

total_value= sum(row.values())

print("Region\\Brand  |  Nokia (Count, t-weight, d-weight)  |  Apple (Count, t-weight, d-weight)  |  Total")
print("-" * 80)

for region ,row_count in row.items():
     rows_data=[]
     rows_data.append(region)

     for company,company_count in col.items():
          tweight=round((data[region][company]/row_count)*100,2)
          dweight=round((data[region][company]/company_count)*100,2)
          rows_data.append(f"{data[region][company]} ({tweight}, {dweight})")
     
     rows_data.append(f"{row_count} (100%,{round((row_count/total_value)*100,2)})")
     print(" | ".join(rows_data))


rows_data=[]
rows_data.append("total")

for company, company_count in col.items():
     tweight = round((company_count/total_value)*100,2)
     rows_data.append(f"{company_count} ({tweight} ,100) ")
rows_data.append(f"{total_value} (100%, 100%)")
print(" | ".join(rows_data))
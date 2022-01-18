## Capstone Project : Global Airport Ticket (GAT)
###  Udacity Data Engineering Nanodegree 
#### Data Warehouse Modeling use Postgre SQL with Start Schema
#### Project Summary
The objective of this project was to create an ETL pipeline for the Global Airport Ticket Data Contains view in 1993 (Q1:Q4) summary characteristics of each domestic itinerary on the Origin and Destination Survey, including the reporting carrier, itinerary fare, a number of passengers, originating airport, roundtrip indicator, and miles flown, global temperatures , global airport, and global ISO countries datasets to form an analytics database on travel events and find travel patterns the globe.  

##### The project follows the follow steps:
* Step 1: Scope the Project and Gather Data
* Step 2: Explore and Assess the Data
* Step 3: Define the Data Model
* Step 4: Run ETL to Model the Data
* Step 5: Complete Project Write Up

### Step 1: Scope the Project and Gather Data
We need to create ETL for converting numbers of CSV files to Data Warehouse Modeling using Postgre SQL with Star Schema for Airport Ticket Data Contains view in 1991-Q1 for date analytics database on travel events and find travel patterns the globe. 

### DataSet

##### I  ) Global ISO Countries
file name: Countries.csv

source file: https://public.opendatasoft.com/explore/dataset/world-administrative-boundaries-countries/export/

#####  II ) Global Airport
file name: Airports.csv

source file: https://www.transtats.bts.gov/Download_Lookup.asp?Y11x72=Y_NVecbeg
#####  III  ) Global Airport Ticket 1993 [Q1,Q2,Q3,4]
file name:  Ticket1993Q1.csv,Ticket1993Q2.csv,
            Ticket1993Q3.csv,Ticket1993Q4.csv

source file: https://www.transtats.bts.gov/DL_SelectFields.asp?gnoyr_VQ=FKF&QO_fu146_anzr=b4vtv0%20n0q%20Qr56v0n6v10%20f748rB
### Step 2: Explore and Assess the Data
#### Explore Sample Data top 1000 rows
Identify data quality issues, like missing values, duplicate data, etc.
##### we need to create analytics for travel patterns around the globe for these columns :
[number_passengers, round_trip,online,dollar_cred,bulk_fare]

### Step 3: Define the Data Model
#### 3.1 Conceptual Data Model
-Data Warehouse with star schema dimensions and fact table

-Chose that model it's easy to work and  low cost

#### 3.2 Mapping Out Data Pipelines
-copy all csv file to storage tables on DB

-cleaning tasks after ETL on storage tables

-create dimensions and fact table
### Step 4: Run Pipelines to Model the Data 
#### 4.1 Create the data model for storage
Build the data pipelines to create the data model for storage.
##### Create and copy from CSV to storage

##### Cleaning Tasks  

Countries:

-dimensions convert grouping columns: [(Region_Code,Region_Name)]

Airports:

-spilt Description column to city,cuntry, airport name


-convert to dimensions


Ticket:

-dimensions convert grouping columns: [(year, quarter)]

-create fact table [year, quarter,Origin,origincountry, originstate,Passengers,RoundTrip,OnLine,DollarCred,BulkFare] 
  
drop storage tables
#### 4.2 Create the data model for dimensions and fact
Build the data pipelines to create the data model for dimensions and fact.
#### 4.2.1 Create dimensions tables
Countries:

-dimensions convert grouping columns: 

    -Region:(Region_Code,Region_Name),

    -Country:(country_code,country_name,country_code_iso_2)    
#### 4.2 Data Quality Checks
-Using  Integrity constraints on the relational database (Constraint Primary Key, Foreign Key , Data Type , Not Null And Inner Join, etc.) .

-use inner join in the fact table to get complete data .

##### Run Quality Checks
select count(0) from stg = ticket=select count(0) from fact_ticket
#### 4.3 Data dictionary 
all URLs have description for each field setp 1 > DataSet

#### Step 5: Complete Project Write Up

Run the ETL every quarter,we need compare full quarter.

Recommend add partitioned table for fact_ticket on year_quarter column.
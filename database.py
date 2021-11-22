# first install "python with path"
# If you have any questions this youtube video will explain
# https://www.youtube.com/watch?v=byHcYRpMgI4
import sqlite3 

#connect to database
conn = sqlite3.connect('jobs.db')

#Create a cursor
c = conn.cursor()


# Create a Table
# Datatypes are NULL, INTEGAR, REAL, TEXT, BLOB
c.execute("""CREATE TABLE jobs (
    job_sector TEXT,
    employed INTEGAR,
    employment_per_1000_jobs INTEGAR,
    median_hrly_wage INTEGAR,
    mean_hourly_wage INTEGAR,
    annual_mean_wage INTEGAR
)""")


# Create the job table. This table include job sector, how many are employed,
# how many are employed by every 1000 jobs, median hourly wage, mean hourly wage,
# and annual mean salary.
jobs = [('Management Occupations', 171950, 53.815, 24.81, 66.66, 138660),
            ('Business and Financial Operations Occupations', 237920, 74.462, 37.94, 41.63, 86600), 
            ('Computer and Mathmatical Ocupations', 200650, 62.796, 58.88, 58.96, 122640), 
            ('Architecture and Engineering Occupations', 74670, 23.369, 45.71, 48.31, 100480), 
            ('Life, Physical, and Social Service Occupations', 40370, 12.634, 35.84, 38.52, 80130), 
            ('Community and Social Service Occupations', 56140, 17.570, 25.02, 26.71, 55560), 
            ('Legal Occupations', 23200, 7.261, 41.05, 50.79, 105640), 
            ('Educational Instruction and Library Occupations', 178700, 55.928, 26.89, 29.89, 62180), 
            ('Arts, Design, Entertainment, Sports, and Media', 48850, 15.289, 27.89, 31.80, 66140), 
            ('Healthcare Practitioners and Technical Occupations', 171850, 53.785, 40.75, 47.28, 98350), 
            ('Healthcare Support Occupations', 139350, 43.614, 17.03, 18.43, 38330), 
            ('Protective Service Occupations', 139350, 20.002, 27.33, 30.45, 63330), 
            ('Food Preparation and Serving Realted Occupations', 254380, 79.613, 15.45, 17.32, 36030), 
            ('Building and Grounds Cleaning and Maintenance Occupations', 83240, 26.053, 17.21, 19.20, 39930), 
            ('Personal Care and Service Occupations', 61720, 19.316, 17, 19.87, 41340), 
            ('Sales and Related Occupations', 294420, 92.144, 18.43, 24.80, 51580), 
            ('Office and Administrative Support Occupations', 370370, 115.915, 21.12, 22.90, 47630), 
            ('Farming, Fishing and Forestry Occupations', 24300, 7.606, 15.07, 17.78, 36980), 
            ('Construction and Extraction Occupations', 161780, 50.632, 29.90, 32.23, 67030),
            ('Installation, Maitenance, and Repair Occupations', 125650, 39.324, 27.38, 29.15, 60640),
            ('Production Occupations', 168080, 52.605, 21.10, 24.17, 50270),
            ('Transportation and Material Moving Occupations', 243690, 76.269, 19.41, 23.20, 48260),
            ('Science', 0, 0, 0, 0, 100),
            ('Example', 100, 0, 0, 0, 0)]

c.executemany("INSERT INTO jobs VALUES (?,?,?,?,?,?)", jobs)


#Query the Database before update and delete
c.execute("SELECT rowid, * FROM jobs")
items = c.fetchall()

for item in items:
    print(item)


# Update Records
c.execute("""UPDATE jobs SET job_sector = null
            WHERE employed = 0
    """)


# Delete Records
c.execute("DELETE from jobs WHERE annual_mean_wage = 0")


#Query the Database after update and delete
c.execute("SELECT rowid, * FROM jobs")
items = c.fetchall()

for item in items:
    print(item)


# Query the database for the highest salaried job
c.execute("SELECT MAX(annual_mean_wage), * FROM jobs")
print("The following job has the highest wage: \n", c.fetchone())


# Query the database for the numver of jobs that have more 
# than 20 people per every 1000 jobs
c.execute("SELECT COUNT(*) FROM jobs WHERE employment_per_1000_jobs > 20")
employ = c.fetchall()

for employed in employ:
    print("There are", employed, "jobs that have more than 20 people working for 1000 jobs.")


#Commit our command
conn.commit()

#Close our connection
conn.close()
#drop tables 
drivers_table_drop="DROP TABLE IF EXISTS drivers ;"


#create tables
drivers_table_create="""
CREATE TABLE IF NOT EXISTS drivers(
							givenName varchar,
							familyName varchar,
							url varchar,
							dateOfBirth timestamp, 
							nationality varchar NOT NULL,
                            permanentNumber int, 
                            code varchar,
                            PRIMARY KEY(givenName, familyName)
							)"""

drivers_table_insert="""
INSERT INTO drivers ( givenName, familyName, url, dateOfBirth, nationality,  permanentNumber, code) 
VALUES ( %s, %s, %s,%s, %s, %s, %s)
"""

drop_table_queries = [drivers_table_drop]
create_table_queries=[drivers_table_create]

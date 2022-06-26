import psycopg2 # python driver to set connexion to Postgres
from sql_queries import drop_table_queries, create_table_queries

def create_database():
	#connect to the default database :
	conn=psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=admin" )
	conn.set_session(autocommit=True)
	cur=conn.cursor()

	#drop f1_api db if it exists 
	cur.execute("DROP DATABASE IF EXISTS f1_api")
	#create f1_api db where to host all tables 
	cur.execute("CREATE DATABASE f1_api WITH ENCODING 'utf8' TEMPLATE template0")

	#close the connection to the default database
	conn.close()

	#connect to the f1_api db database
	conn=psycopg2.connect("host=127.0.0.1 dbname=f1_api user=postgres password=admin" )
	cur=conn.cursor()

	return cur, conn


def drop_tables(cur, conn):
	for query in drop_table_queries:
		cur.execute(query)
		conn.commit()
		print('dropping table is completed')
def create_tables(cur, conn):
	for query in create_table_queries:
		cur.execute(query)
		conn.commit()
		print('creating table is completed')

def main():
	cur, conn = create_database()
	drop_tables(cur, conn)
	create_tables(cur, conn)

	conn.close()

if __name__=="__main__":
	main()



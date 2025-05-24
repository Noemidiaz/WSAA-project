
# DAO file
# Data layer that connects to mental_health database
# It establishes a connection to my MySQL database using the credentials in dbconfig.py



import mysql.connector
import dbconfig as cfg


class MentalHealthDAO:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )
        self.cursor = self.connection.cursor()


    def create(self, survey):
        sql = '''
            INSERT INTO mental_health_survey 
            (name, age, gender, location, service_type, provider_name)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (
            survey['name'],
            survey['age'],
            survey['gender'],
            survey['location'],
            survey['service_type'],
            survey['provider_name']
        )
        self.cursor.execute(sql, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def get_all(self):
        self.cursor.execute("SELECT * FROM mental_health_survey")
        results = self.cursor.fetchall()
        return [self.convert_to_dict(row) for row in results]

    def find_by_id(self, id):
        sql = "SELECT * FROM mental_health_survey WHERE id = %s"
        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()
        return self.convert_to_dict(row)

    def update(self, id, survey):
        sql = '''
            UPDATE mental_health_survey 
            SET name=%s, age=%s, gender=%s, location=%s, 
                service_type=%s, provider_name=%s
            WHERE id=%s
        '''
        values = (
            survey['name'],
            survey['age'],
            survey['gender'],
            survey['location'],
            survey['service_type'],
            survey['provider_name'],
            id
        )
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete(self, id):
        sql = "DELETE FROM mental_health_survey WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.connection.commit()

    def convert_to_dict(self, row):
        if not row:
            return {}
        return {
            'id': row[0],
            'name': row[1],
            'age': row[2],
            'gender': row[3],
            'location': row[4],
            'service_type': row[5],
            'provider_name': row[6]
        }


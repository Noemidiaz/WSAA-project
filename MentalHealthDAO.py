
#  DAO file
# Data layer that connects to mental_health database in MySQL

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

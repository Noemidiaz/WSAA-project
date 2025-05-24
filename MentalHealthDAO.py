
#  DAO file

# Data layer that connects to a database

import mysql.connector
import dbconfig as cfg


class MentalHealthDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
from flask import Flask
from os.path import dirname, basename, isfile
import glob
import mysql.connector
from mysql.connector import errorcode
from server import app
from server.controller import (account_route)

if __name__ == "__main__":
	Flask.run(app, host="0.0.0.0", port=8000, debug=True)
	

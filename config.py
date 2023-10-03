from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from urllib import parse
import pymongo
import mysql.connector
import ssl
import certifi


#=======================GOOGLE API KEY=================================
api_key = 'AIzaSyAn-Brd_kFjXpcB6WSL4O0ij_-udPYdDRo'
youtube = build('youtube', 'v3', developerKey=api_key)


#======================MONGODB CONNECTION==============================
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://bageetha:PxiU2ioVp7w0x4fV@cluster0.wkxkdx1.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
database = client["youtube"]
collection = database["channel_information"]

#=====================SQLALCHEMY FOR SEND AS DATAFRAME================
engine = create_engine('mysql+mysqlconnector://root:RoshanNew@localhost/youtube_data')


#=====================MYSQL - PYTHON CONNECTION=======================
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="RoshanNew",
  database="youtube_data"
)
mycursor = mydb.cursor()

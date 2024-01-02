from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing exception file")
    except Exception as e:
        ML=CustomException(e,sys)
        logging.info(ML.error_message)

        return "heloooooooooooooo"



if __name__=='__main__':
    app.run(debug=True)
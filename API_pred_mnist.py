from fastapi import FastAPI, File, UploadFile
from typing import Annotated
import requests
import uvicorn
from bs4 import BeautifulSoup

import pickle 


# load model mnist
digit=open("trained_model/mnist_digit",'rb')


digit = pickle.load(digit)

# load model emnist
letter=open("trained_model/mnist_letter",'rb')
letter = pickle.load(letter)



def send_image (image):

    """
    model.predict
    
    """
    dp=digit.predict(image)
    dl=letter.predict(image)

    return  dp,dl



app=FastAPI()


from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
    )

@app.post("/image")
async def create_upload_file(image: UploadFile):
    return send_image(image)


uvicorn.run(app)



       
    


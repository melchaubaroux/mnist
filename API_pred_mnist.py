from fastapi import FastAPI, File, UploadFile
from typing import Annotated
import requests
import uvicorn
from bs4 import BeautifulSoup
# from transformers import AutoTokenizer, AutoModelForCausalLM
import pickle 

# # load model gemma
# huggingface_token = "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"
# tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b-it", use_auth_token=huggingface_token)
# model = AutoModelForCausalLM.from_pretrained("google/gemma-7b-it", use_auth_token=huggingface_token)

# load model mnist
digit=open("mnist_digit",'rb')


digit = pickle.load(digit)

# load model emnist
letter=open("mnist_letter",'rb')
letter = pickle.load(letter)


def send_text (text): return 0


    # input_text = text
    # input_ids = tokenizer(input_text, return_tensors="pt")

    # outputs = model.generate(**input_ids)
    # # print(tokenizer.decode(outputs[0]))

    # return tokenizer.decode(outputs[0])


    

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


@app.post("/chatbot")
def chatbot(text):
    return send_text (text)  

    
uvicorn.run(app)



       
    


from typing import Optional
from joblib import load
from fastapi import FastAPI, Request, Form, Depends
from DataModel import DataModel2
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI()
templates=Jinja2Templates(directory="templates")

"""@app.get("/")
def read_root():
   return {"Hello": "World"}"""


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict/")
def make_predictions(dataModel:DataModel2):  
   df = pd.Series(dataModel)
   #df.columns = dataModel.columns()
   re=df[0][1]
   model = load("assets/pipeline.joblib")
   serie=pd.Series(re)
   result = model['model'].predict(model['tf-idf'].transform(serie))
   res=int(result[0])
   return res

@app.get("/basic",response_class=HTMLResponse)
def read_pred(request:Request):
   return templates.TemplateResponse("ind.html",{"request":request})

@app.post("/basic",response_class=HTMLResponse)
def predecir(request:Request, form_data: DataModel2=Depends(DataModel2.as_forms)):
   des=make_predictions(form_data)
   tot=""
   if des==1:
      tot="La persona podria presentar tendencias suicidas"
   else:
      tot="la persona no parece mostrar tendencias suicidas"
   return templates.TemplateResponse("ind.html",{"request":request,"response":tot})


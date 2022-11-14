from pydantic import BaseModel
from fastapi import Form

class DataModel2(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    mesage: str
    
    #admission_points: float

#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib. "Admission Points"
    @classmethod
    def as_forms(
        cls,
        mesage: str = Form(...)
    ):
        return cls(
            mesage=mesage
        )

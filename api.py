from fastapi import FastAPI, Depends
import orm.repo as repo
import orm.esquemas as esquemas
from sqlalchemy.orm import Session
from orm.config import generador_sesion

app = FastAPI()

@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("Api consultando todos los alumno")
    return repo.alumno(sesion)
    
@app.get("/alumnos/{id}")
def alumno_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificacion_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificacion por id alumno")
    return repo.calificacion_por_idAlumno(sesion, id)

@app.get("/alumnos/{id}/fotos")
def foto_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando foto por id alumno")
    return repo.foto_por_idAlumno(sesion, id)

@app.get("/fotos/{id}")
def foto_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando foto por id")
    return repo.foto_por_id(sesion, id)

@app.get("/calificaciones/{id}")
def calificacion_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando calificacion por id")
    return repo.calificacion_por_id(sesion, id)

@app.delete("/fotos/{id}")
def borra_foto_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando foto por id")
    repo.borra_foto_por_id(sesion, id)
    return{"Foto_borrada":"OK"}

@app.delete("/calificaciones/{id}")
def borra_calificacion_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando calificacion por id")
    repo.borra_calificacion_por_id(sesion, id)
    return{"Calificacion_borrada":"OK"}

@app.delete("/alumnos/{id}/calificaciones")
def borra_calificacion_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando calificacion por id alumno")
    repo.borra_calificacion_por_idAlumno(sesion, id)
    return{"Calificacion_borrada":"OK"}

@app.delete("/alumnos/{id}/fotos")
def borra_foto_por_id_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando foto por id alumno")
    repo.borra_foto_por_idAlumno(sesion, id)
    return{"Foto_borrada":"OK"}

@app.delete("/alumnos/{id}")
def borra_alumno_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando alumno por id")
    repo.borra_calificacion_por_idAlumno(sesion, id)
    repo.borra_foto_por_idAlumno(sesion, id)
    repo.borra_alumno_por_id(sesion, id)
    return{"Alumno_borrado":"OK"}

@app.post("/alumnos")
def guarda_alumno(alumno:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    print(alumno)
    return repo.guardar_alumno(sesion, alumno)

@app.put("/alumnos/{id}")
def actualiza_alumno(id:int, info_alumno:esquemas.AlumnoBase, sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_alumno_por_id(sesion, id, info_alumno)

@app.post("/alumnos/{id}/calificaciones")
def guarda_calificacion_alumno(id:int, calificacion:esquemas.CalificacionBase, sesion:Session=Depends(generador_sesion)):
    print(calificacion)
    return repo.guarda_calificacion_alumno(sesion, id, calificacion)

@app.put("/calificaciones/{id}")
def actualiza_calificacion(id:int, info_calificacion:esquemas.CalificacionBase, sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_calificacion_por_id(sesion, id, info_calificacion)

@app.post("/alumnos/{id}/fotos")
def guarda_foto_alumno(id:int, foto:esquemas.FotoBase, sesion:Session=Depends(generador_sesion)):
    print(foto)
    return repo.guarda_foto_alumno(sesion, id, foto)

@app.put("/fotos/{id}")
def actualiza_foto(id:int, info_foto:esquemas.FotoBase, sesion:Session=Depends(generador_sesion)):
    return repo.actualiza_foto_por_id(sesion, id, info_foto)
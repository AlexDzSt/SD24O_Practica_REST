from fastapi import FastAPI, Depends
import orm.repo as repo
from sqlalchemy.orm import Session
from orm.config import generador_sesion

app = FastAPI()

### Alumnos ###
@app.get("/alumnos")
def lista_alumnos(sesion: Session = Depends(generador_sesion)):
    print("Api consultando lista de alumnos")
    return repo.alumno(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificacion_por_idAlumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando calificacion por id de Alumno")
    return repo.calificacion_por_idAlumno(sesion, id)

@app.get("/alumnos/{id}/fotos")
def foto_por_idAlumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando fotos por id de Alumno")
    return repo.foto_por_idAlumno(sesion, id)

@app.delete("/alumnos/{id}")
def eliminar_alumno_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api eliminando alumno por id")
    return repo.del_alumno_por_id(sesion, id)

@app.delete("/alumnos/{id}/calificaciones")
def eliminar_calificaciones_por_idAlumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api eliminando calificaciones del alumno por id")
    return repo.del_calificacion_por_idAlumno(sesion, id)

@app.delete("/alumnos/{id}/fotos")
def eliminar_fotos_por_idAlumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api eliminando fotos del alumno por id")
    return repo.del_foto_por_idAlumno(sesion, id)


### Fotos ###         
@app.get("/fotos/{id}")
def foto_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando foto por id")
    return repo.foto_por_id(sesion, id)

@app.delete("/fotos/{id}")
def eliminar_foto_por_idAlumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api eliminando foto por id")
    return repo.del_foto_por_id(sesion, id)

### Calificaciones ###
@app.get("/calificaciones/{id}")
def calificacion_por_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api consultando calificación por id")
    return repo.calificacion_por_id(sesion, id)

@app.delete("/calificaciones/{id}")
def eliminar_calificacion(id: int, sesion: Session = Depends(generador_sesion)):
    print("Api eliminando calificación por id")
    return repo.del_calificacion_por_id(sesion, id)

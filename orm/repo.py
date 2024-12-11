import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

### Alumnos ###
# SELECT * FROM app.alumnos
def alumno(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

# SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_por_id(sesion:Session, id_alumno: int):
    print("SELECT * FROM app.alumnos WHERE id=", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()

# DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def borra_alumno_por_id(sesion: Session, id_alumno: int):
    print("DELETE FROM app.alumnos WHERE id_alumnos=", id_alumno)
    borra_calificacion_por_idAlumno(sesion, id_alumno)
    borra_foto_por_idAlumno(sesion, id_alumno)
    alumn = alumno_por_id(sesion, id_alumno)
    if alumn is not None:
        sesion.delete(alumn)
        sesion.commit()
    respuesta = {"mensaje":"Alumno eliminado"}
    return respuesta
    
### Fotos ###
# SELECT * FROM app.fotos
def foto(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()
    
# SELECT * FROM app.fotos WHERE id={id_fo}
def foto_por_id(sesion:Session, id_foto: int):
    print("SELECT * FROM app.fotos WHERE id=", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()
    
# SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def foto_por_idAlumno(sesion:Session, id_alumno: int):
    print("SELECT * FROM app.fotos WHERE id_alumnos=", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).first()

# DELETE FROM app.fotos WHERE id_fotos={id_f}
def borra_foto_por_id(sesion:Session, id_foto:int):
    print("DELETE FROM app.fotos WHERE id_fotos=", id_foto)
    foto = foto_por_id(sesion, id_foto)
    if foto is not None:
        sesion.delete(foto)
        sesion.commit()
    respuesta = {"mensaje":"Foto eliminada"}
    return respuesta
    
# DELETE FROM app.fotos WHERE id_alumnos={id_al}
def borra_foto_por_idAlumno(sesion:Session, id_alumno:int):
    print("DELETE FROM app.fotos WHERE id_alumnos=", id_alumno)
    foto_alumno = foto_por_idAlumno(sesion, id_alumno)
    if foto_alumno is not None:
        sesion.delete(foto_alumno)
        sesion.commit()
    respuesta = {"mensaje":"Foto por alumno eliminada"}
    return respuesta

### Calificaciones ###
# SELECT * FROM app.calificaciones
def calificacion(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

# SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificacion_por_id(sesion:Session, id_calificacion: int):
    print("SELECT * FROM app.calificaciones WHERE id=", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first()

# SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificacion_por_idAlumno(sesion:Session, id_alumno: int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos=", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).first()

# DELETE FROM app.calificaciones WHERE id_calificaciones={id_cal}
def borra_calificacion_por_id(sesion:Session, id_calificacion:int):
    print("DELETE FROM app.calificaciones WHERE id_calificaciones=", id_calificacion)
    calif = calificacion_por_id(sesion, id_calificacion)
    if calif is not None:
        sesion.delete(calif)
        sesion.commit()
    respuesta = {"mensaje":"Calificacion eliminada"}
    return respuesta

# DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def borra_calificacion_por_idAlumno(sesion:Session, id_alumno:int):
    print("DELETE FROM app.calificaciones WHERE id_alumnos= ", id_alumno)
    calif_alumno = calificacion_por_idAlumno(sesion, id_alumno)
    if calif_alumno is not None:
        sesion.delete(calif_alumno)
        sesion.commit()
    respuesta = {"mensaje":"Calificacion por alumno eliminada"}
    return respuesta
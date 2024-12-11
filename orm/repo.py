import orm.modelos as modelos
import orm.esquemas as esquemas
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

# POST ("/alumnos”)
def guardar_alumno(sesion:Session, al_nuevo:esquemas.AlumnoBase):
    al_bd = modelos.Alumno()
    al_bd.nombre = al_nuevo.nombre
    al_bd.edad = al_nuevo.edad
    al_bd.domicilio = al_nuevo.domicilio
    al_bd.carrera = al_nuevo.carrera
    al_bd.trimestre = al_nuevo.trimestre
    al_bd.email = al_nuevo.email
    al_bd.password = al_nuevo.password
    
    sesion.add(al_bd)
    sesion.commit()
    sesion.refresh(al_bd)
    return al_bd
    
# PUT ("/alumnos/{id})
def actualiza_alumno_por_id(sesion:Session, id_al:int, al_esquema:esquemas.AlumnoBase):
    al_bd = alumno_por_id(sesion,id_al)
    if al_bd is not None:
        al_bd.nombre = al_esquema.nombre
        al_bd.edad = al_esquema.edad
        al_bd.domicilio = al_esquema.domicilio
        al_bd.carrera = al_esquema.carrera
        al_bd.trimestre = al_esquema.trimestre
        al_bd.email = al_esquema.email
        al_bd.password = al_esquema.password
        
        sesion.commit()
        sesion.refresh(al_bd)
        
        print(al_esquema)
        return al_esquema
    else:
        respuesta = {"mensaje":"No existe el alumno"}
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

# POST("/alumnos/{id}/fotos")
def guarda_foto_alumno(sesion:Session, id_al:int, foto_nueva:esquemas.FotoBase):
    al = alumno_por_id(sesion, id_al)
    if al is not None:
        foto_bd = modelos.Foto()
        foto_bd.id_alumno = id_al
        foto_bd.titulo = foto_nueva.titulo
        foto_bd.descripcion = foto_nueva.descripcion
        foto_bd.ruta = foto_nueva.ruta
        
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        
        return foto_bd
    else:
        respuesta = {"mensaje":"El alumno no existe"}
        return respuesta
    
# PUT("/fotos/{id}")
def actualiza_foto_por_id(sesion:Session, id_foto:int, foto_esquema:esquemas.FotoBase):
    foto_bd = foto_por_id(sesion, id_foto)
    if foto_bd is not None:
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta = foto_esquema.ruta
        
        sesion.commit()
        sesion.refresh(foto_bd)
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {"mensaje":"La foto no existe"}
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

# POST ("/alumnos/{id}/calificaciones")
def guarda_calificacion_alumno(sesion:Session, id_al:int, cal_nueva:esquemas.CalificacionBase):
    al = alumno_por_id(sesion, id_al)
    if al is not None:
        cal_bd = modelos.Calificacion()
        cal_bd.id_alumno = id_al
        cal_bd.uea = cal_nueva.uea
        cal_bd.calificacion = cal_nueva.calificacion
        
        sesion.add(cal_bd)
        sesion.commit()
        sesion.refresh(cal_bd)
        
        return cal_bd
    else:
        respuesta = {"mensaje":"El alumno no existe"}
        return respuesta
    
# PUT ("/calificaciones/{id}")
def actualiza_calificacion_por_id(sesion:Session, id_cal:int, cal_esquema:esquemas.CalificacionBase):
    cal_bd = calificacion_por_id(sesion, id_cal)
    if cal_bd is not None:
        cal_bd.uea = cal_esquema.uea
        cal_bd.calificacion = cal_esquema.uea
        
        sesion.commit()
        sesion.refresh(cal_bd)
        print(cal_esquema)
        return cal_esquema
    else:
        respuesta = {"mensaje":"La calificacion no existe"}
        return respuesta
    
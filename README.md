# Proyecto fin de ciclo

 Módulo odoo OELS English

 ![Screenshot](oels.jpeg)

## Descripción

El proyecto se trata de un módulo para la gestión de una academia de inglés en Santiago de Compostela, OELS English. Este tiene el objetivo principal de llevar un registro y seguimiento de los profesores,alumnos,grupos,notas y recordatorios.

Esta idea surge a raíz de ver lo cómodos y intuitivos que son los ERPs como odoo para trabajar, ofreciendo un servicio sencillo pero funcional.

El módulo consta de las siguientes partes:

- Teachers, aquí se podrá dar de alta a nuevos profesores y visualizar los ya existentes, además de visualizar información de sus estudiantes y grupos.

- Students, bastante similar al apartado anterior pero añadiendo el profesor que les da clase y el grupo al que pertenecen. Además se podrá visualizar las notas y recordatorios del alumno.

- Groups, se encargará de almacenar y registrar toda la información relativa a las clases de estudiantes, referenciando al profesor y visualizando los estudiantes de cada grupo.

- Grades, permitirá añadir las notas de los alumnos,tipo de examen y su fecha.

- Reminders, podrás añadir recordatorios sobre un alumno, ya sea por motivos de trámites o faltas de asistencia

Respecto a las características y funcionalidades del módulo podemos encontrar:

- Campos autoincrementales,many2one,one2many,date,fieldSelection y binary 
- Widgets
- Validación de campos
- Vistas formulario,árbol y kanban
- Filtros y agrupaciones personalizadas en el apartado de estudiantes
- Log de notificaciones(informa sobre cualquier modificacion o dato nuevo añadido)
- Exportar a pdf el registro de un profesor y sus alumnos
- Selección de estados en la sección reminders
- Herencia de vistas
- Caja de comentarios
- Fichero de seguridad
- Configuración del módulo para que aparezca en el despegable de apps y en la primera posicion de la sección de aplicaciones


## Instalación / Puesta en marcha

Para la puesta en marcha es necesario tener odoo14, puedes realizar una instalación completa mediante: [Link a Linuxize](https://linuxize.com/post/how-to-install-odoo-14-on-ubuntu-20-04/) o realizar una instalación mas rápida pero menos configurable desde docker.

En caso de querer realizar la instalación desde docker necesitas realizar los siguientes pasos:

- Instalar dockerhub mediante el comando sudo apt install docker.io
- Lanzar el servicio de postgress con docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:13
- Finalmente arrancar el servicio de odoo y nuestro módulo custom con docker run -v /path/to/addons:/mnt/extra-addons -p 8069:8069 --name odoo --link db:db -t odoo, donde /path/to/addons será la ruta que contenga el módulo privado.

Una vez realizado todo lo anterior, deberemos ingresar a la dirección localhost:8069 y crear la base de datos. Tras finalizar, estaremos dentro de la página principal de odoo pero aún tendremos que realizar un paso más para visualizar nuestro módulo. Para poder acceder a este, es necesario actualizar la lista de apps, que es solo posible desde el modo desarollador. Si escribimos http://localhost:8069/web?debug=1 en la url, accederemos al modo debug y desde ahí podremos ver una opción llamada actualizar lista de apps. Tras esto ya tendremos nuestro módulo disponible en la parte posterior y además podremos acceder a el mediante el desplegable de arriba izquierda.

## Uso

El módulo consta de 5 modelos principales que son los profesores,grupos,alumnos,notas y recordatorios. Todos estos tienen el objetivo de organizar una escuela de inglés en sus diferentes ámbitos.

Cualquier cambio que realices, ya sea una modificación o un comentario, se mostrará en el apartado log que hay abajo de cada modelo.

Algunos modelos tienen una relacion directa ya que en el caso de notas y recordatorios, no podrán ser añadidos sin un estudiante relacionado.

La funcionalidad de cada modelo es:

Profesores, puedes añadir,modificar o borrar los profesores relativos a la academia Oels English junto con sus respectivos datos, a la vez que visualizas los estudiantes y grupos a los que dan clase. Además, tienes la opción de imprimir ese registro en formato pdf, tanto del profesor como el profesor y sus alumnos. Contará con una vista en árbol y será el primer modelo que veas al entrar al módulo. Desde ahí, podrás visualizar su información personal pero será necesario entrar al registro para acceder al resto.

Grupos, permite añadir un grupo en relación a una clase de alumnos, el nivel de inglés con el que trabajan, su horario y el profesor. Además podrás visualizar los alumnos que están registrados en ese mismo grupo.

Estudiantes, tiene bastante semejanza con los campos de profesor, con la diferencia de que puedes añadir el docente que le da clase y el grupo al que pertenecen. También se podrán visualizar sus notas y recordatorios. Su vista principal será en kanban, pudiendo además aplicar filtros y agrupaciones por sus grupos,profesores o género. 

Notas, su objetivo principal será guardar y mostrar las notas relativas a los estudiantes, la fecha de realización,tipo de examen y un comentario en específico.

Recordatorios, puedes almacenar un recordatorio sobre un trámite pendiente de algún alumno o una falta de asistencia.

## Sobre el autor

Soy un estudiante del IES San Clemente que desde pequeño le llamó mucho la atención todo lo relacionado con las nuevas técnologias. Con lo que aprendí en estos ultimos meses, diría que mi punto fuente reside sobreotodo en el desarollo android pero también me gusta bastante todo lo relacionado con la gestión y manejo de datos, motivo por el que escogí utilizar odoo como proyecto de fin de ciclo. Además, lo vi una buena oportunidad de trabajar con un lenguaje de programación diferente a Java y así iniciarme un poco en el desarollo Python.

Como puntos positivos sobre mi personalidad como programador creo que:

- Creativo
- Me gusta aprender sobre nuevas tecnologías
- Trabajo bien bajo presión
- Resolutivo

## Licencia

Copyright (C)  2021  Hugo Pires Rodríguez.
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in the section entitled "GNU
    Free Documentation License".


## Índice

> *TODO*: Simplemente indexa ordenadamente todo tu proyecto.

1. Anteproyecto
    * 1.1. [Idea](doc/templates/1_idea.md)
    * 1.2. [Necesidades](doc/templates/2_necesidades.md)
2. [Análisis](doc/templates/3_analise.md)
3. [Planificación](doc/templates/4_planificacion.md)
4. [Diseño](doc/templates/5_deseño.md)
5. [Implantación](doc/templates/6_implantacion.md)


## Guía de contribución

Una buena implementación puede ser añadir diferentes estilos y temas mediante css y js. Además se podrían añadir nuevos módulos para dar una funcionalidad mas amplia que se adapte a este o a otro negocio.

## Links

[Link instalación odoo](https://linuxize.com/post/how-to-install-odoo-14-on-ubuntu-20-04/)<br>
[Link a la documentación de odoo](https://www.odoo.com/documentation/14.0/es/)<br>
[Link a la documentación de python](https://docs.python.org/es/3/)<br>
[Link a la documentación de docker](https://docs.docker.com/)


# Base de datos que utilizo para almacenar registros
import sqlite3
# Libreria que permite utilizar expresiones regulares para validar informacion
import re
# Libreria que utilizo para conseguir la fecha y hora exacta al momento de registrar cambios en la base de datos
from datetime import datetime
# Libreria utilizada para mostrar popups o mensajes de alerta a la hora de realizar algun cambio en el registro de datos
from tkinter import messagebox


# Clase ABMC: maneja la logica relacionada a las funciones de Alta, Baja, MOdificacion y Consulta del sistema
class Abmc():
    # Metodo de instancia
    def __init__(self,):
        # Matchea con lineas de texto que solo tengan numeros entre 0  y 9
        self.regex_numeros = "^[0-9]+$"

        # Matchea con lineas de texto que solo tengan caracteres y con una longitud entre 1  y 60 caracteres
        self.regex_palabra = r"^[.,a-zA-Z\s]{1,60}$"

        # Matchea con lineas de texto que tengan caracteres o numeros y con una longitud entre 1 y 60 caracteres
        self.regex_vacio = r"^[,.a-zA-Z0-9_\s]{1,60}$"

    # --------FUNCIONES--------------

    # Funcion que devuelve una conexion a la base de datos
    def crear_db(self,):
        # El metodo "connect" de sqlite3 me permite conectarme a una base de datos con el nombre que es enviado como parametroo
        # En el caso de que haya una base de datos con ese nombre en el mismo directorio que el archivo, este metodo nos conecta a esa base de datos
        # En el caso de que NO haya una base de datos con ese nombre, este metodo crea la base de datos y luegos nos conecta
        basedatos = sqlite3.connect("libreria.db")
        # Devuelvo la referencia a la base de datos
        return basedatos

    # Funcion para crear la tabla de registros de libros en nuestra base de datos
    # Toma como parametro a la base de datos que estamos utilizando
    def crear_tabla_libro(self, ):

        # Consigo la referencia a la base de datos utilizando la funcion de conexion
        basedatos = self.crear_db()
        # Creo un objeto cursor que me permite ejecutar sentencias SQL en la base de datos
        cursorbdd = basedatos.cursor()

        # Defino una sentencia SQL que me permite crear la tabla "libros" si es que no fue creada con anterioridad
        sql = (
            "CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " titulo TEXT,"
            " precio INTEGER,"
            " editorial TEXT,"
            " genero TEXT,"
            " autor TEXT,"
            " fecha_mod DATETIME)"
        )

        # Ejecuta la sentencia utilizando el cursor
        cursorbdd.execute(sql)

        # Utilizo el metodo commit para guardar los cambios realizados en la base de datos
        basedatos.commit()

    # Funcion para determinar si los botones de actualizacion y borrado se encuentran activos
    # Esta funcion toma como parametros a los objetos boton de actualizacion y boton de borrado; tambien toma un parametro booleano deshabilitar
    def toggle_botones(self, upd_boton, borrar_boton, deshabilitar):
        # Si dehabilitar es "True", deshabilitamos los botones de actualizacion y borrado
        if deshabilitar:
            # "state" es un atributo de los botones de Tkinter que determina si el boton es clickeable o no
            upd_boton["state"] = "disabled"
            borrar_boton["state"] = "disabled"
        # En el caso de que deshabilitar sea "False", hago que los botones sean clickeables
        else:
            upd_boton["state"] = "normal"
            borrar_boton["state"] = "normal"

    # Funcion para vaciar todos los campos de entrada luego de realizar una alta, baja o modificacion
    # Toma como parametro a los entry del sector principal del programa
    def vaciar_entradas(self, titulo, precio, editorial, genero, autor):
        # El metodo "set("") nos permite vaciar cada uno de los campos de entrada
        titulo.set("")
        precio.set("")
        editorial.set("")
        genero.set("")
        autor.set("")

    # Funcion para rellena los entry con datos del item seleccionado en treeview
    # Toma como parametro al objeto listado, los campos de entrada y los botones de borrar y actualizar

    def select_item(
        self, lista, id, titulo, precio, editorial, genero, autor, borrar_boton, upd_boton
    ):

        try:
            # Relleno los campos de entrada con los valores del item seleccionado dentro de la lista
            id.set(lista["text"])
            titulo.set(lista["values"][0])
            precio.set(lista["values"][1].lstrip("$"))
            editorial.set(lista["values"][2])
            genero.set(lista["values"][3])
            autor.set(lista["values"][4])
        except IndexError:
            # En el caso de que haya un error a la hora de conseguir los valores del item, se sale de la funcion
            return

        # Habilito los botones de actualizar y eliminar ya que estoy seleccionando un registro
        self.toggle_botones(upd_boton, borrar_boton, False)

    # Funcion para validar los campos de entrada de dato teniendo en cuenta diferentes criterios

    def validar_entrada(self, titulo, precio, editorial, genero, autor):

        # Cargo los patrones de regex que voy a usar para validar cada campo
        patron_num = re.compile(self.regex_numeros)
        patron_text = re.compile(self.regex_palabra)
        patron_vacio = re.compile(self.regex_vacio)

        # Variable en la que concateno cada campo que tenga un error
        errores = ""

        if not re.fullmatch(patron_vacio, titulo.get()):
            errores += "\n-Titulo"
        if not re.fullmatch(patron_num, precio.get()):
            errores += "\n-Precio"
        if not re.fullmatch(patron_text, editorial.get()):
            errores += "\n-Editorial"
        if not re.fullmatch(patron_text, genero.get()):
            errores += "\n-Genero"
        if not re.fullmatch(patron_text, autor.get()):
            errores += "\n-Autor"

        # Si la variable error no esta vacia, muestra un mensaje indicando los campos que no estan ingresados correctamente
        if errores != "":
            messagebox.showerror(
                title="Error",
                message="Los siguientes campos no se ingresaron correctamente: " + errores,
            )
            return True

    # Funcion para poblar el listado treeview
    # Toma como parametros al listado, el campo de entrada de filtro y una variable "borrar_filtro" que se utiliza
    # Para determinar si se hizo click en el boton de borrar filtro
    def cargar_listado(
        self, tree, filtro, borrar_filtro=""
    ):

        # Me conecto a la base de datos
        basedatos = self.crear_db()
        # Creo un cursor apuntando a la base de datos
        cursorbdd = basedatos.cursor()

        # Cargo una variable con el contenido del campo de entrada de filtro
        busqueda = filtro.get()

        # El atributo borrar_filtro es una bool
        # Lo utilizo para determinar si se toco el boton de borrar filtros

        # En el caso de que el campo busqueda este vacio o si se hizo click en el boton de borrar filtros
        if busqueda == "" or borrar_filtro:
            # Vacia el campo de entrada de filtro
            filtro.set("")
            # Trae el listado completo de registros sin filtrar
            cursorbdd.execute("SELECT * FROM libros")
            # Creo un listado con los registros traidos de la base de datos
            lista_datos = cursorbdd.fetchall()
        else:
            # En el caso de que se haya ingresado informacion en el campo de entrada de filtro

            # Cargo una variable con la informacion agregada en el filtro
            datos = (busqueda,)
            # Con esta declaracion puedo traer todos los registros de la base de datos que contengan el titulo que busco
            # Utilizamos los caracteres "?" para hacer referencia a un parametro que vamos a indicar mas adelante
            sql_select = "SELECT * FROM libros WHERE titulo LIKE '%' || ? || '%' "
            # Ejecuto la secuencia SQL
            # El array "datos" contiene el parametro que va a remplazar el simbolo "?" de la secuencia "sql_select"
            cursorbdd.execute(sql_select, datos)
            # Creo un listado con los registros traidos de la base de datos
            lista_datos = cursorbdd.fetchall()

        # Borra todos los registros del tree view
        for i in tree.get_children():
            tree.delete(i)

        # Recorre el listado de registros y los introduce en el treeview
        for item in lista_datos:

            # Formateo la fecha para mostrarla en el formato de dd/mm/yyyy h:m:s
            fecha = datetime.strptime(str(item[6]), "%Y/%m/%d %H:%M:%S")
            fecha_format = datetime.strftime(fecha, "%d/%m/%Y %H:%M:%S")

            # Agrego un registro en el listado por cada item traido de la base de datos
            tree.insert(
                "",
                "end",
                text=str(item[0]),
                values=(
                    item[1],
                    "$" + str(item[2]),
                    item[3],
                    item[4],
                    item[5],
                    fecha_format,
                ),
            )

    # Funcion para dar de baja registros de la base de datos
    # Toma como parametros al id del registro a eliminar, al objeto de boton de actualizar y borrar, al listado de registros
    # y a los campos de entrada del sector principal y de busqueda
    def funcion_baja(
        self,
        id,
        upd_boton,
        borrar_boton,
        tree,
        titulo,
        precio,
        editorial,
        genero,
        autor,
        busqueda,
    ):

        # Me conecto a la base de datos
        basedatos = self.crear_db()
        # Creo un cursor apuntando a la base de datos
        cursorbdd = basedatos.cursor()

        # En el caso de que el campo Id este vacio
        if id == "":
            # Se muestra un mensaje emergente indicando que no se selecciono ningun registro del listado
            messagebox.showinfo(
                title="Info", message="No se ha seleccionado ningun registro en el listado"
            )
            # Salgo de la funcion
            return

        # Muestro un mensaje de consulta al usuario
        if messagebox.askyesno(
            title="Confirmar eleccion", message="¿Desea eliminar el registro de la lista?"
        ):
            # En el caso de que el usuario haga click en el boton "Si" dentro del mensaje emergente ->

            # Secuencia SQL para eliminar el registro con el mismo id al ingresado
            sql_delete = "DELETE FROM libros WHERE id = ?"
            datos = (id,)
            cursorbdd.execute(sql_delete, datos)
            # Guardo los cambios en la base de datos
            basedatos.commit()
            # Muestro un mensaje indicando que el proceso ha finalizado con exito
            messagebox.showinfo(
                title="Info", message="Registro eliminado con exito")

        # Refresco el treeview luego de hacer un cambio
        self.cargar_listado(tree, busqueda)
        # Deshabilito el uso de los botones
        self.toggle_botones(upd_boton, borrar_boton, True)
        # Vacio los campos de entrada
        self.vaciar_entradas(titulo, precio, editorial, genero, autor)

    # Funcion para dar de alta registros
    # Toma como parametros a los campos de entrada, el listado de registros y los botones de actualizar y eliminar
    def funcion_alta(
        self, titulo, precio, editorial, genero, autor, upd_boton, borrar_boton, busqueda, tree
    ):
        # Me conecto a la base de datos
        basedatos = self.crear_db()
        # Creo un cursor apuntando a la base de datos
        cursorbdd = basedatos.cursor()

        # Consigo la fecha y hora actual
        horario_actual = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        # Sale de la funcion si algun dato ingresado es incorrecto
        if self.validar_entrada(titulo, precio, editorial, genero, autor):
            return

        # Creo una tupla con los datos ingresados en los campos de entrada
        datos = (
            titulo.get(),
            precio.get(),
            editorial.get(),
            genero.get(),
            autor.get(),
            horario_actual,
        )

        # creo una secuencia SQL que recibe como parametro al listado de datos ingresados
        sql_insert = "INSERT INTO libros (titulo, precio, editorial, genero, autor, fecha_mod) VALUES (?, ?, ?, ?, ?, ?)"
        # Ejecuto la secuencia y guardo el registro
        cursorbdd.execute(sql_insert, datos)
        basedatos.commit()
        # Muestro un mensaje indicando que el proceso ha finalizado con exito
        messagebox.showinfo(
            title="Info", message="Registro ingresado con exito!")

        # Refresco el treeview luego de hacer un cambio
        self.cargar_listado(tree, busqueda)
        # Vacio los campos de entrada
        self.vaciar_entradas(titulo, precio, editorial, genero, autor)
        # Deshabilito el uso de los botones
        self.toggle_botones(upd_boton, borrar_boton, True)

    # Funcion para modificar registros
    # Toma como parametros a los campos de entrada, el listado de registros y los botones de actualizar y eliminar
    def funcion_modificar(
        self,
        id_registro,
        titulo,
        precio,
        editorial,
        genero,
        autor,
        borrar_boton,
        upd_boton,
        busqueda,
        tree,
    ):

        # Me conecto a la base de datos
        basedatos = self.crear_db()
        # Creo un cursor apuntando a la base de datos
        cursorbdd = basedatos.cursor()

        # Verifico si se selecciono algun registro del listado
        if id_registro.get() == "":
            messagebox.showinfo(
                title="Info", message="No se ha seleccionado ningun registro en el listado"
            )
            return
        # Valido los datos ingresados
        elif self.validar_entrada(titulo, precio, editorial, genero, autor):
            return

        # Consigo la fecha y hora actual
        horario_actual = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        # Cargo una tupla con los datos a ingresar
        datos = (
            titulo.get(),
            precio.get(),
            editorial.get(),
            genero.get(),
            autor.get(),
            horario_actual,
            id_registro.get(),
        )

        # Muestro un mensaje de consulta al usuario
        if messagebox.askyesno(
            title="Confirmar eleccion", message="¿Desea modificar el registro de la lista?"
        ):
            # Modifica la informacion del registro que tenga el mismo id del item seleccionado en el listado
            sql_update = (
                "UPDATE libros SET titulo = ?, precio =?, editorial =?, genero = ?, autor = ?, fecha_mod = ? "
                "WHERE id = ?"
            )
            # Ejecuto la secuencia SQL y guardo los cambios en la base de datos
            cursorbdd.execute(sql_update, datos)
            basedatos.commit()
            # Muestro un mensaje indicando que el proceso ha finalizado con exito
            messagebox.showinfo(
                title="Info", message="Registro modificado con exito")

        # Refresco el treeview luego de hacer un cambio
        self.cargar_listado(tree, busqueda)
        # Vacio los campos de entrada
        self.vaciar_entradas(titulo, precio, editorial, genero, autor)
        # Deshabilito el uso de los botones
        self.toggle_botones(upd_boton, borrar_boton, True)

import sqlite3
import re
from datetime import datetime
from tkinter import messagebox


class Abmc():
    def __init__(self,):
        # Matchea con lineas de texto que solo tengan numeros entre 0  y 9
        self.regex_numeros = "^[0-9]+$"

        # Matchea con lineas de texto que solo tengan caracteres y con una longitud entre 4 y 60 caracteres
        self.regex_palabra = r"^[.,a-zA-Z\s]{2,60}$"

        # Matchea con lineas de texto que tengan caracteres o numeros y con una longitud entre 4 y 60 caracteres
        self.regex_vacio = r"^[,.a-zA-Z0-9_\s]{2,60}$"

    # --------FUNCIONES--------------

    def crear_db(self,):
        basedatos = sqlite3.connect("libreria.db")
        return basedatos

    def crear_tabla_libro(self, basedatos):
        basedatos = self.crear_db()
        cursorbdd = basedatos.cursor()

        sql = (
            "CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " titulo TEXT,"
            " precio INTEGER,"
            " editorial TEXT,"
            " genero TEXT,"
            " autor TEXT,"
            " fecha_mod DATETIME)"
        )

        cursorbdd.execute(sql)

        basedatos.commit()

    # Funcion para determinar si los botones de actualizacion y borrado se encuentran activos

    def toggle_botones(self, upd_boton, borrar_boton, deshabilitar):
        if deshabilitar:
            upd_boton["state"] = "disabled"
            borrar_boton["state"] = "disabled"
        else:
            upd_boton["state"] = "normal"
            borrar_boton["state"] = "normal"

    # Funcion para vaciar todos los campos de entrada luego de realizar una alta, baja o modificacion

    def vaciar_entradas(self, titulo, precio, editorial, genero, autor):
        titulo.set("")
        precio.set("")
        editorial.set("")
        genero.set("")
        autor.set("")

    # Funcion para rellena los entry con datos del item seleccionado en treeview

    def select_item(
        self, lista, id, titulo, precio, editorial, genero, autor, borrar_boton, upd_boton
    ):

        try:
            # Los siguientes datos salen del diccionario donde se guardan los valores del item que seleccione
            id.set(lista["text"])
            titulo.set(lista["values"][0])
            precio.set(lista["values"][1].lstrip("$"))
            editorial.set(lista["values"][2])
            genero.set(lista["values"][3])
            autor.set(lista["values"][4])
        except IndexError:
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

    def cargar_listado(
        self, tree, filtro, borrar_filtro=""
    ):
        basedatos = self.crear_db()
        cursorbdd = basedatos.cursor()
        busqueda = filtro.get()

        # el atributo borrar_filtro es una bool
        # para determinar si se toco el boton de borrar filtros

        if busqueda == "" or borrar_filtro:
            filtro.set("")
            cursorbdd.execute("SELECT * FROM libros")
            lista_datos = cursorbdd.fetchall()
        else:
            datos = (busqueda,)
            # Con esta declaracion puedo traer todos los registros de la base de datos que contengan el titulo que busco
            sql_select = "SELECT * FROM libros WHERE titulo LIKE '%' || ? || '%' "
            cursorbdd.execute(sql_select, datos)
            lista_datos = cursorbdd.fetchall()

        # Borra todos los registros del tree view
        for i in tree.get_children():
            tree.delete(i)

        # Recorre el listado de registros y los introduce en el treeview
        for item in lista_datos:

            # Formateo la fecha para mostrarla en el formato de dd/mm/yyyy h:m:s
            fecha = datetime.strptime(str(item[6]), "%Y/%m/%d %H:%M:%S")
            fecha_format = datetime.strftime(fecha, "%d/%m/%Y %H:%M:%S")

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

    # Funcion para dar de baja registros

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
        basedatos = self.crear_db()
        cursorbdd = basedatos.cursor()

        if id == "":
            messagebox.showinfo(
                title="Info", message="No se ha seleccionado ningun registro en el listado"
            )
            return

        # Se elimina el registro que tenga un id igual al item seleccionado del listado
        if messagebox.askyesno(
            title="Confirmar eleccion", message="¿Desea eliminar el registro de la lista?"
        ):
            sql_delete = "DELETE FROM libros WHERE id = ?"
            datos = (id,)
            cursorbdd.execute(sql_delete, datos)
            basedatos.commit()
            messagebox.showinfo(
                title="Info", message="Registro eliminado con exito")

        # refresco el treeview luego de hacer un cambio
        self.cargar_listado(tree, busqueda)
        # deshabilito el uso de los botones
        self.toggle_botones(upd_boton, borrar_boton, True)
        # vacio los campos de entrada
        self.vaciar_entradas(titulo, precio, editorial, genero, autor)

    # Funcion para dar de alta registros

    def funcion_alta(
        self, titulo, precio, editorial, genero, autor, upd_boton, borrar_boton, busqueda, tree
    ):
        basedatos = self.crear_db()
        cursorbdd = basedatos.cursor()

        # Consigo la fecha actual
        horario_actual = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        # Sale de la funcion si algun dato ingresado es incorrecto
        if self.validar_entrada(titulo, precio, editorial, genero, autor):
            return

        # Creo una tupla con los datos necesarios
        datos = (
            titulo.get(),
            precio.get(),
            editorial.get(),
            genero.get(),
            autor.get(),
            horario_actual,
        )

        sql_insert = "INSERT INTO libros (titulo, precio, editorial, genero, autor, fecha_mod) VALUES (?, ?, ?, ?, ?, ?)"
        cursorbdd.execute(sql_insert, datos)
        basedatos.commit()
        messagebox.showinfo(
            title="Info", message="Registro ingresado con exito!")

        self.cargar_listado(tree, busqueda)
        self.vaciar_entradas(titulo, precio, editorial, genero, autor)
        self.toggle_botones(upd_boton, borrar_boton, True)

    # Funcion para modificar registros

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
        basedatos = self.crear_db()
        cursorbdd = basedatos.cursor()

        if id_registro.get() == "":
            messagebox.showinfo(
                title="Info", message="No se ha seleccionado ningun registro en el listado"
            )
            return
        elif self.validar_entrada(titulo, precio, editorial, genero, autor):
            return

        # Consigo la fecha actual
        horario_actual = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        datos = (
            titulo.get(),
            precio.get(),
            editorial.get(),
            genero.get(),
            autor.get(),
            horario_actual,
            id_registro.get(),
        )

        if messagebox.askyesno(
            title="Confirmar eleccion", message="¿Desea modificar el registro de la lista?"
        ):
            # Modifica la informacion del registro que tenga el mismo id del item seleccionado en el listado
            sql_update = (
                "UPDATE libros SET titulo = ?, precio =?, editorial =?, genero = ?, autor = ?, fecha_mod = ? "
                "WHERE id = ?"
            )
            cursorbdd.execute(sql_update, datos)
            basedatos.commit()
            messagebox.showinfo(
                title="Info", message="Registro modificado con exito")

            self.cargar_listado(tree, busqueda)
            self.toggle_botones(upd_boton, borrar_boton, True)
            self.vaciar_entradas(titulo, precio, editorial, genero, autor)

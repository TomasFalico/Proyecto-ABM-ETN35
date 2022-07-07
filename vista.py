import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

#Clase que se encarga del apartado visual del programa
class Panel():

    # Metodo de instacia de la clase Panel
    def __init__(self, ventana, objeto_modelo):

        # Creo una variable de instancia root y la cargo con nuestro objeto tk "ventana" que determina la ventana sobore la que estamos trabajando
        self.root = ventana

        # Configuro el titulo de la ventana sobre la que trabajo
        self.root.title("Proyecto Analisis de Sistema/POO")

        # Este metodo hace que el tamaño de la ventana no se pueda modificar en ninguno de los dos ejes
        self.root.resizable(False, False)

        # Declaro y cargo una variable para almacenar el color de fondo del sistema
        self.color_fondo = tk.StringVar()
        self.color_fondo.set("#b3cde0") 

        # Configuro el color de fondo de la ventana utilizando la variable 
        self.root.configure(bg=self.color_fondo.get())

        # Declaracion de variables a utilizar dentro del sistema
        # Cada una de estas variables va a ser referenciada dentro de un campo de texto/Entry 
        self.var_titulo = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_editorial = tk.StringVar()
        self.var_genero = tk.StringVar()
        self.var_autor = tk.StringVar()
        self.var_id = tk.StringVar()
        self.var_busqueda = tk.StringVar()

        # Declaro los frames donde van a ir ubicado los widgets del sistema
        self.frame_central = tk.Frame(
            self.root, bg=self.color_fondo.get())

        self.frame_entry = tk.Frame(
            self.frame_central, bg=self.color_fondo.get())

        self.frame_entryprecio = tk.Frame(
            self.frame_entry, bg=self.color_fondo.get())

        self.frame_botones = tk.Frame(
            self.frame_central, bg=self.color_fondo.get())

        self.frame_tree = tk.Frame(
            self.frame_central, bg=self.color_fondo.get())

        self.frame_buscar = tk.Frame(
            self.frame_central, bg=self.color_fondo.get())

        # Declaracion de las etiquetas que componen al sector inicial de nuestro programa
        # El primer parametro es la ubicacion en donde se va a pocisionar el elemento
        # El parametro "bg" determina el color de fondo del elemento
        # El parametro "text" determina el texto que va a tener nuestro elemento
        # El parametro "font" indica la fuente de este elemento
        self.sistema_label = tk.Label(
            self.root,
            bg=self.color_fondo.get(),
            text="Sistema ABM Libreria",
            font=tkfont.Font(family="Times", size=23),
        )

        self.titulo_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            text="Titulo",
            font=tkfont.Font(family="Times", size=13),
        )

        self.editorial_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            text="Editorial",
            font=tkfont.Font(family="Times", size=13),
        )

        self.simbolopeso_label = tk.Label(
            self.frame_entryprecio,
            bg=self.color_fondo.get(),
            text="$",
            font=tkfont.Font(family="Times", size=13),
        )

        self.precio_label = tk.Label(
            self.frame_entryprecio,
            bg=self.color_fondo.get(),
            text="Precio",
            font=tkfont.Font(family="Times", size=13),
        )

        self.genero_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            text="Genero",
            font=tkfont.Font(family="Times", size=13),
        )

        self.autor_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            text="Autor",
            font=tkfont.Font(family="Times", size=13),
        )

        # -------- ENTRYS PRINCIPALES ----------


        # Declaracion de las campos de texto que componen al sector inicial de nuestro programa
        # El primer parametro es la ubicacion en donde se va a pocisionar el elemento
        # El parametro "textvariable" determina la variable en donde se va a almacenar la informacion de nuestro Entry
        # El parametro "font" indica la fuente de este elemento
        self.titulo_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_titulo,
            font=tkfont.Font(family="Times", size=13),
        )

        self.precio_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_precio,
            font=tkfont.Font(family="Times", size=13),
        )

        self.editorial_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_editorial,
            font=tkfont.Font(family="Times", size=13),
        )

        self.gen_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_genero,
            font=tkfont.Font(family="Times", size=13),
        )

        self.autor_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_autor,
            font=tkfont.Font(family="Times", size=13),
        )

        # ---- FIN ENTRYS -----


        # Botones del sector principal
        #El primer parametro de cada boton determina su ubicacion 
        #El parametro "state" determina si el boton es clickeable o no


        #Boton Eliminar
        #Llama a la funcion "funcion_baja" que crearemos mas adelante en el modulo "modelo"
        self.borrar_boton = tk.Button(
            self.frame_botones,
            command=lambda: objeto_modelo.funcion_baja(
                self.var_id.get(),
                self.upd_boton,
                self.borrar_boton,
                self.tree,
                self.var_titulo,
                self.var_precio,
                self.var_editorial,
                self.var_genero,
                self.var_autor,
                self.var_busqueda,
            ),
            font=tkfont.Font(family="Times", size=13),
            text="Eliminar",
            state="disabled",
        )

        # Boton guardar
        # Llama a la funcion "funcion_alta" que crearemos mas adelante en el modulo "modelo"
        self.g_boton = tk.Button(
            self.frame_botones,
            command=lambda: objeto_modelo.funcion_alta(
                self.var_titulo,
                self.var_precio,
                self.var_editorial,
                self.var_genero,
                self.var_autor,
                self.upd_boton,
                self.borrar_boton,
                self.var_busqueda,
                self.tree,
            ),
            font=tkfont.Font(family="Times", size=13),
            fg="#000000",
            justify="center",
            text="Guardar",
        )

        # Boton guardar
        # Llama a la funcion "funcion_alta" que crearemos mas adelante en el modulo "modelo"
        self.upd_boton = tk.Button(
            self.frame_botones,
            command=lambda: objeto_modelo.funcion_modificar(
                self.var_id,
                self.var_titulo,
                self.var_precio,
                self.var_editorial,
                self.var_genero,
                self.var_autor,
                self.upd_boton,
                self.borrar_boton,
                self.var_busqueda,
                self.tree,
            ),
            font=tkfont.Font(family="Times", size=13),
            fg="#000000",
            justify="center",
            text="Actualizar",
            state="disabled",
        )

        # ---- POCISIONAMIENTO DE WIDGETS EN LA GRILLA ----

        self.frame_central.grid(row=1, column=0)
        self.frame_entry.grid(row=0, column=0)
        self.frame_botones.grid(row=1, column=0)
        self.frame_tree.grid(row=2, column=0)
        self.frame_buscar.grid(row=3, column=0)

        self.sistema_label.grid(row=0, column=0)

        self.titulo_label.grid(row=1, column=0, padx=15, pady=(20, 5))
        self.titulo_entry.grid(row=1, column=1, padx=15, pady=(20, 5))

        self.frame_entryprecio.grid(row=2, column=0, padx=(30, 0))
        self.precio_label.grid(row=0, column=0, pady=5, padx=(0, 30))
        self.simbolopeso_label.grid(row=0, column=1)

        self.precio_entry.grid(row=2, column=1)

        self.editorial_label.grid(row=3, column=0, pady=5)
        self.editorial_entry.grid(row=3, column=1)

        self.genero_label.grid(row=4, column=0, pady=5)
        self.gen_entry.grid(row=4, column=1)

        self.autor_label.grid(row=5, column=0, pady=5)
        self.autor_entry.grid(row=5, column=1)

        self.g_boton.grid(row=0, column=0, padx=30, pady=10)
        self.upd_boton.grid(row=0, column=1, padx=10, pady=10)
        self.borrar_boton.grid(row=0, column=2, padx=30, pady=10)


        # ---- BOTONES PRINCIPALES -----




        """---------------------------------------
        LISTADO TREE VIEW DE LA INFORMACIÓN
        ---------------------------------------"""

        #Declaro un array con nombres para identificar a cada columna 
        self.columnas = ("titulo", "precio", "editorial",
                         "genero", "autor", "fecha_upd")

        #Creo el listado treeview y le paso como parametros la ubicacion en donde va a estar pocisionado
        #y el listado de las columnas
        self.tree = ttk.Treeview(self.frame_tree, columns=self.columnas)

        #Declaro los heading o encabezados de la lista y le asigno un nombre
        self.tree.heading("#0", text="ID")
        #Modifico la configuracion de la columna correspondiente a cada encabezado  
        #-minwidth determina el ancho minimo que puede tener la columna  
        #-width determina el ancho predeterminado de la columna
        #-anchor determina como ubico el texto dentro de la columna, en este caso el texto estaria centrado
        self.tree.column("#0", minwidth=0, width=40, anchor="center")

        self.tree.heading("titulo", text="Titulo")
        self.tree.column("titulo", minwidth=0, width=150, anchor="center")

        self.tree.heading("precio", text="Precio")
        self.tree.column("precio", minwidth=0, width=50, anchor="center")

        self.tree.heading("editorial", text="Editorial")
        self.tree.column("editorial", minwidth=0, width=100, anchor="center")

        self.tree.heading("genero", text="Genero")
        self.tree.column("genero", minwidth=0, width=100, anchor="center")

        self.tree.heading("autor", text="Autor")
        self.tree.column("autor", minwidth=0, width=100, anchor="center")

        self.tree.heading("fecha_upd", text="Ult. Actualizacion")
        self.tree.column("fecha_upd", minwidth=0, width=120, anchor="center")

        #Pocisiono el listado tree dentro de la grilla 
        self.tree.grid(row=0, column=0, padx=30)

        # Evento que se acciona cuando hago click en un item del treeview
        self.tree.bind(
            "<<TreeviewSelect>>",
            lambda event: objeto_modelo.select_item(
                self.tree.item(self.tree.focus()),
                self.var_id,
                self.var_titulo,
                self.var_precio,
                self.var_editorial,
                self.var_genero,
                self.var_autor,
                self.borrar_boton,
                self.upd_boton,
            ),
        )

        # Llamo a funcion para popular la lista 
        # Esta funcion solo se llama una vez 
        objeto_modelo.cargar_listado(self.tree, self.var_busqueda)

        """------------------------------------------
        FIN DE TREE VIEW
        ------------------------------------------"""


        # ---- BUSQUEDA POR TITULO ----

        #Label "Buscar por titulo" 
        self.buscar_label = tk.Label(
            self.frame_buscar,
            bg=self.color_fondo.get(),
            text="Buscar por titulo",
            font=tkfont.Font(family="Times", size=13),
        )

        #Campo de texto para ingresar titulo utilizado en el filtro
        self.buscar_entry = tk.Entry(
            self.frame_buscar,
            textvariable=self.var_busqueda,
            font=tkfont.Font(family="Times", size=13),
        )

        #Boton de busqueda: muestra solo los registros que contengan el texto del entry "buscar_entry" dentro del listado de registros
        self.busq_boton = tk.Button(
            self.frame_buscar,
            command=lambda: objeto_modelo.cargar_listado(
                self.tree,
                self.var_busqueda,
            ),
            font=tkfont.Font(family="Times", size=13),
            text="Buscar",
        )

        #Boton borrar filtro: vacia campos de texto y reinicia el listado de registros
        self.b_filtro_boton = tk.Button(
            self.frame_buscar,
            command=lambda: objeto_modelo.cargar_listado(
                self.tree,
                self.var_busqueda,
                True,
            ),
            font=tkfont.Font(family="Times", size=13),
            text="Borrar filtro",
        )

        #Pocisionamiento de la etiquetas, campos de entrada y los botones del sector busqueda
        self.buscar_label.grid(row=8, column=0, padx=10, pady=10)
        self.buscar_entry.grid(row=8, column=1, pady=10)

        self.busq_boton.grid(row=8, column=2, padx=20, pady=10)
        self.b_filtro_boton.grid(row=8, column=3, padx=10, pady=10)

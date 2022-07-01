import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk


class Panel():
    def __init__(self, ventana, objeto_modelo):

        self.root = ventana

        # Determinando el titulo del programa
        self.root.title("Entrega Final ABM")

        self.root.resizable(False, False)

        # Determinando el color de fondo del programa
        self.color_fondo = tk.StringVar()
        self.color_fondo.set("#b3cde0")  # F0F2FF
        self.root.configure(bg=self.color_fondo.get())

        # Declaracion de variables a utilizar dentro del sistema
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

        # Nombre del sistema
        self.sistema_label = tk.Label(
            self.root,
            bg=self.color_fondo.get(),
            text="Sistema de stock - LIBRERIA",
            font=tkfont.Font(family="Times", size=23),
            fg="#333333",
            justify="right",
        )

        self.titulo_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            text="Titulo",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
            justify="right",
        )

        self.editorial_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            anchor="e",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
            justify="right",
            text="Editorial",
        )

        self.simbolopeso_label = tk.Label(
            self.frame_entryprecio,
            bg=self.color_fondo.get(),
            text="$",
            anchor="e",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
            justify="right",
        )

        self.precio_label = tk.Label(
            self.frame_entryprecio,
            bg=self.color_fondo.get(),
            text="Precio",
            anchor="e",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
            justify="right",
        )

        self.genero_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            text="Genero",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
            justify="right",
        )

        self.autor_label = tk.Label(
            self.frame_entry,
            bg=self.color_fondo.get(),
            text="Autor",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
            justify="right",
        )

        # -------- ENTRYS PRINCIPALES ----------

        self.titulo_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_titulo,
            font=tkfont.Font(family="Times", size=13),
            borderwidth="1px",
            fg="#333333",
        )

        self.precio_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_precio,
            borderwidth="1px",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
        )

        self.editorial_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_editorial,
            borderwidth="1px",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
        )

        self.gen_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_genero,
            borderwidth="1px",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
        )

        self.autor_entry = tk.Entry(
            self.frame_entry,
            textvariable=self.var_autor,
            borderwidth="1px",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
        )

        # ---- FIN ENTRYS -----

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

        """---------------------------------------
        LISTADO TREE VIEW DE LA INFORMACIÓN
        ---------------------------------------"""

        self.columnas = ("titulo", "precio", "editorial",
                         "genero", "autor", "fecha_upd")

        self.tree = ttk.Treeview(self.frame_tree, columns=self.columnas)

        self.tree.heading("#0", text="ID")
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
        self.tree.grid(row=0, column=0, padx=30)

        # funcion que se triggerea cuando hago click en un item del treeview
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
        objeto_modelo.cargar_listado(self.tree, self.var_busqueda)

        """------------------------------------------
        FIN DE TREE VIEW
        ------------------------------------------"""

        # ---- BOTONES PRINCIPALES -----

        # Boton Elimnar
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
            fg="#000000",
            justify="center",
            text="Eliminar",
            state="disabled",
        )

        # Boton guardar
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

        # Boton Actualizar
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

        # ---- BUSQUEDA POR TITULO ----

        self.buscar_label = tk.Label(
            self.frame_buscar,
            bg=self.color_fondo.get(),
            text="Buscar por titulo",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
            justify="right",
        )

        self.buscar_entry = tk.Entry(
            self.frame_buscar,
            textvariable=self.var_busqueda,
            borderwidth="1px",
            font=tkfont.Font(family="Times", size=13),
            fg="#333333",
        )

        self.busq_boton = tk.Button(
            self.frame_buscar,
            command=lambda: objeto_modelo.cargar_listado(
                self.tree,
                self.var_busqueda,
            ),
            font=tkfont.Font(family="Times", size=13),
            fg="#000000",
            justify="center",
            text="Buscar",
        )

        self.b_filtro_boton = tk.Button(
            self.frame_buscar,
            command=lambda: objeto_modelo.cargar_listado(
                self.tree,
                self.var_busqueda,
                True,
            ),
            font=tkfont.Font(family="Times", size=13),
            fg="#000000",
            justify="center",
            text="Borrar filtro",
        )

        self.g_boton.grid(row=0, column=0, padx=30, pady=10)
        self.upd_boton.grid(row=0, column=1, padx=10, pady=10)
        self.borrar_boton.grid(row=0, column=2, padx=30, pady=10)

        self.buscar_label.grid(row=8, column=0, padx=10, pady=10)
        self.buscar_entry.grid(row=8, column=1, pady=10)

        self.busq_boton.grid(row=8, column=2, padx=20, pady=10)
        self.b_filtro_boton.grid(row=8, column=3, padx=10, pady=10)

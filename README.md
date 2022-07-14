> **<u>Documentación y guía paso a paso de</u>**

**<u>Sistema ABM Librería</u>**

Tabla de contenido

<table>
<thead>
<tr class="header">
<th>1.</th>
<th><blockquote>
<p>Introduccion</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.</td>
<td><blockquote>
<p>1.1.</p>
</blockquote></td>
<td><blockquote>
<p>Alcance</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>1.2.</p>
</blockquote></td>
<td><blockquote>
<p>Comportamiento</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>1.3.</p>
</blockquote></td>
<td><blockquote>
<p>Maqueta (Previsualización)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>2. Reproducción paso a paso del sistema</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2.1.</p>
</blockquote></td>
<td><blockquote>
<p>Introducción de herramientas a utilizar</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2.2.</p>
</blockquote></td>
<td><blockquote>
<p>Configuración del área de trabajo</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2.3.</p>
</blockquote></td>
<td><blockquote>
<p>Creación de la estructura MVC</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2.4.</p>
</blockquote></td>
<td><blockquote>
<p>Desarrollo de apartado visual (vista.py)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>2.4.1.</td>
<td><blockquote>
<p>Sector Principal</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>2.4.2.</td>
<td><blockquote>
<p>Listado de registros</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>2.4.3.</td>
<td><blockquote>
<p>Sector de búsqueda/filtro</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2.5.</p>
</blockquote></td>
<td><blockquote>
<p>Lógica del sistema (modelo.py)</p>
</blockquote></td>
</tr>
</tbody>
</table>

***1.* Introduccion**

1.1 Alcance

> La finalidad de la aplicación a desarrollar es la de mantener un
> control del catálogo de los libros e historietas presentes dentro de
> una librería.
>
> Para esto se pensó una aplicación en donde se ingresen los siguientes
> datos:  
> ● Titulo: Titulo comercial del libro  
> ● Precio: Valor en pesos del producto  
> ● Editorial: La empresa que produjo ese libro  
> ● Genero: Genero literario del libro  
> ● Autor: Escritor del libro

1.2 Comportamiento

> La aplicación se compone de seis campos de ingreso de texto junto a
> seis etiquetas que se encargan de describir cada uno de estos campos,
> a su vez, la aplicación cuenta con un listado en
>
> donde se exhiben todos los registros guardados y una serie de cinco
> botones que se comportan según se describe a  
> continuación:  
> ● Guardar: Almacena los datos ingresados en los campos de entrada
> dentro de la Base de Datos.
>
> ● Actualizar: Edita y guarda un registro seleccionado desde la lista
> de libros.
>
> ● Eliminar: Elimina desde la Base de Datos al registro seleccionado en
> el listado.
>
> ● Buscar: Muestra un listado de registros que tengan un títuloparecido
> o igual al ingresado dentro del campo de texto“Buscar por título”.
>
> ● Borrar filtro: Muestra el listado completo de registros y limpia el
> campo de texto “Buscar por título”
>
> 1.3 Maqueta (Previsualización)

<img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image1.png" style="width:7.34444in;height:4.25972in" />

***2.* Reproducción paso a paso**

**del Sistema**

> 2.1 Introducción de herramientas a utilizar
>
> Esta es una breve introducción a las herramientas que utilizo a lo
> largo del desarrollo de este sistema:
>
> ● Visual Studio Code: editor de texto en donde voy a  
> programar el sistema utilizando el lenguaje de programación Python.
>
> ● Dentro de Python utilizo las siguientes librerías:
>
> ● Tkinter: interfaz gráfica por la cual el usuario se va a
>
> poder comunicar con el sistema
>
> ● SQLite3: motor de bases de datos SQL ligero donde
>
> almacenaremos los datos ingresados
>
> ● re: módulo que proporciona operaciones de  
> coincidencia de expresiones regulares (utilizado en las validaciones
> de ingreso de datos)  
> ● Datetime: módulo que proporciona clases para  
> manipular fechas y horas
>
> 2.2 Configuración del área de trabajo
>
> El primer paso al momento de configurar el área de trabajos es el de
> descargar Visual Studio Code, para eso hay que dirigirse a la pagina
> https://code.visualstudio.com/download en donde hay que hacer click en
> el enlace de descarga correspondiente a nuestro sistema operativo:
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image2.png" style="width:6.8125in;height:3.96806in" />
>
> El siguiente paso es el de descargar Python por lo que me voy a
> dirigir ir al siguiente enlace: y hacer click en el botón de descarga
> de la versión más reciente
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image3.png" style="width:6.97917in;height:4.88472in" />
>
> Mientras hago la instalación de Python es muy importante que se tilde
> la opción de “Add Python 3.X to PATH” como muestra la imagen a
> continuación. Si no se realiza este paso, es muy  
> probable que tenga problemas de compatibilidad a futuro.
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image4.png" style="width:7.10417in;height:4.40556in" />
>
> El último paso a la hora de crear el espacio de trabajo es el de poder
> utilizar Python dentro de Visual Studio Code. Para eso voy a abrir VS
> Code y me voy a dirigir a la sección de extensiones
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image5.png" style="width:8.15694in;height:2.85417in" />
>
> Y dentro de esta sección voy a utilizar el buscador indicado a
> continuación para encontrar e instalar las extensiones que dejo más
> adelante:
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image6.png" style="width:5.70833in;height:4.63611in" />
>
> \- Code Runner
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image7.png" style="width:7.10417in;height:1.0625in" />
>
> \- Python
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image8.png" style="width:7.15556in;height:1.03056in" />
>
> 2.3 Creación de la estructura MVC
>
> Luego de seguir los anteriores pasos ya debería contar tanto con VS
> Code como con Python instalados y funcionando en mi computadora así
> que el siguiente paso es el diseñar la base o arquitectura del
> programa.
>
> En este caso la arquitectura del sistema va a estar basadaen el patrón
> MVC (Modelo-Vista-Controlador) en el cual cuento con un archivo
> “Vista” que es por donde el usuario se va a comunicar con el sistema,
> un archivo “Modelo” que es el que contiene gran parte de la lógica de
> nuestro sistema y un archivo“Controlador” que se encarga de comunicar
> a la Vista con el Modelo.
>
> Lo primero que hago dentro del Visual Studio Code es crear tres
> archivos que compondrán al modelo MVC y los titulo de la siguiente
> manera:
>
> \- “main.py” como nuestro Controlador  
> - “modelo.py” como nuestro Modelo  
> - “Vista.py” como nuestra Vista
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image9.png" style="width:7.03056in;height:3.61528in" />
>
> 2.4 Desarrollo del apartado visual (vista.py)
>
> Voy a separar la parte visual del programa en tres partes para una
> mejor comprensión del código. Esta división se encuentra graficada a
> continuación:
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image10.png" style="width:6.95833in;height:5.70833in" />

**(1) Sector principal**

**(2) Listado de Registros**

**(3) Sector de búsqueda/filtro**

2.4.1 Sector Principal

> Abro el archivo “vista.py” en donde voy a importar tres librerías que
> traen varias funcionalidades para el desarrollo del apartado visual
> del sistema. Las librerías a importar son las siguientes:
>
> ● Tkinter: Es el paquete más utilizado para crear interfacesgráficas
> en Python, es la herramienta que nos permite crear las etiquetas,
> botones, campos de texto y hasta la misma ventana donde el usuario
> interactúa con el sistema.
>
> ● Tkfont: Utilizada para modificar la fuente del texto dentro de los
> elementos de Tkinter.
>
> ● Tkinter.Ttk: extensión del paquete Tkinter que me permite crear el
> listado registros
>
> <img src="vertopal_8ea7a0085cc04c228d7bfd9db39ede49/media/image11.png" style="width:6.57361in;height:2.80139in" />
>
> Luego voy a crear una clase con nombre “Panel” que tendrá un método de
> instancia (método que se llama al momento de instanciar a la clase)
> que recibe los siguientes parámetros:
>
> ● self: Hace referencia a la instancia del objeto
>
> ● ventana: Hace referencia a un objeto “tk” que va a servir como
>
> la ventana donde se posicionan los elementos visuales
>
> ● objeto\_modelo: Hace referencia a un objeto de la clase “Abmc”que
> voy a crear más adelante. Me permite interactuar con la parte lógica
> del programa

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td>#<em>Clase que se encarga del apartado visual del programa</em></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>class Panel():</td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Metodo de instacia de la clase Panel</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>def __init__(self, ventana, objeto_modelo):</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Y ahora voya realizar las configuraciones básicas de la ventana y las
> declaraciones de las variables que se van a utilizar dentro de la
> misma:

<table>
<thead>
<tr class="header">
<th>#<em>Clase que se encarga del apartado visual del programa</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>class Panel():</td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Metodo de instacia de la clase Panel</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>def __init__(self, ventana, objeto_modelo):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Creo una variable de instancia root y la cargo con nuestro objeto tk</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>"ventana" que determina la ventana sobore la que estamos trabajando</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.root = ventana</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Configuro el titulo de la ventana sobre la que trabajo</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.root.title("Proyecto Analisis de Sistema/POO")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Este metodo hace que el tamaño de la ventana no se pueda modificar en</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>ninguno de los dos ejes</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.root.resizable(False, False)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Declaro y cargo una variable para almacenar el color de fondo del</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>sistema</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.color_fondo = tk.StringVar()</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.color_fondo.set("#b3cde0")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Configuro el color de fondo de la ventana utilizando la variable</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.root.configure(bg=self.color_fondo.get())</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Declaracion de variables a utilizar dentro del sistema</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Cada una de estas variables va a ser referenciada dentro de un campo de</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>texto/Entry</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_titulo = tk.StringVar()</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_precio = tk.StringVar()</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_editorial = tk.StringVar()</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_genero = tk.StringVar()</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_autor = tk.StringVar()</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_id = tk.StringVar()</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_busqueda = tk.StringVar()</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Luego declaro los “tk.Frame”. Este objeto representa un contenedor con
> un área rectangular en donde se pueden agrupar y organizar los
> elementos dentro de la ventana del sistema

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Declaro los frames donde van a ir ubicado los widgets del sistema</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.frame_central = tk.Frame(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.root, bg=self.color_fondo.get())</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_entry = tk.Frame(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_central, bg=self.color_fondo.get())</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_entryprecio = tk.Frame(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry, bg=self.color_fondo.get())</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_botones = tk.Frame(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_central, bg=self.color_fondo.get())</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_tree = tk.Frame(</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.frame_central, bg=self.color_fondo.get())</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.frame_buscar = tk.Frame(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_central, bg=self.color_fondo.get())</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Ahora paso a declarar las Label o Etiquetas principales que sirven
> como guía para el usuario a la hora de poder ingresar información.

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Declaración de las etiquetas que componen al sector inicial de nuestro</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><em>programa</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>El primer parametro es la ubicación en donde se va a posicionar el</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>elemento</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>El parametro "bg" determina el color de fondo del elemento</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>El parametro "text" determina el texto que va a tener nuestro elemento</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>El parametro "font" indica la fuente de este elemento</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.sistema_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.root,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Sistema ABM Libreria",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=23),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.titulo_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Titulo",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.editorial_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Editorial",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.simbolopeso_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entryprecio,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>text="$",</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.precio_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entryprecio,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Precio",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.genero_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Genero",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.autor_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Autor",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Creo los campos de entrada que le permiten ingresar datos en el
> sistema al usuario y van a estar ubicados al lado de sus  
> etiquetas/labels correspondientes

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Declaración de las campos de texto que componen al sector inicial de</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><em>nuestro programa</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>El primer parametro es la ubicacion en donde se va a pocisionar el</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>elemento</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>El parametro "textvariable" determina la variable en donde se va a</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>almacenar la informacion de nuestro Entry</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>El parametro "font" indica la fuente de este elemento</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.titulo_entry = tk.Entry(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>textvariable=self.var_titulo,</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.precio_entry = tk.Entry(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>textvariable=self.var_precio,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.editorial_entry = tk.Entry(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>textvariable=self.var_editorial,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.gen_entry = tk.Entry(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>textvariable=self.var_genero,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.autor_entry = tk.Entry(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_entry,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>textvariable=self.var_autor,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Creo los botones principales del programa que son
> “Guardar”,“Actualizar” y “Eliminar”. Cada uno de estos botones va a
> llamar a una función que voy a declarar más adelante en el módulo
> “Modelo”donde se encuentra la lógica del programa

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Botones del sector principal</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#<em>El primer parametro de cada boton determina su ubicacion</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#<em>El parametro "state" determina si el boton es clickeable o no</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#<em>Boton Eliminar</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Llama a la funcion "funcion_baja" que crearemos mas adelante en el</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>modulo "modelo"</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.borrar_boton = tk.Button(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_botones,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>command=lambda: objeto_modelo.funcion_baja(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_id.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.upd_boton,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.borrar_boton,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_titulo,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_precio,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_editorial,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_genero,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_autor,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_busqueda,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>text="Eliminar",</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>state="disabled",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Boton guardar</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Llama a la funcion "funcion_alta" que crearemos mas adelante en el</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>modulo "modelo"</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.g_boton = tk.Button(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_botones,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>command=lambda: objeto_modelo.funcion_alta(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_titulo,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_precio,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_editorial,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_genero,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_autor,</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.upd_boton,</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.borrar_boton,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_busqueda,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Guardar",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Boton guardar</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Llama a la funcion "funcion_alta" que crearemos mas adelante en el</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>modulo "modelo"</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.upd_boton = tk.Button(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_botones,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>command=lambda: objeto_modelo.funcion_modificar(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_id,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_titulo,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_precio,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_editorial,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_genero,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_autor,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.upd_boton,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.borrar_boton,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_busqueda,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Actualizar",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>state="disabled",</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Y el último paso para dentro del sector en donde se hace el ingreso de
> datos es el de ubicar los elementos que cree previamente. Para eso voy
> a utilizar el método “grid” que me permite ubicar cada elemento dentro
> de una grilla imaginaria dentro de la ventana.
>
> Los parámetros “row” y “column” determinan en qué fila ycolumna se va
> a posicionar cada elemento de la grilla, mientras que los parámetros
> “padx” y “pady” permiten mover al elemento dentro del eje X e Y para
> un posicionamiento más preciso.

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.frame_central.grid(row=1, column=0)</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.frame_entry.grid(row=0, column=0)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_botones.grid(row=1, column=0)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_tree.grid(row=2, column=0)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_buscar.grid(row=3, column=0)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.sistema_label.grid(row=0, column=0)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.titulo_label.grid(row=1, column=0, padx=15, pady=(20, 5))</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.titulo_entry.grid(row=1, column=1, padx=15, pady=(20, 5))</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_entryprecio.grid(row=2, column=0, padx=(30, 0))</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.precio_label.grid(row=0, column=0, pady=5, padx=(0, 30))</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.simbolopeso_label.grid(row=0, column=1)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.precio_entry.grid(row=2, column=1)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.editorial_label.grid(row=3, column=0, pady=5)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.editorial_entry.grid(row=3, column=1)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.genero_label.grid(row=4, column=0, pady=5)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.gen_entry.grid(row=4, column=1)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.autor_label.grid(row=5, column=0, pady=5)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.autor_entry.grid(row=5, column=1)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.g_boton.grid(row=0, column=0, padx=30, pady=10)</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.upd_boton.grid(row=0, column=1, padx=10, pady=10)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.borrar_boton.grid(row=0, column=2, padx=30, pady=10)</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.4.2 Listado de registros

> Para la creación del listado voy a usar el objeto
> “Treeview”perteneciente a la librería “ttk”.
>
> Un dato a aclarar es que los treeview vienen con una columnapor
> default (normalmente llamada “ghost column” o “columna fantasma”) y
> voy a utilizar esa columna para almacenar el “ID” de cada elemento,
> por eso no se declara la columna “ID” dentro del array de columnas
> “self.columnas”.

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#<em>Declaro un array con nombres para identificar a cada columna</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.columnas = ("titulo", "precio", "editorial",</p>
</blockquote></td>
</tr>
<tr class="even">
<td>"genero", "autor", "fecha_upd")</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Creo el listado treeview y le paso como parametros la ubicacion</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>en donde va a estar pocisionado</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>y el listado de las columnas</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree = ttk.Treeview(self.frame_tree, columns=self.columnas)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Declaro los heading o encabezados de la lista y le asigno un</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>nombre</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree.heading("#0", text="ID")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Modifico la configuracion de la columna correspondiente a cada</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>encabezado</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>-minwidth determina el ancho minimo que puede tener la columna</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#<em>-width determina el ancho predeterminado de la columna</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>-anchor determina como ubico el texto dentro de la columna, en</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>este caso el texto estaria centrado</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.tree.column("#0", minwidth=0, width=40, anchor="center")</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.tree.heading("titulo", text="Titulo")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.column("titulo", minwidth=0, width=150, anchor="center")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree.heading("precio", text="Precio")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.column("precio", minwidth=0, width=50, anchor="center")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree.heading("editorial", text="Editorial")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.column("editorial", minwidth=0, width=100,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>anchor="center")</td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.heading("genero", text="Genero")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree.column("genero", minwidth=0, width=100, anchor="center")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.heading("autor", text="Autor")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree.column("autor", minwidth=0, width=100, anchor="center")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.heading("fecha_upd", text="Ult. Actualizacion")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree.column("fecha_upd", minwidth=0, width=120,</p>
</blockquote></td>
</tr>
<tr class="even">
<td>anchor="center")</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Pocisiono el listado tree dentro de la grilla</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.grid(row=0, column=0, padx=30)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Luego creo un evento utilizando el método “bind” que me permite
> ejecutar una función cada vez que el usuario hace click en el listado

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Evento que se acciona cuando hago click en un item del treeview</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.tree.bind(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>"&lt;&lt;TreeviewSelect&gt;&gt;",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>lambda event: objeto_modelo.select_item(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree.item(self.tree.focus()),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_id,</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td>)</td>
</tr>
</tbody>
</table></th>
<th>),</th>
<th><blockquote>
<p>self.var_titulo,</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>self.var_precio,</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>self.var_editorial,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>self.var_genero,</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>self.var_autor,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>self.borrar_boton,</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>self.upd_boton,</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Y por último llamo a un método que voy a crear más adelante y que me
> permite mostrar los registros ingresados dentro del listado Treeview.

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Llamo a funcion para popular la lista</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Esta funcion solo se llama una vez</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td>objeto_modelo.cargar_listado(self.tree, self.var_busqueda)</td>
</tr>
</tbody>
</table>

> 2.4.3 Sector de búsqueda/filtro
>
> El último sector a desarrollar en el módulo de vista es el de
> búsqueda/filtro. Este sector está compuesto por:
>
> ● Etiqueta/Label: identificador del campo de entrada .
>
> ● Campo de texto: espacio en donde el usuario puede ingresar el título
> del producto a buscar.
>
> ● Botón “Buscar”: ejecuta un función “cargar\_listado” del
> módulo“modelo” que modifica la información del listado treeview
> dependiendo de los datos ingresados en el campo de texto.
>
> ● Botón “Borrar Filtro”: ejecuta la misma función que el botón
> “Buscar” pero aplicando una lógica distinta que permite vaciar
>
> los campos de entrada y mostrar el listado de registros completos sin
> aplicar filtros.
>
> Asi deberia verse el código que compone al “sector búsqueda” del
> sistema:

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#<em>Label "Buscar por titulo"</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.buscar_label = tk.Label(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_buscar,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>bg=self.color_fondo.get(),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Buscar por titulo",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>#<em>Campo de texto para ingresar titulo utilizado en el filtro</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.buscar_entry = tk.Entry(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.frame_buscar,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>textvariable=self.var_busqueda,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Boton de busqueda: muestra solo los registros que contengan el</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>texto del entry "buscar_entry" dentro del listado de registros</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.busq_boton = tk.Button(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.frame_buscar,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>command=lambda: objeto_modelo.cargar_listado(</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.tree,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.var_busqueda,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Buscar",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Boton borrar filtro: vacia campos de texto y reinicia el listado</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>de registros</em></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.b_filtro_boton = tk.Button(</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.frame_buscar,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>command=lambda: objeto_modelo.cargar_listado(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.tree,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.var_busqueda,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>True,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>),</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>font=tkfont.Font(family="Times", size=13),</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>text="Borrar filtro",</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Pocisionamiento de la etiquetas, campos de entrada y los botones</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>del sector busqueda</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.buscar_label.grid(row=8, column=0, padx=10, pady=10)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.buscar_entry.grid(row=8, column=1, pady=10)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.busq_boton.grid(row=8, column=2, padx=20, pady=10)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>self.b_filtro_boton.grid(row=8, column=3, padx=10, pady=10)</td>
</tr>
</tbody>
</table>

> Con esto ya doy por finalizado el desarrollo del apartado visual del
> programa. Ahora paso a crear la lógica del sistema que me va a
> permitir procesar la información que ingrese el usuario desde el
> apartado visual.
>
> 2.5 Lógica del sistema (modelo.py)
>
> El primer paso a la hora de desarrollar la lógica del programa es el
> de abrir el archivo “modelo.py” previamente creado en el inicio de
>
> esta guía. Dentro de este módulo voy a estar declarando las siguientes
> librerías:

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td>#<em>Base de datos que utilizo para almancenar registros</em></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>import</em> sqlite3</td>
</tr>
<tr class="even">
<td>#<em>Libreria que permite utilizar expresiones regulares para validar</em></td>
</tr>
<tr class="odd">
<td><em>informacion</em></td>
</tr>
<tr class="even">
<td><em>import</em> re</td>
</tr>
<tr class="odd">
<td>#<em>Libreria que utilizo para conseguir la fecha y hora exacta al momento de</em></td>
</tr>
<tr class="even">
<td><em>registrar cambios en la base de datos</em></td>
</tr>
<tr class="odd">
<td><em>from</em> datetime <em>import</em> datetime</td>
</tr>
<tr class="even">
<td>#<em>Libreria utilizada para mostrar popups o mensajes de alerta a la hora de</em></td>
</tr>
<tr class="odd">
<td><em>realizar algun cambio en el registro de datos</em></td>
</tr>
<tr class="even">
<td><em>from</em> tkinter <em>import</em> messagebox</td>
</tr>
</tbody>
</table>

> Luego creo la clase “Abmc” y dentro de su método de instancia (“def
> \_\_init\_\_ (self,)”) voy a crear tres variables “regex” que me van a
> servir a la hora de realizar validaciones. Para tener una idea del
> funcionamiento de las “regex” o “expresiones regulares” dejo este link
> a continuacion:

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td>#<em>Clase ABMC: maneja la logica relacionada a las funciones de Alta, Baja,</em></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>MOdificacion y Consulta del sistema</em></td>
</tr>
<tr class="even">
<td>class Abmc():</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Metodo de instancia</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>def __init__(self,):</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Matchea con lineas de texto que solo tengan numeros entre 0 y 9</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>self.regex_numeros = "^[0-9]+$"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Matchea con lineas de texto que solo tengan caracteres y con una</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>longitud entre 1 y 60 caracteres</em></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>self.regex_palabra = r"^[.,a-zA-Z\s]{1,60}$"</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Matchea con lineas de texto que tengan caracteres o numeros y</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>con una longitud entre 1 y 60 caracteres</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.regex_vacio = r"^[,.a-zA-Z0-9_\s]{1,60}$"</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **Todas las funciones que se creen a continuación van**

**a estar dentro de la clase “Abmc”**

> “crear\_db”: permite conectarse/crear a la base de datos SQLite3 y
> crear la tabla “libros” dentro de esta base:

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#<em>Funcion que devuelve una conexion a la base de datos</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>def <em>crear_db</em>(self,):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>El metodo "connect" de sqlite3 me permite conectarme a una base</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>de datos con el nombre que es enviado como parametroo</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>En el caso de que haya una base de datos con ese nombre en el</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>mismo directorio que el archivo, este metodo nos conecta a esa base de</em></td>
</tr>
<tr class="even">
<td><em>datos</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>En el caso de que NO haya una base de datos con ese nombre, este</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>metodo crea la base de datos y luegos nos conecta</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>basedatos = sqlite3.connect("libreria.db")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Devuelvo la referencia a la base de datos</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>return</em> basedatos</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Funcion para crear la tabla de registros de libros en nuestra base de</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>datos</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Toma como parametro a la base de datos que estamos utilizando</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>def <em>crear_tabla_libro</em>(self, basedatos):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Consigo la referencia a la base de datos utilizando la funcion de</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>conexion</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>basedatos = self.crear_db()</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>#<em>Creo un objeto cursor que me permite ejecutar sentencias SQL en</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>la base de datos</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>cursorbdd = basedatos.cursor()</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Defino una sentencia SQL que me permite crear la tabla "libros"</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>si es que no fue creada con anterioridad</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sql = (</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>"CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>AUTOINCREMENT,"</td>
</tr>
<tr class="even">
<td><blockquote>
<p>" titulo TEXT,"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>" precio INTEGER,"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>" editorial TEXT,"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>" genero TEXT,"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>" autor TEXT,"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>" fecha_mod DATETIME)"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Ejecuta la sentencia utilizando el cursor</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>cursorbdd.execute(sql)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>Utilizo el metodo commit para guardar los cambios realizados en</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>la base de datos</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>basedatos.commit()</p>
</blockquote></td>
</tr>
</tbody>
</table>

> “toggle\_botones”: me permite habilitar o deshabilitar los botones de
> actualizar y eliminar según sea necesario. La idea de esta función es
> hacer que los botones previamente mencionados sean clickeables solo si
> el usuario hizo click en un elemento de la lista, en caso  
> contrario, solo el botón de “Agregar” debería poder ser seleccionado.

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Funcion para determinar si los botones de actualizacion y borrado se</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>encuentran activos</em></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Esta funcion toma como parametros a los objetos boton de</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>actualizacion y boton de borrado; tambien toma un parametro booleano</em></td>
</tr>
<tr class="even">
<td><em>deshabilitar</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>def <em>toggle_botones</em>(self, upd_boton, borrar_boton, deshabilitar):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>Si dehabilitar es "True", deshabilitamos los botones de</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>actualizacion y borrado</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>if</em> deshabilitar:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>"state" es un atributo de los botones de Tkinter que</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>determina si el boton es clickeable o no</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>upd_boton["state"] = "disabled"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>borrar_boton["state"] = "disabled"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>En el caso de que deshabilitar sea "False", hago que los botones</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>sean clickeables</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>else</em>:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>upd_boton["state"] = "normal"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>borrar_boton["state"] = "normal"</p>
</blockquote></td>
</tr>
</tbody>
</table>

> “vaciar\_entradas”: resetea los campos de entrada de texto

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td># <em>Funcion para vaciar todos los campos de entrada luego de realizar</em></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>una alta, baja o modificacion</em></td>
</tr>
<tr class="even">
<td># <em>Toma como parametro a los entry del sector principal del programa</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>def <em>vaciar_entradas</em>(self, titulo, precio, editorial, genero, autor):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>El metodo "set("") nos permite vaciar cada uno de los campos de</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>entrada</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>titulo.set("")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>precio.set("")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>editorial.set("")</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>genero.set("")</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>autor.set("")</p>
</blockquote></td>
</tr>
</tbody>
</table>

> “select\_item”: permite recibir los datos de los registros
> seleccionados en el listado y a su vez llena los campos de entrada con
> la  
> información recibida

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td># <em>Funcion para rellena los entry con datos del item seleccionado en</em></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>treeview</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Toma como parametro al objeto listado, los campos de entrada y los</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>botones de borrar y actualizar</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>def <em>select_item</em>(</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>self, lista, id, titulo, precio, editorial, genero, autor,</td>
</tr>
<tr class="even">
<td>borrar_boton, upd_boton</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>try</em>:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Rellenamos los campos de entrada con los valores del item</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>seleccionado dentro de la lista</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>id.set(lista["text"])</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>titulo.set(lista["values"][0])</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>precio.set(lista["values"][1].lstrip("$"))</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>editorial.set(lista["values"][2])</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>genero.set(lista["values"][3])</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>autor.set(lista["values"][4])</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>except</em> IndexError:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>En el caso de que haya un error a la hora de conseguir los</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>valores del item, se sale de la funcion</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>return</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Habilito los botones de actualizar y eliminar ya que estoy</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>seleccionando un registro</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>self.toggle_botones(upd_boton, borrar_boton, False)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> “Validar\_entrada”: valida los datos ingresados en los campos de
> entrada a la hora de añadir, eliminar o actualizar un registro de la
> base de datos. La validación se hace utilizando las expresiones
> regulares declaradas al principio de nuestra clase “Abmc”

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p># <em>Funcion para validar los campos de entrada de dato teniendo en</em></p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>cuenta diferentes criterios</em></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td># <em>Toma como parametro a los campos de entrada del sector principal</em></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>def <em>validar_entrada</em>(self, titulo, precio, editorial, genero, autor):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Cargo los patrones de regex que voy a usar para validar cada</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>campo</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>patron_num = re.compile(self.regex_numeros)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>patron_text = re.compile(self.regex_palabra)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>patron_vacio = re.compile(self.regex_vacio)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p># <em>Variable en la que concateno cada campo que tenga un error</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>errores = ""</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>el metodo fullmatch de la libreria regex permite comparar un</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>string con una expresion regular</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>En este caso estoy verificando si mi string no cumple con las</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>condiciones de la expresion regular</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>if</em> not re.fullmatch(patron_vacio, titulo.get()):</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>En el caso de que no cumpla con esa condicion, agregamos el</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>nombre del campo de entrada a nuestro</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#<em>string de errores</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>errores += "\n-Titulo"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>if</em> not re.fullmatch(patron_num, precio.get()):</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>errores += "\n-Precio"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>if</em> not re.fullmatch(patron_text, editorial.get()):</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>errores += "\n-Editorial"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>if</em> not re.fullmatch(patron_text, genero.get()):</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>errores += "\n-Genero"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>if</em> not re.fullmatch(patron_text, autor.get()):</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>errores += "\n-Autor"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p># <em>Si la variable error no esta vacia, muestra un mensaje indicando</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>los campos que no estan ingresados correctamente</em></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>if</em> errores != "":</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#<em>El metodo showerror de la libreria messagebox permite mostrar</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><em>una ventana emergente con los parametros ingresados</em></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>messagebox.showerror(</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><table>
<tbody>
<tr class="odd">
<td><blockquote>
<p>title="Error",</p>
</blockquote></td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>message="Los siguientes campos no se ingresaron</p>
</blockquote></td>
</tr>
<tr class="even">
<td>correctamente: " + errores,</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>return</em> True</p>
</blockquote></td>
</tr>
</tbody>
</table>

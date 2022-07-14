#Importo la libreria TK para poder crear una ventana que luego voy a utilizar a la hora de llamar a mi Vista
from tkinter import Tk
#Importo el modulo "modelo" para poder utilizar sus clases y funciones
import modelo
#Importo el modulo "vista" para poder utilizar sus clases y funciones
import vista


#Creo la clase controlador 
class Controller:
    # funcion que se ejecuta al instanciar la clase
    # Toma como parametro a un objeto Tk (ventana del programa) 
    def __init__(self, ventana, ):
        #Creo un objeto utilizando la clase "Abmc" del modulo "modelo"
        self.objeto_modelo = modelo.Abmc()
        #Creo/Conecto la base de datos 
        self.objeto_modelo.crear_db()
        #Creo la tabla "libros" en caso de que no haya  sido creada previamente
        self.objeto_modelo.crear_tabla_libro()
        # guardo la ventana en un atributo de instancia
        self.ventana = ventana
        # Creo un objeto "Panel" de modulo vista y le envio la ventana como parametro
        self.objeto_vista = vista.Panel(self.ventana, self.objeto_modelo)



# verifica que el modulo se haya ejecutado como programa principal
if __name__ == "__main__":
    
    #Creo la ventana donde voy a pocisionar mis elementos visuales haciendo una instacia del objeto "TK"
    root = Tk()

    # Instancio un objeto "Controller" y le envio la ventana como parametro
    mi_app = Controller(root)

    # Crea un loop infinito que permite visualizar la ventana
    # Sin esta funcion, la ventana se cerraria al momento de ejecutar el programa
    root.mainloop()

from tkinter import Tk
import modelo
import vista


#Creo la clase controlador 
class Controller:
    # funcion que se ejecuta al instanciar la clase
    # Toma como parametro a un objeto Tk (ventana del programa) y a un objeto "Abmc" del modulo ventana
    def __init__(self, root_v, objeto_modelo):
        # guardo la ventana en un atributo de instancia
        self.root = root_v
        # Creo un objeto "Panel" de modulo vista y le envio la ventana como parametro
        self.objeto_vista = vista.Panel(self.root, objeto_modelo)


# verifica que el modulo se haya ejecutado como programa principal
if __name__ == "__main__":

    try:
        # Instacio al objeto modelo e inicio/creo la base de datos
        objeto_modelo = modelo.Abmc()
        objeto_modelo.modelo.crear_db()
        objeto_modelo.modelo.crear_tabla_libro()
    except:
        exit

    # Instancio un objeto Tk 
    root = Tk()

    # Instancio un objeto "Controller" y le envio la ventana y el objeto "Abmc" como parametro
    mi_app = Controller(root, objeto_modelo)

    # Crea un loop infinito que permite visualizar la ventana
    # Sin esta funcion, la ventana se cerraria al momento de ejecutar el programa
    root.mainloop()

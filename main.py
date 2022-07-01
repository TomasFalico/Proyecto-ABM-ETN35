from tkinter import Tk
import modelo
import vista


class Controller:
    # funcion que se ejecuta al instanciar la clase
    def __init__(self, root_v, objeto_modelo):
        # guardo ventana en atributo de instancia
        self.root = root_v
        # instancio panel de modulo vista y le envio la ventana como parametro
        self.objeto_vista = vista.Panel(self.root, objeto_modelo)


# verifica que el modulo se haya ejecutado como programa principal
if __name__ == "__main__":

    try:
        # instacio al objeto modelo e inicio/creo la base de datos
        objeto_modelo = modelo.Abmc()
        objeto_modelo.modelo.crear_db()
        objeto_modelo.modelo.crear_tabla_libro()
    except:
        exit

    root = Tk()

    # instancio controlador y le envio la ventana y el objeto modelo como parametro
    mi_app = Controller(root, objeto_modelo)

    root.mainloop()

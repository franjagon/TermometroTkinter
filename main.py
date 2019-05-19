from tkinter import *
from tkinter import ttk

'''Nuestra clase principal será un frame de TKINTER en el que habrá un campo de entrada en el que escribiremos una cantidad
   y tres radiobuttons para poder convertir esa cantidad en tres unidades diferentes.
   La clase principal heradará de la clase -Tk- de TKINTER y así, en sí misma, ya será un frame TKINTER con todos sus atributos
   y métodos, al que le podremos agregar los nuestros.'''
class ConversorTemperatura(Tk):
    temperatura = None
    unidad = None
    __temperaturaAnterior = None
    __unidadAnterior = None
    
    '''El método constructor no recibirá valores. Se encargará de heredar del frame de TKINTER.'''    
    def __init__(self):
        '''Lo primero es instanciar la clase padre -Tk-.'''
        Tk.__init__(self)
        
        '''Y ahora que nuestra clase es un frame TKINTER, lo dimensionamos, lo titulamos, le ponemos un color de fondo RGB en hexadecimal
           e indicamos que no se pueda redimensionar, usando los métodos de la clase -Tk-.'''
        self.geometry("205x160")
        self.title("C F K")
        self.configure(bg = "#ECECEC")
        self.resizable(0 ,0)
        
        '''Inicializamos los atributos de nuestra clase principal, asociándolos a variables de control de la clase Tk que se encargarán de
           controlar los valores que vayan conteniendo con sus métodos de trazado.'''
        self.__temperaturaAnterior = ""
        self.__unidadAnterior = "C"
        self.temperatura = StringVar(value = self.__temperaturaAnterior)
        self.temperatura.trace('w', self.validaTemp)
        self.unidad = StringVar(value = self.__unidadAnterior)
        
        '''Invocamos un método propio que nos dibujará los objetos en el frame.'''
        self.__capaGrafica()
    
    '''Este método se encargará de crear los objetos gráficos y de situarlos en el frame.'''
    def __capaGrafica(self):
        '''Nuestro primer objeto será un campo de entrada en el que escribiremos la temperatura a convertir.
           Indicamos que pertenecerá a nuestro frame, que tendrá asociada la variable de texto -temperatura- y lo colocamos.'''
        self.cajaEntrada = ttk.Entry(self, textvariable = self.temperatura).place(x = 40, y = 10)
        
        '''Ahora colocaremos una etiqueta informativa.'''
        self.etiquetaGrados = ttk.Label(self, text = "Grados").place(x = 50, y = 45)
        
        '''Y ahora los radiobuttons que se encargarán de marcar a que unidad convertimos la temperatura.'''
        self.rbC = ttk.Radiobutton(self, text = "Celsius", variable = self.unidad, value = "C", command = self.seleccionRB). place(x = 65, y = 70)
        self.rbF = ttk.Radiobutton(self, text = "Fahrenheit", variable = self.unidad, value = "F", command = self.seleccionRB). place(x = 65, y = 90)
        self.rbK = ttk.Radiobutton(self, text = "Kelvin", variable = self.unidad, value = "K", command = self.seleccionRB). place(x = 65, y = 110)
    
    '''Este método validará que lo que se introduce en la -cajaEntrada- sea una temperatura válida.'''
    def validaTemp(self, *args):
        '''Sólo validaremos si la variable de control -temperatura- contuviera algo y evitamos validar si sólo contuviera el signo menos.
           Si se introduce el signo menos, será porque se ha borrado toda el contenido de -cajaEntrada- y se quiere anteponer a una nueva
           cantidad, por tanto, inicializaremos a cero la variable privada -__temperaturaAnterior- para evitar que al introducir un carácter
           no valido tras el signo menos la validación imponga el último carácter borrado antes de meter dicho signo menos.'''
        if len(self.temperatura.get()) != 0 and self.temperatura.get() != '-':
            '''La validación consistirá en intentar castear el contenido de la variable de control -temperatura- en float.
               Si se puede, cargaremos el nuevo valor en la variable privada -__temperaturaAnterior-.
               Si no se puede, devolveremos a la variable de control -temperatura- lo que tuvieramos guardado en la
               variable privada -__temperaturaAnterior-.'''
            try:
                float(self.temperatura.get())
                self.__temperaturaAnterior = self.temperatura.get()
            except:
                self.temperatura.set(self.__temperaturaAnterior)
        elif self.temperatura.get() == '-':
            self.__temperaturaAnterior = 0
        
    
    '''Este método albergará el código funcional de conversión de temperatura que se ejecutará cuando se seleccione uno u otro radiobutton.'''
    def seleccionRB(self):
        '''Sólo convertiremos si la variable de control -temperatura- contuviera algo y evitamos convertir si sólo contuviera el signo menos.'''
        if len(self.temperatura.get()) != 0 and self.temperatura.get() != '-':
            '''Sólo si la unidad seleccionada es -F- y antes la unidad era -C- o -K-, aplicamos la fórmula que toque.'''
            '''Sólo si la unidad seleccionada es -K- y antes la unidad era -C- o -F-, aplicamos la fórmula que toque.'''
            '''Sólo si la unidad seleccionada es -C- y antes la unidad era -F- o -K-, aplicamos la fórmula que toque.'''
            '''Si ninguna de las tres condiciones se cumple, posiblemente se está volviendo a pulsar el radiobutton que ya estaba seleccionado.'''
            if self.unidad.get() == "F":
                if self.__unidadAnterior == "C":
                    self.temperatura.set(32 + (float(self.temperatura.get()) * 9 / 5))
                elif self.__unidadAnterior == "K":
                    self.temperatura.set(32 + ((float(self.temperatura.get()) - 273.15) * 9 / 5))
            elif self.unidad.get() == "C":
                if self.__unidadAnterior == "F":
                    self.temperatura.set((float(self.temperatura.get()) - 32) * 5 / 9)
                elif self.__unidadAnterior == "K":
                    self.temperatura.set(float(self.temperatura.get()) - 273.15)
            elif self.unidad.get() == "K":
                if self.__unidadAnterior == "F":
                    self.temperatura.set(273.15 + ((float(self.temperatura.get()) - 32) * 5 / 9))
                elif self.__unidadAnterior == "C":
                    self.temperatura.set(273.15 + float(self.temperatura.get()))

        '''Se realice o no conversión, actualizamos la variable privada -__unidadAnterior- al valor del radiobutton que quede seleccionado.'''
        self.__unidadAnterior = self.unidad.get()
    
    '''Este método arrancará la ejecución del frame con el método -mainloop- de la clase -Tk-.'''
    def comenzar(self):
        self.mainloop()

'''Nuestra ejecución como programa principal instanciará un objeto -ConversorTemperatura- e invocará su método -comenzar- para que se inicie la ejecución.'''
if __name__ == "__main__":
    ConverTemp = ConversorTemperatura()
    ConverTemp.comenzar()

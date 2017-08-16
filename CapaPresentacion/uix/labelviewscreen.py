import os

from libtools.filesystem import Archivo
from libtools.filesystem import Carpeta

from kivy.uix.screenmanager import Screen
from CapaNegocio.printing import Printer


class LabelViewScreen(Screen):

    archivo = None

    def __init__(self, **kwargs):
        super(LabelViewScreen, self).__init__(**kwargs)
        self._show_loader(False)

    def _show_loader(self, show):
        if show:
            self.ids['loader'].opacity = 1.0
        else:
            self.ids['loader'].opacity = 0.0

    def failure(self, error):
        self._show_toast(error)
        self._show_loader(False)

    def _show_toast(self, text):
        self.ids['toast'].show(text)

    def set_ImageEmpty(self):
        deafult_abspath = os.path.abspath(os.path.join(os.getcwd(), "data", "images", "no_img.png"))
        self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = deafult_abspath

    def get_ImageFile(self, _archivo_pdf):
        folder = Carpeta(_archivo_pdf.carpeta.abspath)
        nombre = _archivo_pdf.nombre.replace("pdf", "png")
        archivo = Archivo(folder, nombre)
        archivo.exist("buscando_imagen")
        return archivo

    def set_Label(self, _flag, _content, _archivo_pdf):

        contenedor = self.ids['label_container'].ids['labelview_widget']

        contenedor.ids['img_etiqueta'].source = ""

        if _flag:
            try:
                self.archivo = _archivo_pdf
                archivo_img = self.get_ImageFile(_archivo_pdf)
                contenedor.ids['img_etiqueta'].source = archivo_img.get_Abspath()
                contenedor.ids['lbl_etiqueta_view'].text = _content

            except Exception as error:
                self.set_ImageEmpty()
                contenedor.ids['lbl_etiqueta_view'].text = str(error)
        else:
            self.set_ImageEmpty()
            contenedor.ids['lbl_etiqueta_view'].text = _content

    def imprimir(self):

        try:
            cantidad = str(self.ids['txt_number_labels'].text)

            if cantidad != "" and cantidad != "0":
                if int(cantidad) <= 5:
                    self._show_loader(True)
                    for x in range(0, int(cantidad)):
                        Printer.send(self.archivo)
                    self._show_loader(False)
                else:
                    raise ValueError("No puede imprimirse mas de 5 veces")
            else:
                raise ValueError("Falta especificar el numero de Impresiones")

        except Exception as e:
            self.failure(str(e))

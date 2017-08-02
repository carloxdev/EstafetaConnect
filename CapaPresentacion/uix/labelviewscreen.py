import os

from libtools.filesystem import Archivo
from libtools.filesystem import Carpeta

from kivy.uix.screenmanager import Screen
from CapaNegocio.printing import Printer


class LabelViewScreen(Screen):

    fac_numero = None
    fac_tipo = None

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

    def imprimir(self):
        try:
            self._show_loader(True)
            Printer.send(self.fac_numero, self.fac_tipo)
            self._show_loader(False)
        except Exception as e:
            self.failure(str(e))

    def set_ImageEmpty(self):
        deafult_abspath = os.path.abspath(os.path.join(os.getcwd(), "data", "images", "no_img.png"))
        self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = deafult_abspath

    def get_ImageFile(self):
        abspath = os.path.abspath(os.path.join(os.getcwd(), "etiquetas"))
        folder = Carpeta(abspath)
        file_name = "%s_%s.png" % (self.fac_tipo, self.fac_numero)
        archivo = Archivo(folder, file_name)
        archivo.exist("buscando_imagen")
        return archivo

    def set_Label(self, _flag, _content):

        self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = ""

        if _flag:
            try:
                archivo_img = self.get_ImageFile()
                self.ids['label_container'].ids['labelview_widget'].ids['img_etiqueta'].source = archivo_img.get_Abspath()
                self.ids['label_container'].ids['labelview_widget'].ids['lbl_etiqueta_view'].text = _content
            except Exception as error:
                self.set_ImageEmpty()
                self.ids['label_container'].ids['labelview_widget'].ids['lbl_etiqueta_view'].text = str(error)
        else:
            self.set_ImageEmpty()
            self.ids['label_container'].ids['labelview_widget'].ids['lbl_etiqueta_view'].text = _content

# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty

from CapaNegocio.gestordb import ModeloEstafetaAmbiente
from libtools.data import Validator


class EstafetaScreen(Screen):

    def __init__(self, **kwargs):
        super(EstafetaScreen, self).__init__(**kwargs)
        self._show_loader(False)
        self.show_Registros()

    def _show_loader(self, show):
        if show:
            self.ids['loader'].opacity = 1.0
        else:
            self.ids['loader'].opacity = 0.0

    def _show_toast(self, text):
        self.ids['toast'].show(text)

    def failure(self, error):
        self._show_toast(error)
        self._show_loader(False)

    def show_Registros(self):
        try:
            self._show_loader(True)
            cadena_buscar = self.ids['txt_buscar'].text
            contenedor = self.ids['estafeta_container'].ids['container']
            contenedor.clear_widgets()
            registros = ModeloEstafetaAmbiente.get(cadena_buscar)

            for registro in registros:
                widget = EstafetaItem(registro, self)
                contenedor.add_widget(widget)

            self._show_loader(False)

        except Exception as e:
            self.failure(str(e))

    def click_BotonNuevo(self):
        EstafetaAddPopup(self).open()

    def click_BotonBuscar(self):
        self.show_Registros()


class EstafetaItem(StackLayout):

    registro = ObjectProperty(None)
    screen = ObjectProperty(None)

    def __init__(self, _registro, _screen, **kwargs):
        super(EstafetaItem, self).__init__(**kwargs)
        self.ids['lbl_clave'].text = _registro.clave
        self.ids['lbl_login'].text = _registro.login
        self.ids['lbl_date'].text = _registro.created_date.strftime('%m/%d/%Y')
        self.registro = _registro
        self.screen = _screen

    def click_BotonEditar(self):
        EstafetaEditPopup(self.registro, self.screen).open()


class EstafetaAddPopup(Popup):

    screen = ObjectProperty(None)

    def __init__(self, _screen, **kwargs):
        super(EstafetaAddPopup, self).__init__(**kwargs)
        self.screen = _screen

    def click_BotonCrear(self):
        clave = self.ids['txt_clave'].text
        url = self.ids['txt_url'].text
        login = self.ids['txt_login'].text
        password = self.ids['txt_password'].text
        quadrant = self.ids['txt_quadrant'].text
        suscriber_id = self.ids['txt_suscriber_id'].text
        paper_type = self.ids['txt_paper_type'].text
        is_active = self.ids['chk_is_active'].active
        cliente_numero = self.ids['txt_customernumber'].text

        cot_url = self.ids['txt_cot_url'].text
        cot_id_usuario = self.ids['txt_cot_id_usuario'].text
        cot_usuario = self.ids['txt_cot_usuario'].text
        cot_contra = self.ids['txt_cot_contra'].text

        ModeloEstafetaAmbiente.add(
            clave,
            url,
            login,
            password,
            quadrant,
            suscriber_id,
            paper_type,
            is_active,
            cliente_numero,
            cot_url,
            cot_id_usuario,
            cot_usuario,
            cot_contra
        )
        self.screen.show_Registros()
        self.dismiss()


class EstafetaEditPopup(Popup):

    screen = ObjectProperty(None)

    def __init__(self, _registro, _screen, **kwargs):
        super(EstafetaEditPopup, self).__init__(**kwargs)
        self.ids['txt_clave'].text = Validator.checkToChar(_registro.clave)
        self.ids['txt_url'].text = Validator.checkToChar(_registro.url)
        self.ids['txt_login'].text = Validator.checkToChar(_registro.login)
        self.ids['txt_password'].text = Validator.checkToChar(_registro.password)
        self.ids['txt_quadrant'].text = Validator.checkToChar(_registro.quadrant)
        self.ids['txt_suscriber_id'].text = Validator.checkToChar(_registro.suscriber_id)
        self.ids['txt_paper_type'].text = Validator.checkToChar(_registro.paper_type)
        self.ids['chk_is_active'].active = Validator.checkToChar(_registro.is_active)
        self.ids['txt_customernumber'].text = Validator.checkToChar(_registro.customer_number)

        self.ids['txt_cot_url'].text = Validator.checkToChar(_registro.cot_url)
        self.ids['txt_cot_id_usuario'].text = Validator.checkToChar(_registro.cot_id_usuario)
        self.ids['txt_cot_usuario'].text = Validator.checkToChar(_registro.cot_usuario)
        self.ids['txt_cot_contra'].text = Validator.checkToChar(_registro.cot_contra)

        self.screen = _screen

    def click_BotonGuardar(self):
        clave = self.ids['txt_clave'].text
        url = self.ids['txt_url'].text
        login = self.ids['txt_login'].text
        password = self.ids['txt_password'].text
        quadrant = self.ids['txt_quadrant'].text
        suscriber_id = self.ids['txt_suscriber_id'].text
        paper_type = self.ids['txt_paper_type'].text
        is_active = self.ids['chk_is_active'].active
        cliente_numero = self.ids['txt_customernumber'].text

        cot_url = self.ids['txt_cot_url'].text
        cot_id_usuario = self.ids['txt_cot_id_usuario'].text
        cot_usuario = self.ids['txt_cot_usuario'].text
        cot_contra = self.ids['txt_cot_contra'].text

        ModeloEstafetaAmbiente.edit(
            clave,
            url,
            login,
            password,
            quadrant,
            suscriber_id,
            paper_type,
            is_active,
            cliente_numero,
            cot_url,
            cot_id_usuario,
            cot_usuario,
            cot_contra
        )
        self.screen.show_Registros()
        self.dismiss()

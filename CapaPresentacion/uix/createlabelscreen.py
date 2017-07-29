from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from CapaPresentacion.uix.widget import Toast

from CapaNegocio.gestordb import ModeloEstafetaUser
from CapaNegocio.gestordb import Factura
from CapaNegocio.gestordb import DireccionOrigen
from CapaNegocio.gestordb import DireccionDestino


class CreateLabelScreen(Screen):

    def __init__(self, **kwargs):
        super(CreateLabelScreen, self).__init__(**kwargs)

    def failure(self, error):
        self._show_toast(error)

    def _show_toast(self, text):
        self.ids['toast'].show(text)

    def buscar_Factura(self):

        factura_numero = str(self.ids['txt_factura_numero'].text)
        factura_tipo = self.ids['txt_factura_tipo'].text

        # fact = Factura.get(factura_numero, factura_tipo)
        # fact = Factura.get(543, 'RI')


        if factura_numero != "" and factura_tipo != "":

            self.clear_DireccionOrigen()
            self.clear_DireccionDestino()
            self.clear_Servicio()
            self.clear_Paquete()

            bandera, dir_origen = DireccionOrigen.get(factura_numero, factura_tipo)

            if bandera:
                self.fill_DireccionOrigen(dir_origen)

            bandera, dir_destino = DireccionDestino.get(factura_numero, factura_tipo)

            if bandera:
                self.fill_DireccionDestino(dir_destino)

        else:
            self.failure("Falto especificar Factura")

    def fill_DireccionOrigen(self, _data):
        data = self.ids['label_container'].ids['origen_widget']
        data.ids['txt_origen_address1'].text = _data["address1"]
        data.ids['txt_origen_address2'].text = _data["address2"]
        data.ids['txt_origen_cellphone'].text = _data["cellphone"]
        data.ids['txt_origen_city'].text = _data['city']
        data.ids['txt_origen_contactname'].text = _data["contactname"]
        data.ids['txt_origen_corporatename'].text = _data["corporatename"]
        data.ids['txt_origen_customernumber'].text = "000000"
        data.ids['txt_origen_neighborhood'].text = _data['neighborhood']
        data.ids['txt_origen_phonenumber'].text = _data["phonenumber"]
        data.ids['txt_origen_state'].text = _data['state']
        data.ids['txt_origen_zipcode'].text = _data['zipcode']

    def clear_DireccionOrigen(self):
        data = self.ids['label_container'].ids['origen_widget']
        data.ids['txt_origen_address1'].text = ""
        data.ids['txt_origen_address2'].text = ""
        data.ids['txt_origen_cellphone'].text = ""
        data.ids['txt_origen_city'].text = ""
        data.ids['txt_origen_contactname'].text = ""
        data.ids['txt_origen_corporatename'].text = ""
        data.ids['txt_origen_customernumber'].text = ""
        data.ids['txt_origen_neighborhood'].text = ""
        data.ids['txt_origen_phonenumber'].text = ""
        data.ids['txt_origen_state'].text = ""
        data.ids['txt_origen_zipcode'].text = ""

    def fill_DireccionDestino(self, _data):
        data = self.ids['label_container'].ids['destino_widget']
        data.ids['txt_destino_address1'].text = _data["address1"]
        data.ids['txt_destino_address2'].text = _data["address2"]
        data.ids['txt_destino_cellphone'].text = _data["cellphone"]
        data.ids['txt_destino_city'].text = _data['city']
        data.ids['txt_destino_contactname'].text = _data["contactname"]
        data.ids['txt_destino_corporatename'].text = _data["corporatename"]
        data.ids['txt_destino_customernumber'].text = "000000"
        data.ids['txt_destino_neighborhood'].text = _data['neighborhood']
        data.ids['txt_destino_phonenumber'].text = _data["phonenumber"]
        data.ids['txt_destino_state'].text = _data['state']
        data.ids['txt_destino_zipcode'].text = _data['zipcode']

    def clear_DireccionDestino(self):
        data = self.ids['label_container'].ids['destino_widget']
        data.ids['txt_destino_address1'].text = ""
        data.ids['txt_destino_address2'].text = ""
        data.ids['txt_destino_cellphone'].text = ""
        data.ids['txt_destino_city'].text = ""
        data.ids['txt_destino_contactname'].text = ""
        data.ids['txt_destino_corporatename'].text = ""
        data.ids['txt_destino_customernumber'].text = ""
        data.ids['txt_destino_neighborhood'].text = ""
        data.ids['txt_destino_phonenumber'].text = ""
        data.ids['txt_destino_state'].text = ""
        data.ids['txt_destino_zipcode'].text = ""

    def fill_Servicio(self, _data):
        data = self.ids['label_container'].ids['servicio_widget']
        data.ids['txt_num_cliente'].text = ""
        data.ids['txt_servicetypeid'].text = "70"
        data.ids['txt_number_labels'].text = "1"
        data.ids['txt_office_num'].text = "130"
        data.ids['txt_contentdescription'].text = ""
        data.ids['txt_aditionalinfo'].text = ""
        data.ids['txt_costcenter'].text = ""
        data.ids['txt_content'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_servicetypeiddocret'].text = ""
        data.ids['txt_destino_countryid'].text = ""
        data.ids['txt_reference'].text = ""

    def clear_Servicio(self):
        data = self.ids['label_container'].ids['servicio_widget']
        data.ids['txt_num_cliente'].text = ""
        data.ids['txt_servicetypeid'].text = "70"
        data.ids['txt_number_labels'].text = "1"
        data.ids['txt_office_num'].text = "130"
        data.ids['txt_contentdescription'].text = ""
        data.ids['txt_aditionalinfo'].text = ""
        data.ids['txt_costcenter'].text = ""
        data.ids['txt_content'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_servicetypeiddocret'].text = ""
        data.ids['txt_destino_countryid'].text = ""
        data.ids['txt_reference'].text = ""

    def clear_Paquete(self):
        data = self.ids['label_container'].ids['paquete_widget']
        data.ids['txt_peso'].text = ""
        data.ids['txt_kilos'].text = ""
        data.ids['txt_parcelTypeId'].text = "1"
        data.ids['txt_largo'].text = ""
        data.ids['txt_alto'].text = ""
        data.ids['txt_ancho'].text = ""


class PaqueteWidget(StackLayout):

    def open_TipoPaquetePopup(self):
        TipoPaquetePopup(self).open()

    def fill_Campos(self, _value):

        self.clear_Campos()
        self.ids['txt_parcelTypeId'].text = _value

    def clear_Campos(self):
        self.ids['txt_parcelTypeId'].text = ''


class TipoPaquetePopup(Popup):
    padre = ObjectProperty(None)

    def __init__(self, padre, **kwargs):
        super(TipoPaquetePopup, self).__init__(**kwargs)
        self.padre = padre

        self.show_All_Options()

    def show_All_Options(self):

        self.ids['container'].clear_widgets()

        widgetSobre = TipoPaqueteWidget("1", "Sobre")
        widgetPaquete = TipoPaqueteWidget("4", "Paquete")

        self.ids['container'].add_widget(widgetSobre)
        self.ids['container'].add_widget(widgetPaquete)

    def click_SelectButton(self):

        value = ""

        for hijo in self.ids['container'].children:

            if hijo.ids['chk_tipo'].active is True:
                value = hijo.valor

        if value:
            self.padre.fill_Campos(value)
            self.dismiss()


class TipoPaqueteWidget(BoxLayout):

    valor = ObjectProperty(None)

    def __init__(self, _valor, _descripcion, **kwargs):
        super(TipoPaqueteWidget, self).__init__(**kwargs)
        self.valor = _valor
        self.ids["lbl_tipo"].text = _descripcion


class CredencialesWidget(StackLayout):

    def open_CredencialesPopup(self):
        CredencialesPopup(self).open()

    def fill_Campos(self, cuenta):

        self.clear_Campos()
        self.ids['txt_cuenta'].text = cuenta.clave
        self.ids['txt_url'].text = cuenta.url
        self.ids['txt_login'].text = cuenta.login
        self.ids['txt_suscriber_id'].text = cuenta.suscriber_id
        self.ids['txt_password'].text = cuenta.password
        self.ids['txt_quadrant'].text = str(cuenta.quadrant)
        self.ids['txt_tipo_papel'].text = str(cuenta.paper_type)

    def clear_Campos(self):
        self.ids['txt_cuenta'].text = ''
        self.ids['txt_url'].text = ''
        self.ids['txt_login'].text = ''
        self.ids['txt_suscriber_id'].text = ''
        self.ids['txt_password'].text = ''
        self.ids['txt_quadrant'].text = ''
        self.ids['txt_tipo_papel'].text = ''


class CredencialesPopup(Popup):

    padre = ObjectProperty(None)

    def __init__(self, padre, **kwargs):

        super(CredencialesPopup, self).__init__(**kwargs)

        self.padre = padre

        self.show_All_Cuentas()

    def show_All_Cuentas(self):

        self.ids['container'].clear_widgets()

        cuentas = ModeloEstafetaUser.get()

        for cuenta in cuentas:
            widget = CuentaWidget(cuenta)
            self.ids['container'].add_widget(widget)

    def click_SelectButton(self):

        cuenta = None

        for hijo in self.ids['container'].children:

            if hijo.ids['chk_cuenta'].active is True:
                cuenta = hijo.cuenta

        if cuenta:
            self.padre.fill_Campos(cuenta)
            self.dismiss()


class CuentaWidget(BoxLayout):

    cuenta = ObjectProperty(None)

    def __init__(self, _cuenta, **kwargs):
        super(CuentaWidget, self).__init__(**kwargs)
        self.ids["lbl_cuenta"].text = _cuenta.clave
        self.cuenta = _cuenta

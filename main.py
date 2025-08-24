from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
import pandas as pd
import matplotlib.pyplot as plt

Window.size = (360, 640)  # Para pruebas en PC, en celular ignora

KV = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDLabel:
            text: "Finanzas Personales"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: desc
            hint_text: "Descripción"

        MDTextField:
            id: amount
            hint_text: "Monto"
            input_filter: "float"

        MDSpinner:
            id: category
            text: "Categoría"
            values: ["Comida","Transporte","Entretenimiento","Salud","Otros"]

        MDRaisedButton:
            text: "Agregar gasto"
            on_release: app.agregar_gasto(desc.text, amount.text, category.text)

        MDRaisedButton:
            text: "Mostrar gráfico"
            on_release: app.mostrar_grafico()

        ScrollView:
            MDList:
                id: lista_gastos
'''

class FinanzasApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.df_file = "gastos.csv"
        try:
            self.df = pd.read_csv(self.df_file)
        except:
            self.df = pd.DataFrame(columns=["Descripción","Monto","Categoría"])
            self.df.to_csv(self.df_file, index=False)
        return Builder.load_string(KV)

    def agregar_gasto(self, desc, amount, category):
        if not desc or not amount or not category:
            return
        self.df = pd.concat([self.df, pd.DataFrame([[desc, float(amount), category]], columns=self.df.columns)])
        self.df.to_csv(self.df_file, index=False)
        self.root.ids.lista_gastos.add_widget(OneLineListItem(text=f"{desc} - ${amount} - {category}"))
        self.root.ids.desc.text = ""
        self.root.ids.amount.text = ""

    def mostrar_grafico(self):
        if self.df.empty:
            return
        summary = self.df.groupby("Categoría")["Monto"].sum()
        plt.figure(figsize=(5,4))
        summary.plot(kind="pie", autopct='%1.1f%%', startangle=90)
        plt.title("Gastos por categoría")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    FinanzasApp().run()
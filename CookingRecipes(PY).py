import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class RecipeApp(App):

    def build(self):
        # Definir la interfaz de usuario
        layout = GridLayout(cols=2)

        # Receta 1
        layout.add_widget(Label(text='Receta 1 - Nombre'))
        self.recipe1_name = TextInput(text='Ensalada César')
        layout.add_widget(self.recipe1_name)

        layout.add_widget(Label(text='Receta 1 - Ingredientes'))
        self.recipe1_ingredients = TextInput(text='- Lechuga romana\n- Pollo asado\n- Pan tostado\n- Queso parmesano rallado\n- Salsa César')
        layout.add_widget(self.recipe1_ingredients)

        layout.add_widget(Label(text='Receta 1 - Instrucciones'))
        self.recipe1_instructions = TextInput(text='1. Trocear la lechuga y el pollo asado.\n2. Tostar el pan y cortarlo en cuadraditos.\n3. Incorporar La lechuga y el pollo en un bol y añadir el pan tostado.\n4. Espolvorear el queso parmesano rallado y servir con la salsa César.')
        layout.add_widget(self.recipe1_instructions)

        # Receta 2
        layout.add_widget(Label(text='Receta 2 - Nombre'))
        self.recipe2_name = TextInput(text='Espaguetis a la boloñesa')
        layout.add_widget(self.recipe2_name)

        layout.add_widget(Label(text='Receta 2 - Ingredientes'))
        self.recipe2_ingredients = TextInput(text='- 400g de espaguetis\n- 500g de carne picada\n- 1 cebolla\n- 2 dientes de ajo\n- 2 zanahorias\n- 2 ramas de apio\n- 1 lata de tomate triturado\n- Aceite de oliva\n- Sal y pimienta')
        layout.add_widget(self.recipe2_ingredients)

        layout.add_widget(Label(text='Receta 2 - Instrucciones'))
        self.recipe2_instructions = TextInput(text='1. Pelar y picar la cebolla y el ajo. Pelar y rallar las zanahorias.\n2. Calentar aceite de oliva en una sartén y dorar la carne picada.\n3. Añadir la cebolla, el ajo, las zanahorias y el apio picado y sofreír durante unos minutos.\n4. Añadir el tomate triturado, salpimentar y cocinar a fuego lento durante 20-25 minutos.\n5. Cocer los espaguetis en agua con sal hasta que estén al dente. Escurrirlos y añadir la salsa boloñesa. Mezclar bien y servir caliente.')
        layout.add_widget(self.recipe2_instructions)

        return layout

if __name__ == '__main__':
    RecipeApp().run()



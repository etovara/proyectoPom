from selenium.webdriver.common.by import By

# Se debe crear una clase

class locators():
# Se debe copiar los localizadores de los Pages de manera separada.
# Se debe eliminar el self debido a que son variables de la nueva clase creada en los localizadores
# Una vez creada los localizadores, se deben importar desde los Pages
# Una vez importados los localizadores, es importante modificar las variables declaradas en su oportunidad en los Page para que realice el llamado desde los localizadores

## Ejemplo

 # self.register_button_id       = 'signin2' se reemplaza por 
 # self.register_button_id       = locators.register_button_id



  # Localizadores de loginPage.py
    
  register_button_id       = 'signin2'
  username_textbox_id      = "sign-username"
  password_textbox_id      = "sign-password"
  click_cancelar_xpath           = '//*[@id="signInModal"]/div/div/div[3]/button[1]'
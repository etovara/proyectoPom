# Se debe crear una clase
class loginPage():
  
    # Se debe crear un contructor +  un argumento para el controlador 
    def __init__(self, driver):
      self.driver = driver
    
    # Se debe agregar los objectos existente en la pagina
      self.singUp= "signin2"
      self.username_textbox_id = "sign-username"
      self.password_textbox_id = "sign-password"
      self.cancelar_XPATH = "//*[@id="signInModal"]/div/div/div[3]/button[1]"
      
      
    # Se debe crear una función o metodo de acción
    def click_singUp(self):
      self.driver.find_element(By.ID, self.singUp).click()
      
    
    def enter_username(self, username):
      self.driver.find_element(By.ID, self.username_textbox_id).clear()
      self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)
      

    def enter_password(self, password):
      self.driver.find_element(By.ID, self.password_textbox_id).clear()
      self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)
      
      
    def click_cancelar(self):
      self.driver.find_element(By.XPATH, self.cancelar_XPATH).click()
      


#Una vez que se declaran la funciones / metodos en los Pages se debe ir a los test generados para comentar o se pueden eliminar de acuerdo a las politicas de empresa.

# una vez realizada esa acción debemos llamar desde los Test las funciones creadas en los Pages (Revisar el From posterior a los import)

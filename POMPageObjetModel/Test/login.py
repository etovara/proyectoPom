from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from proyectoPom.POMPageObjetModel.Pages.loginPage import loginPage
import time
import unittest #Importar el modulo de pruebas de Python


# Se debe declarar la clase de la prueba Registro (Caso de Prueba. Clase de Prueba)
class RegistroTest(unittest.TestCase):

# Se debe declarar las funciones de configuración setUpClass(cls) antes de que se ejecuten las pruebas en una clase individual.

  @classmethod
  def setUpClass(cls): # Un método de clase llamado antes de que los tests en una clase individual sean ejecutados
    
    #Ubicacion del Driver y Url prueba
    cls.driver = webdriver.Chrome(executable_path= r"C:\Users\Edwin Tovar\Desktop\proyectoPom\chromedriver\chromedriver.exe")
    cls.driver.implicitly_wait(10)
    cls.driver.maximize_window()
  
  # Se va a estar creando un nuevo objeto el cual va a estar realizando el llamado a los Page de las clases, esto es para poder tener un controlador de recorrido declarado y no automatico.
  
  def test_login_valid(self):
    driver = self.driver
    driver.get("https://www.demoblaze.com/index.html")
    time.sleep(2)
    
    login = loginPage(driver)
    time.sleep(2)
    login.click_singUp()
    time.sleep(2)
    login.enter_username("EDTOVAR")
    time.sleep(2)
    login.enter_password("12345")
    time.sleep(2)
    login.click_cancelar()
    
      
  
  """ Voy a estar comentando estas linea, ya que una vez que hice las pruebas de manera individual las envie al Page y luego hice el llamado a traves del From
  
  def test_registro_usuario(self):
    self.driver.get("https://www.demoblaze.com/index.html")
    
    #Registro Usuario
    self.driver.find_element(By.ID, 'signin2').click()
    time.sleep(3)

    #Completa el Formulario Registro
    self.driver.find_element(By.ID, "sign-username").send_keys("EDTOVAR")
    time.sleep(2)

    self.driver.find_element(By.ID, "sign-password").send_keys("12345")
    time.sleep(2)

    #Permite buscar la información de un archivo
    #Password = open('Practica/clave.txt').readline().strip()

    #Cancelar Registro
    self.driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[1]').click()
    time.sleep(3)
   """
   
  @classmethod  
  def tearDownClass(cls): # Un método de clase llamado después de que se hayan realizado tests en una clase individual.
    cls.driver.close()
    cls.driver.quit()
    time.sleep(3)
    print("Test Completado")

if __name__ == '__main__':
    unittest.main()
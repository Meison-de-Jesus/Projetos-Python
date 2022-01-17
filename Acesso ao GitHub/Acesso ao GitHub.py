from selenium import webdriver
from time import sleep

# Automatizando login no GitHub


class ChromeAuto:
    def __init__(self):
        self.driver_path = "/usr/local/bin/chromedriver"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("user-data-dir=Meison")
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar(self, site):
        self.chrome.get(site)

    def clicar_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text("Sign in")
            btn_sign_in.click()
        except Exception as erro:
            print("Houve um erro ao clicar em Sign in:", erro)

    def logar_usuario(self):
        try:
            usuario = self.chrome.find_element_by_id("login_field")
            sleep(0.2)
            senha = self.chrome.find_element_by_id("password")
            sleep(0.2)
            btn_login = self.chrome.find_element_by_name("commit")
            usuario.send_keys("seu_email")
            senha.send_keys("sua_senha")
            sleep(1)
            btn_login.click()
        except Exception as erro:
            print("Houve um erro ao tentar logar:", erro)

    def clicar_perfil_usuario(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                "body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details")
            perfil.click()
        except Exception as erro:
            print("Houve um erro ao clicar no perfil:", erro)

    def clicar_repositorios(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text(
                "Your repositories")
            btn_sign_in.click()
        except Exception as erro:
            print("Houve um erro ao acessar os repositórios:", erro)

    def logout_usuario(self):
        try:
            sleep(3)
            perfil = self.chrome.find_element_by_css_selector(
                "button.dropdown-item:nth-child(2)")
            perfil.click()
        except Exception as erro:
            print("Houve um erro ao fazer logout", erro)

    def sair(self):
        self.chrome.quit()


if __name__ == "__main__":
    chrome = ChromeAuto()
    chrome.acessar("https://github.com")

chrome.clicar_sign_in()
chrome.logar_usuario()
chrome.clicar_perfil_usuario()
chrome.clicar_repositorios()
chrome.logout_usuario()
chrome.sair()

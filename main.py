"""
Premissa: baixar o geckodriver em: https://github.com/mozilla/geckodriver/releases e apontar
o diretorio do driver na variavel 'path' do windows.
"""
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def acessar_site_shopper_limpo():
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.cache.disk.enable", False)
    firefox_profile.set_preference("browser.cache.memory.enable", False)
    firefox_profile.set_preference("browser.cache.offline.enable", False)
    firefox_profile.set_preference("network.http.use-cache", False)
    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    browser.get('https://shopper.com.br/')
    assert 'Shopper' in browser.title
    return browser


def acessar_site_shopper():
    browser = webdriver.Firefox()
    browser.get('https://shopper.com.br/')
    assert 'Shopper' in browser.title
    return browser


def realizar_login(browser):
    elements = browser.find_elements_by_tag_name('button')
    for e in elements:
        if e.text == 'ENTRAR':
            e.click()

    form = browser.find_element_by_tag_name('form')
    form.find_element_by_name('email').send_keys('jhow.rafael@hotmail.com')
    form.find_element_by_name('senha').send_keys('jhow123shopper')
    form.find_element_by_tag_name('button').click()

    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and @type='button']"))).click()
    except:
        print("Timed Out!!!!!")
        pass
    finally:
        print("Pagina carregada!")
    time.sleep(3)


def recuperar_valor_carrinho(browser):
    valor = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/button/span/span/span').get_attribute('innerHTML')
    return float(str(valor).replace(',', '.'))


def comprar_produto_anuncio(browser):
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-gBsxbr dxFZky"]'))).click()

    produtos_anuncio = browser.find_elements_by_xpath('//div[@class="sc-iQQLPo eVFQLq"]')
    print(produtos_anuncio)
    # botao adicionar
    produtos_anuncio[0].find_element_by_xpath('//div[@class="sc-fTFMiz PIJDq"]').click()
    # botao quantidade
    produtos_anuncio[0].find_element_by_xpath('//button[@class="sc-bTJQgd crMrTS"]').click()
    qtd_max_produto = produtos_anuncio[0].find_element_by_xpath(
        '//div[@class="quantity-actions"]').find_element_by_tag_name('input').get_attribute('max')
    produtos_anuncio[0].find_element_by_xpath('//div[@class="quantity-actions"]').find_element_by_tag_name(
        'input').send_keys(int(qtd_max_produto) - 1)
    produtos_anuncio[0].find_element_by_xpath('//button[@class="submit-button"]').click()

    produtos_anuncio[1].find_element_by_xpath('//div[@class="sc-fTFMiz PIJDq"]').click()
    produtos_anuncio[1].find_element_by_xpath('//button[@class="sc-bTJQgd crMrTS"]').click()
    qtd_max_produto = produtos_anuncio[1].find_element_by_xpath(
        '//div[@class="quantity-actions"]').find_element_by_tag_name('input').get_attribute('max')
    produtos_anuncio[1].find_element_by_xpath('//div[@class="quantity-actions"]').find_element_by_tag_name(
        'input').send_keys(int(qtd_max_produto) - 1)
    produtos_anuncio[1].find_element_by_xpath('//button[@class="submit-button"]').click()

    time.sleep(3)


def finalizar_compra(browser):
    browser.find_element_by_xpath('//div[@class="sc-bgPuHN dFTeZX side-cart-toggle"]').find_element_by_tag_name('a').click()


if __name__ == "__main__":
    shopper = acessar_site_shopper()
    realizar_login(shopper)
    # comprar_produto_anuncio(shopper)
    # finalizar_compra(shopper)

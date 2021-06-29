"""
Premissa: baixar o geckodriver em: https://github.com/mozilla/geckodriver/releases e apontar
o diretorio do driver na variavel 'path' do windows.
"""
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def acessar_site_shopper():
    browser = webdriver.Firefox()
    browser.get('https://shopper.com.br/')
    assert 'Shopper' in browser.title
    return browser


def realizar_login(browser, login, senha):
    elements = browser.find_elements_by_tag_name('button')
    for e in elements:
        if e.text == 'ENTRAR':
            e.click()

    form = browser.find_element_by_tag_name('form')
    form.find_element_by_name('email').send_keys(login)
    form.find_element_by_name('senha').send_keys(senha)
    form.find_element_by_tag_name('button').click()

    try:
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and @type='button']"))).click()
    except:
        pass
    time.sleep(3)


def pesquisar_produto(browser, nome_produto):
    navbar = browser.find_element_by_id('reactBuscar')
    form = navbar.find_element_by_tag_name('form')
    form.find_element_by_tag_name('input').send_keys(nome_produto)
    form.find_element_by_xpath('//button[@type="submit"]').click()

    selecionar_qtd_maxima(browser)


def selecionar_qtd_maxima(browser):
    produtos = browser.find_elements_by_xpath('//div[@class="sc-iQQLPo eVFQLq"]')
    produtos[0].find_element_by_xpath('//div[@class="sc-fTFMiz PIJDq"]').click()
    time.sleep(1)
    produtos[0].find_element_by_xpath('//button[@class="sc-bTJQgd crMrTS"]').click()
    qtd_max_produto = produtos[0].find_element_by_xpath(
        '//div[@class="quantity-actions"]').find_element_by_tag_name('input').get_attribute('max')
    produtos[0].find_element_by_xpath('//div[@class="quantity-actions"]').find_element_by_tag_name(
        'input').send_keys(int(qtd_max_produto) - 1)
    produtos[0].find_element_by_xpath('//button[@class="submit-button"]').click()


def recuperar_valor_carrinho(browser):
    valor = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/button/span/span/span').get_attribute('innerHTML')
    return float(str(valor).replace(',', '.'))


def finalizar_compra(browser):
    time.sleep(3)
    browser.find_element_by_xpath('//div[@class="sc-bgPuHN dFTeZX side-cart-toggle"]').find_element_by_tag_name('a').click()


def agendar_entrega(browser, numero_end, data_nasc, sexo):
    browser.find_element_by_xpath('//div[@class="sc-jTFZWL ianKKN"]').click()
    browser.find_element_by_xpath('//input[@name ="number"]').send_keys(numero_end)
    browser.find_element_by_xpath('//input[@name ="birthday"]').send_keys(data_nasc)
    if sexo == 'M':
        browser.find_element_by_xpath('//select[@name ="gender"]/option[@value="M"]').click()
    if sexo == 'F':
        browser.find_element_by_xpath('//select[@name ="gender"]/option[@value="F"]').click()


def realizar_pagamento(browser, nome_cartao, nro_cartao, dt_venc, cvv, cpf):
    browser.find_element_by_xpath('//button[@class="sc-LEMQU dZvoYb sc-cMVuDo dnSSwM"]').click()

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="sc-kOSLtt kLGxTb"]'))).click()

    browser.find_element_by_xpath('//input[@name="name"]').send_keys(nome_cartao)
    browser.find_element_by_xpath('//input[@name="number"]').send_keys(nro_cartao)
    browser.find_element_by_xpath('//input[@name="expiration_month"]').send_keys(
        dt_venc[:2])
    browser.find_element_by_xpath('//input[@name="expiration_year"]').send_keys(
        dt_venc[2:])
    browser.find_element_by_xpath('//input[@name="cvc"]').send_keys(cvv)
    browser.find_element_by_xpath('//input[@name="cpf"]').send_keys(cpf)

    browser.execute_script("window.scrollTo(0, 960)")
    browser.find_element_by_xpath('//label[@class="sc-LvPXS kjLjHl"]').click()
    browser.find_element(By.CSS_SELECTOR, 'button.sc-gefPzt.gTuttx').click()


if __name__ == "__main__":
    shopper = acessar_site_shopper()
    realizar_login(shopper, 'doidocriolo@yahoo.com.br', 'jhow123shopper')
    pesquisar_produto(shopper, 'corona')
    finalizar_compra(shopper)
    agendar_entrega(shopper, '132', '26061992', 'M')
    realizar_pagamento(shopper, 'TESTE - CARTAO FAKE', '5543455559071146',
                       '1022', '551', '86111811827')

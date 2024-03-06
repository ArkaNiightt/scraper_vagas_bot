import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

# Fonte de opções de switches https://chromium.googlesource.com/chromium/src/+/master/chrome/common/chrome_switches.cc e  https://peter.sh/experiments/chromium-command-line-switches/
# Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/master/chrome/common/pref_names.cc
"""
--start-maximized # Inicia maximizado
--lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
--incognito # Usar o modo anônimo
--window-size=800,800 # Define a resolução da janela em largura e altura
--headless # Roda em segundo plano(com a janela fechada)
--disable-notifications # Desabilita notificações
--disable-gpu # Desabilita renderização com GPU
"""


def iniciar_driver(window_size_x=1920, window_size_y=1080):
    chrome_options = Options()
    LOGGER.setLevel(logging.WARNING)
    argumentos = [
        "--lang=pt-BR",
        f"--window-size={window_size_x},{window_size_y}",
        "--incognito",
        # "--headless",
    ]

    for argumento in argumentos:
        chrome_options.add_argument(argumento)

    chrome_options.add_experimental_option(
        "prefs",
        {
            # Desabilitar a confirmação de download
            "download.prompt_for_download": False,
            # Desabilitar notificações
            "profile.default_content_setting_values.notifications": 2,
            # Permitir multiplos downloads
            "profile.default_content_setting_values.automatic_downloads": 1,
        },
    )
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )
    # https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
    wait = WebDriverWait(
        driver=driver,
        timeout=5,
        poll_frequency=10,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ],
    )
    return driver, wait


def input_stop_driver_break(driver):
    try:
        input("Aperte qualquer tecla para fechar")
        driver.close()
    except:
        exit()


def simular_digitacao_lentamente(propriedade: vars, texto: str):
    for letra in texto:
        propriedade.send_keys(letra)
        sleep(random.randint(1, 5) / 30)


def fazer_scroll_pagina(driver, mode: str, scroll_pixel: int):
    # Rolar até o fim da página
    if mode == "final":
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Rolar até o topo da página
    if mode == "inicial":
        sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
    # Rolar Y quantidade em pixels(descer)
    if mode == "down":
        sleep(1)
        driver.execute_script(f"window.scrollTo(0, {scroll_pixel});")
    # Rolar Y quantidade em pixels(subir)
    if mode == "up":
        sleep(1)
        driver.execute_script(f"window.scrollTo(0, {-scroll_pixel});")

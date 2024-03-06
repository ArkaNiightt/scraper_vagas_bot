import scrapy
from scrapy.http import Response
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from web_base_selenium.base_web import (
    input_stop_driver_break,
    iniciar_driver,
    simular_digitacao_lentamente,
)
from selenium.webdriver.common.keys import Keys
from time import sleep

driver, wait = iniciar_driver()


def aceitar_cookies():
    cookies_accept = wait.until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[text()='Aceitar todos os cookies']")
        )
    )
    if cookies_accept is not None:
        sleep(1)
        cookies_accept.click()


def pesquisar_input_vaga(vaga: str):
    try:
        driver.get(url="https://br.indeed.com/")
        sleep(1)
        aceitar_cookies()
        sleep(1)
        campo_pesquisa_vaga = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//input[contains(@id, 'text-input-what')]")
            )
        )
        if campo_pesquisa_vaga is not None:
            simular_digitacao_lentamente(propriedade=campo_pesquisa_vaga, texto=vaga)
            sleep(1)
            campo_pesquisa_vaga.send_keys(Keys.ENTER)
            return driver.current_url
    except Exception as e:
        print("Erro:", e)


page = pesquisar_input_vaga("python")
url_page = page


class Varredor_VagasSpider(scrapy.Spider):
    name = "vagabot"

    # Request
    def start_requests(self):
        urls = [f"{url_page}"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response: Response):
        for element in response.xpath(
            "//td[@class='resultContent css-1qwrrf0 eu4oa1w0']"
        ):
            yield {
                "Cargo": element.xpath(".//span[1]/text()").get(),
                "Empresa": element.xpath(
                    ".//span[@data-testid='company-name']/text()"
                ).get(),
                "Local": element.xpath(
                    ".//div[@data-testid='text-location']/text()"
                ).get(),
                "Link": element.xpath(".//a/@href").get(),
            }
        try:
            link_next_page = response.xpath(
                "//a[@data-testid='pagination-page-next']/@href"
            ).get()
            if link_next_page is not None:
                link_next_full = link_next_page
                print("-=" * 20)
                print(link_next_full)
                print("-=" * 20)
                yield scrapy.Request(url=link_next_full, callback=self.parse)
        except Exception as e:
            print("Chegamos na ultima pagina")
            driver.close()
            print("Erro:", e)

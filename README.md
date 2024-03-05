# Varredor_vagas
<div align="center">
    <pre>
      >>=============================================================================================<<
      || __     __                      _____          _           _ _              ____        _    ||
      || \ \   / __ _  __ _  __ _ ___  |_   __ __ __ _| |__   __ _| | |__   ___    | __ )  ___ | |_  ||
      ||  \ \ / / _` |/ _` |/ _` / __|   | || '__/ _` | '_ \ / _` | | '_ \ / _ \   |  _ \ / _ \| __| ||
      ||   \ V | (_| | (_| | (_| \__ \   | || | | (_| | |_) | (_| | | | | | (_) |  | |_) | (_) | |_  ||
      ||    \_/ \__,_|\__, |\__,_|_______|_||_|  \__,_|_.__/ \__,_|_|_| |_|\_______|____/ \___/ \__| ||
      ||              |___/         |_____|                                   |_____|                ||
      >>=============================================================================================<<
    </pre>
  </div>


# 🧾Descrição 
+ Este repositório contém um script para varrer um site específico em busca de vagas de emprego. O script coleta e organiza informações sobre oportunidades disponíveis neste site, facilitando a busca por emprego para os candidatos interessados. Os usuários podem personalizar a busca de acordo com suas preferências e qualificações específicas.


# 📖 Bibliotecas usadas
- **Selenium**
  ```
  pip install selenium
  ```
- **Fake-UserAgent**
  ```
  pip install scrapy-fake-useragent
  ```
- **Scrapy**
  ```
  pip install scrapy
  ```
- **ScrapeOps Scrapy SDK**
  ```
  pip install scrapeops_scrapy_proxy_sdk
  ```
# ⚙️ Configurações
#### #1 ScrapeOps API Key:
 + Navegue ate o site [scrapeops](https://scrapeops.io/), crie uma conta gratuitamente e utilize:
    ```python
     Your Account API Key: 39b****-****-****-****-******216
    ```
 + Coloque sua Key no arquivo `settings.py` e 
    ```python
     SCRAPEOPS_API_KEY = 'YOUR_API_KEY'
    ```

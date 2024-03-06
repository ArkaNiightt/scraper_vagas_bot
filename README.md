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
#### #1 🔑 ScrapeOps API Key:
 + Navegue ate o site [scrapeops](https://scrapeops.io/), crie uma conta gratuitamente e utilize:
    ```python
    Your Account API Key: 39b****-****-****-****-******216
    ```
 + Coloque sua Key no arquivo `settings.py` e 
    ```python
    SCRAPEOPS_API_KEY = "YOUR_API_KEY"
    ```
#### #2 ⌨️ Configuraçao dos arquivos:
 + `settings.py`
    ```python
    ROBOTSTXT_OBEY = False
    DOWNLOAD_DELAY = 3
    DOWNLOADER_MIDDLEWARES = {
        "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
        "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
        "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
        "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
    }
    FAKEUSERAGENT_PROVIDERS = [
        "scrapy_fake_useragent.providers.FakeUserAgentProvider",  # This is the first provider we'll try
        "scrapy_fake_useragent.providers.FakerProvider",  # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
        "scrapy_fake_useragent.providers.FixedUserAgentProvider",  # Fall back to USER_AGENT value
    ]
    
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    SCRAPEOPS_API_KEY = "YOUR_API_KEY"
    SCRAPEOPS_PROXY_ENABLED = True
    
    DOWNLOADER_MIDDLEWARES = {
        "scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk": 725,
    }
    ```
 + `varredor_vagas.py` escolha a vaga que deseja buscar
   ```python
    page = pesquisar_input_vaga("python") # <--- Substitua a string"python" se deseja buscar por outra vaga
   ```
#### #3 :rocket: Iniciando o bot varredor:
 + Com o terminal no diretorio do projeto, digite
   ```
    scrapy crawl vagabot -O vagas.csv (ou json, xml)
   ```
 + Depois que o bot varrer todas as paginas, criará um arquivo:
   
     <div align="left">
        <img src="https://img001.prntscr.com/file/img001/NNji6PlEQ_iC9ZF5FjD7mQ.jpeg" alt="Code" width="20%">
     </div>
+ Baixar
    ```
    git clone https://github.com/ArkaNiightt/scraper_vagas_bot.git
    ```

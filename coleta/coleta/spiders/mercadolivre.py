import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]

    ## Site que vai fazer o request: fonte original/macro da informação:
    start_urls = ["https://lista.mercadolivre.com.br/carros-usados#D[A:carros%20usados]"]


    ## Configurações do parse ficam abaixo: 
    def parse(self, response):
      
     products = response.css('div.ui-search-result__content') 
    
     for el in products:
      yield { 
        'title': el.css('div.ui-search-item__group.ui-search-item__group--title').css('h2.ui-search-item__title::text').get(),
        'label': el.css('label.ui-search-styled-label.ui-search-item__highlight-label__text::text').get()
      }
        

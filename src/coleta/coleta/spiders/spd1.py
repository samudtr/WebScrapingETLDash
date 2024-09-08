import scrapy
import time

class MercadolivreSpider(scrapy.Spider):
  name = "mercadolivre"
  allowed_domains = ["lista.mercadolivre.com.br"]
  page_count = 1
  max_pages = 100

  ## Site que vai fazer o request: fonte original/macro da informação:
  start_urls = ["https://lista.mercadolivre.com.br/carros-usados#D[A:carros%20usados]"]


  ## Configurações do parse ficam abaixo: 
  def parse(self, response):
      
    products = response.css('div.ui-search-result__content') 
     
    for el in products:
      yield { 
        'title': el.css('div.ui-search-item__group.ui-search-item__group--title').css('h2.ui-search-item__title::text').get(),
        'label': el.css('label.ui-search-styled-label.ui-search-item__highlight-label__text::text').get(),
        'year' : el.css('li.ui-search-card-attributes__attribute::text').getall()[0],
        'km' : el.css('li.ui-search-card-attributes__attribute::text').getall()[1],
        'price' : el.css('span.andes-money-amount__fraction::text').get(),
        'location' : el.css('span.ui-search-item__group__element.ui-search-item__location::text').get()
      }


    if self.page_count < self.max_pages:
      next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
      if next_page:
       self.page_count = self.page_count + 1
       time.sleep(2)
       yield scrapy.Request(url=next_page, callback=self.parse)   

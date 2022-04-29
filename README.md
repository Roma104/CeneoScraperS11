# CeneoScraperS11

## Struktura opinii w serwisie [Ceneo.pl](https:///www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|string|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|14133566|string|
|autor opinii|span.user-post__author-name|author|Maria|string|
|rekomendacje|span.user-post__author-recomendation  > em|recomendation|Polecam|string|
|liczba gwiazdek|span.user-post__score-count|stars|5/5|string|
|treść opinii|div.user-post__text|content|Lodówka amica jest warta zakupu|string|
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item |pros|list|
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|conts|list|
|dla ilu osób przydatna|span[id^="votes-yes"]|useful|string|
|dla ilu osób nieprzydatna|span[id^="votes-no"]|useless|string|
|dla wystawienia mopinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date|string|
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|string|
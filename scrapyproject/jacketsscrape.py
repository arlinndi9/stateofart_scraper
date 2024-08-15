import requests
from bs4 import BeautifulSoup

def scrapers():
    url = f'https://www.stateofart.com/en/clothing/jackets'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.select('.products-grid .product-item')

    for i in products:
        name_tag = i.select_one('.product-item-link')
        if name_tag:
            product_name = name_tag.get_text(strip=True)
        else:
            product_name = 'not found'
        product_url = name_tag['href'] if name_tag else None
        price_tag = i.select_one('.price-wrapper .price')
        product_price = price_tag.get_text(strip=True) if price_tag else None
        sizes = []
        for size in soup.find_all('div', class_='swatch-option text'):
            size_name = size.get('option-label', 'Size label not found')
            sizes.append({'size': size_name})
        image_tag = i.select_one('.product-image-photo')
        image_url = image_tag.get('data-src') or image_tag.get('src') if image_tag else None
        alternative_colors = []
        for color in i.find_all('li', class_='alternative-color-item'):
            color_img = color.find('img')
            if color_img:
                color_name = color_img['alt']
                alternative_colors.append({'color_name': color_name})
        print(f"productname: {product_name}")
        print(f"producturl: {product_url}")
        print(f"price: {product_price}")
        print(f"sizes: {sizes}")
        print(f"imageurl: {image_url}")
        print(f"color: {color_name}")

scrapers()
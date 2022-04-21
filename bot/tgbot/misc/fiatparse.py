import aiohttp
from bs4 import BeautifulSoup


async def fiat_parser():
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://www.kantor.pl/en')
        html = await response.text()
        soup = BeautifulSoup(html, features="html.parser")
        rates = soup.find('div', {'class': 'container-inner'})
        blocks = [block.text for block in rates.findAll('div',
            {'class': 'currency-block'})]
        data = [[
            block[:7],
            f'{block[7:23].replace(",",".")}',
            f'{block[26:32].replace(",",".")}',
            f'{block[36:].replace(",",".")}'
            ] for block in blocks[:-1]]
        return data



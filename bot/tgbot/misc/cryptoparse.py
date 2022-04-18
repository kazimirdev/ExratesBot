import aiohttp
from bs4 import BeautifulSoup

async def crypto_parser():
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://coinmarketcap.com/')
        html = await response.text()
        soup = BeautifulSoup(html, features="html.parser")


        table = soup.find('table', {'class':'h7vnx2-2 czTsgW cmc-table'})
        rates = [rate.text for rate in table.findAll('div',
            {'class': 'sc-131di3y-0 cLgOOr'})]
        names = [name.text for name in table.findAll('p',
            {'class': 'sc-1eb5slv-0 gGIpIK coin-item-symbol'})]
        result = dict(zip(names, rates))
        return result

import aiohttp
import lxml
import re

from bs4 import BeautifulSoup
   
    
async def specific_crypro_parser(currency: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://coinmarketcap.com/pl/currencies/{currency}/"
        response = await session.get(url.lower().replace(" ","-"))
        html = await response.text()
        soup = BeautifulSoup(html, features="lxml")
        if "something went wrong" in soup.text:
            return None
        else:
            table = soup.find('div', {'class': 'sc-16r8icm-0 nds9rn-0 dAxhCK'})
            keys = [
                    re.sub("<[^>]*>", 
                    " ",
                    str(t)).strip() for t in table.findAll("th")]
            values = [
                    re.sub("<[^>]*>",
                    " ",
                    str(t)).strip() for t in table.findAll("td")]
            for v in range(len(values)):
                if "     " in values[v]:
                    values[v] = values[v].split("     ")[0]
            
            table = [[keys[i], values[i]] for i in range(len(keys))]
            return table 


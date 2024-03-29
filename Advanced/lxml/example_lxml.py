from selenium import webdriver
from lxml import etree

class Listing:
    def __init__(self, listing_div):
        self.name = listing_div.find("./span/b").text
        self.wealth = int(listing_div.find("./p").text)

class PageWithListings:
    def __init__(self, page_source):
        self.tree = etree.HTML(page_source)

    def get_listings(self):
        locator = ".//div/span/.."
        divs = self.tree.findall(locator)
        return [Listing(div) for div in divs]
    
    def get_listings_descending(self):
        return sorted(self.get_listings(), key=lambda x: x.wealth, reverse=True)
    
    @property
    def highest_wealth(self):
        return self.get_listings_descending()[0]

if __name__ == "__main__":
    browser = webdriver.Chrome()
    browser.get("https://techstepacademy.com/trial-of-the-stones")
    html = browser.page_source

    listings_page = PageWithListings(html)

    highest_wealth_listing = listings_page.highest_wealth
    print(f"The listing with the highest wealth is: {highest_wealth_listing.name} with ${highest_wealth_listing.wealth}.")
    




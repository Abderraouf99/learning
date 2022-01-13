from bs4 import BeautifulSoup
import requests as http
import lxml
import smtplib

product_page = 'https://www.amazon.ca/Apple-MLWK3AM-A-New-AirPods/dp' \
               '/B09JQMJHXY?ref_=Oct_d_obs_d_680468011&pd_rd_w=C5v3V&pf_rd_p' \
               '=886d55ac-d17c-4912-a5af-948a0d840eec&pf_rd_r' \
               '=QF6QGM0CC2A6858XZ3BB&pd_rd_r=0c999879-8269-490a-816e' \
               '-2322299c31a1&pd_rd_wg=7XCdm&pd_rd_i=B09JQMJHXY '

device_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS "
                  "X 10.15; rv:95.0) Gecko/20100101 "
                  "Firefox/95.0",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3"
}
html_page = http.get(product_page, headers=device_header).text
bot_email_address = "abderraoufbenchoubanebot@gmail.com"
bot_email_password = "Vivemoi16!"
my_email_address = "abderraoufbenchoubane@gmail.com"
web_page_soup = BeautifulSoup(html_page, parser=lxml)
prices = web_page_soup.select(selector=".a-price .a-offscreen")
target_price = 250
if prices is not None:
    current_price = float(prices[0].getText().split("$")[1])
    if current_price <= target_price:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=bot_email_address,
                             password=bot_email_password)
            connection.sendmail(from_addr=bot_email_address,
                                to_addrs=my_email_address,
                                msg=f"Hello this is your amazon bot \n \n The "
                                    f"price of the product at"
                                    f" \t {product_page} has been discounted "
                                    f"below the target price of $"
                                    f"{target_price} \n Happy to serve my "
                                    f"human, Your faithful bot")

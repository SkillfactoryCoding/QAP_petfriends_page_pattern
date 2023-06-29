import os,pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends.skillfactory.ru/'
        super().__init__(web_driver, url)


        with open('my_cookies.txt', 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             web_driver.add_cookie(cookie)
         web_driver.refresh()

    # Main search field
    search = WebElement(id='header-search')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')
    #Last pet element:
    last_pet = WebElement(xpath="//img[contains(@src,'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADJAPsDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzaH/WVoxfP8lOsLGK6sbjYjfaoMP97h07jHqMZp8UaeWju+3d8q/7R7/TqK8SrTdrnC9CeNak2J5lORPJ+d/ml/hVv4fw9f8AP0dcH5/95QzfXv8A4/jXI2Nu5Iw/cbKyXhXzK27aSL7DLE+/7y7tv8XBOP1FOt4rGaO4T7JulVRt3SN6+x5ro5U9tyVLoZwbZHTITWjf6dcQ2txcW9pLKiqdsca72zzhSAMg/hXm6x6n/wAff2iVZWbd94/yreGFnO/tNPkbUabqJtHpVu/7yrcn3K5fw5rP9p7re42LdR/+Pj1Fdht/cVilKlUaZMoO9mYF1v8AMfZVNrZ3j+et9rb+Osy/mSGnJsnl0KSxbPuVoWkG/wC/VaxV7n59lbUUez79JpWIUR7W/wC7+Ssq4l2ffrfiKP8AcqrfWKff2VDhdXRTRzxllenrV4QolI8SVyylrYlophqcJKJFShIqtRVtQSFLUjR0/bsppkqG+xTYJBUqwU6Ft9TrS1ZSaK22pYp9lOcVWeiE3FktGvDPVgHfWJDNWlBLXpxxKktSLFvyqDFU8Ku9XPs2+q9jfVFozFhp/wBnetaOyqf7FXbTw+homef6eYoZ/wCLft3N0xtxkj69PyNZk42eUn91j+eSP6CrUf8Ar3f+Ns7vx606OyuJkTei71YLu3D5skAY9e3T+teV7XmVn0MWuZaEzF3kf/eP55qRrN5p/kdV6L+QAyMc0y/m+xXbp5TROv8AeXB59u3+elUzdO/8fy/3e1c3K0aRSSdzcWyTyE8n966x/vG3AA4JORjPYgde1U1P2b54vldmHzf3cen60y2ubh40i81ti5VV6daLn/V113ajuF1e6Ra+0S/O/wBobZLJvbzJcFDnJIPGep4OaxdfuYnnfykWVNqszKy/MxUE9OOpwfp71U8QN/olrvfb/pG78dpxTdLXzvNhl27PvfM3+ea7MPC6VRnoYSO77nOPO+n30V7bv80bbl/qpHb6V6xYahFqem293F9yRQ3+6e4P0Nec6zZxQyM9vsZNv7yPdyR/noat+DNSe2vv7M374pmzB/vHtj3x09QavFU3OnzLdE1oanfy1g3lrvn+etyXekmx/lf8qo3J2fPXlzk2cOzY60jRI6dNvf7lVraV5pNlbsFonl1pBJrUjUrWIdJNlM1vU7TTIEe7l+dv9XGvLP8AQVW1vX4tCjdItst6y/u4+y9tx9Bk/jg1yWnQy3t893dv59w33pG/kPQe1dWHo6Xex00MO6r12JLnxVcJ+9TR/wB1/eZ+cfQcCtlblbm0iuIvuyKHX8aTWbOJNCll2L90/wCRUGkI/wDY1kn92Ff1Gf61ljIwjC6WtzbF4eNJKwpb95UwapGiSq5XZXnX5kcI6U1XqVvnqNV+emo2C1yzBHVoVHFHUpNbwp3Ieg2VqqO1SStVasakLMd7k8a1r6daO/36p2UW+Sun0+2rbC0+eVzVIvWlnWmlr/sVLaQVpRx178I2Q1EoR2dWPsVaEcdT7K2RaR4HEn+f5U46hF+9SV9vlY27eqkdAPoR1z3pJ75Id7p99VKr/sHoPq1c+d7/AH6+ahRursy+E29c1r+1r7zdi/KoXcq4LcDqe+KSws/O+d6wkTZP9+umtrjybSurkTd2S2PlVIfuURR+d/wKqRuHmd63dJaJ4/n++v8A49WdNp1GXThzSscj45iW1t9Nh3/xM+36ADP61lRX6OiPv2uyj5dw/nU/ja+a61WJF+aKJSvp1IyM/hWXaWP2nytjpsX/AGu2ec/T+pr1oRtFHpL92+VGhdql1G/99V3fnWGjSw7trtHcQMJY2XsQQTj9GH0PrXoFjoaQwfcVopf4e6HHVfY9/rVSfw4nmea6btyr/wACA7fiOKoJK50/hLx7pXiKS3tPENp/xMJWKfaY22hscgn3r0EeG/C1zHLvllX+Ff3n3fcV4AlgmmTxOifvVk+Zv+BE8fhW9J4ku0kT97tT+H5vXgVk8PGWtgtD7aPSG8G6fDJ9oTWIlt/+mi42gVy/i3xR4f0S0e00u6lvNQX+JceX759AK47VNUl1b7PaPKy/LuaPdx7j8QawU0i4tpmDpux8x3dDgnA/HAJ9gaiOFgtyZQh0RoWNtLez+bcS7pZW3zSN1z2H4A/r7V2lvpkVrY/aEdV2/MzbuG/CsOxSW2gi812+b+Hy+c+pwa1YrtJt6PtVNu3sPxPtxW77HXRSijO1W+l1C0liTdvuWCRr9SAP1rqxYpawIn91Qv5DFc3ZjzvFFrsT/R1Yvu6hsKcAH64P4V0V9eO/yb64sRZWRwY6pzSS7FWRf3nyUhtd8fz0yEv5lXjKlcvsOpwpoy3t9lRrFVyZ99Mjj/eVjtKzGxqmopjVh1qnP/rK7LpIxepEWpwFPjgd6uR6e71nUpuqtEUkSWJrqNPNYdvYOlbVnE6VeEo1Kb1RsnodLayVpxisi131qRF69ZFplpafuqJd9Sbaso+efEur2+oas728W3a3zNu4c45O3t9c1TgkR6yJl/f/ACVr2cPkx/PXkwhZJowmrjrqDZHv2fPTYL3+DfUdxeb/AJKoSrSnq7E2sjrLREmj2V0OihLaCV32ttU/eQ5+ma5Xwz5s06Rfe/h/ya9Nv7JNP8P7H2b5fvbVAGPwHNRTV5M7MJC8rnz9d2txq2s3Euxm3SHc2046+1dPoeieTJsl/wC+dwP05H/6/UdMWtSWJJH2bVf+8qgVmRa19ik2fwf3q9SLudLSTO6jaKGP/b3VSubtJo9if5+n5Vzg1uW92JYxSyu3y7Y0J5rNvWvtM3vKk8D/AN2Tpz9CQKq2grpMl1W+R53/ANnDf7xBOR+QrPe4S5S3f+9978MEfzFYoum3yu38X/16kiudnlf7PzVUTOTOkszb/wBpP/Ftx83+frXe2GmW918/y/Mo/P8Az/OvIre+2Oz/AMX+cZ/z2rtNB8TP9kT/AJ6/d/z6VL1NIs76bRYngdP4G/2c/wD664nWbSLTLuV4kZnZf4sYX8R+X9TXfadqsN1aJ86//X9q5PxVo9xe/vU3bPvKsfX8OQP1pWL5mZ/hJnvbu6l8r5II9ny+px/IA8+9bfkfvPnrN+Hb/Yk1L7REkflNuaPjcw/Dita5u0mnd0Tan92uapC8jixdtHfUh+5SY31IkW+rSWD+X9yhUWzjijMYfvKsxpWgmlv/AHKsxae/9yolhbmjMl4arfZv3ldA+nvTo9MenHDi5TOs7KuhttOSpbWw2bK3ba2rrhTsUkUItMT+5VpNNStaO3qwlvWySL5TPhs9lXY4KsLDUyx0wsRLBUn2epVWpMUFHyQ6f6WlWr+bZAmyocb9lV9SbZsryKeqSM0SxbKmng/d70rFS42SV1Wixf2h8lVJdyXG70Nz4faRLqF9/wBMl+91Fdf42uvJ/dI/ybdv5VueFbBNJ0Z7h0+f/P51yniXfdSP89VTp217np4ZcsTzi7m/eO+9fm/OucvZdknyV099H5Mbv/j/AFrktQO+T+GuqITR1PgPVbSy1lPtD7UZWTd/dyB/UD9a7m5s0mjvXu3s5bRlCxttHTGSc56814lE2z/2Vq0k1O48vZ5u7+ddcKnKrHFOnzO9zP1KFLa/uIov9VvOz/dzxTIlxA7U+/uJbqfzZtu77vy+gqW0ZSnlVkjVkVlaXF7dxW9um+WVgir7npXqOmeAIrKe1tLjU1+0Sxs21WAC469ee/8A+quF0K4XSb97j596r+72/wALAjJP+e5r0F/iFYv5VxLaL9riUqrb+OcZ4xx0961pKH2zGs6unsytqBl8J6k9vNfLcpuG1o17Fc8+46cVo22qf2tH9z7v+zXBanrcural9of77MW9vTp9AB+FdPoO+HY+z5GX5q56luh3UW3ozo9P8KpDHcX1p/y1jO5atWmiu+z5K6HwxL5MiI/3P4u4rqptFRJPNiT903zVNNq+pliqN2mjj7XQv9itWLSP9it6Kz2fwVL5NdN0cigYA01P7lDWNbjw1F5FQ7FqBgvaJT4bb/YrUe3pyW1SDiRQWlX4rehI6spVoOUBFUgWlBp4pjGgU4UtKKAAVJmkopAfJFpL+8pmqMj/AHP7tLFb/u99U3/1nz15fJarcxUtLGeEfz9leheErbZJEm/c7Y9wuf51xJTfJXpvgRUS+t0dJW+YfKvVv8K1qK7SKi9T1maL7NoUUX+z81cFq9o91v2f416Fq0v7hP4fl+7/APXrkZmd/wCP+da2PQTsjyjVbK7Sd4tnyf7Tbf5mududPd5PuL/39T/GvZLvSftPzvF/302Py55rEu9FSH777U/3nz+Qx/M1VrA3c8om0u4T/lk36kfnUQLp99Ntd/f6Yjx/62dv4l/d4/Lklq5TUrN03/7P8O0jb+daRkZSiZJi+0yJEn97n/ZFblroTvIlujr9373uawijv/suv92rVvf3f3PtDK6qNv8AXNXdEWZLFE0JXzf9arMsn1zg/wAv0olX/vinB3mnfe/mys25mbqxPWtqz0fzvvyqqL97cp/mAf1pNjSbMu0h+49d/pFtvtE2Ju/4EawzoP7v5HRv7u3j88103h+zvn2Js+T+JuD+o4rGTudVNWOq0W2uEkR/m/76z+depaaPOsVV/vVyOk2USRp/C9dlpq7I9lTFCqy0CWKofIStIimmJaqzMk11MwxIlR/JV6aKqE+xPkSs3c2jYiYpUDSf3Kjk3vUkUOypuzS0ewCSplNMIqQMiU1ORLpwJFNPBqDzUp0Um+tVUfUylQXQmBpwpU2PUvlVoppmEoNDAaM00x02ruRY+Q7a/wB6bKglbZUWn2zzT7/4K0L2y+5srjcVe5ztakml2jzSeb/Av867zwHK/wDbqb02pu2q241zdiIra0SL+Nq39BV4dZt/Kf8Aet8q9cL74BFZU5OUm2VHRnr+rGuWmfZ9/wDvfd/xrqbuJ0gTe+59vzN0/Suemt/tMnyI38j+J7V2WOu5Wjld9/8An86rXESJHvetQWvkx/Im39aPLR/v/N/vL978KLD5jh7xXff5SbUb82/z71x+s29wn8DMn+cda9cu9P3/AOz/ADrCudMf538r5P8AaWpaaNU0zySPS5Zv4Nu6mSaTLbSbN+7/ABrvb/Sf49+3d/eqK20y0SRPtb7vl+79ACannH7MwNG07zpE+Rm/2voefrXe2Nh9lg+R9z/3d33foRzj6c/Ws2xG+TZaIqorfK1dfpVg/mI7/K7fd9M9x9P61SbYNKKCx0iKb79uq/l/Mdfx5966C30mK1+dEqzDEiRpsT/gP+H+f/rWYQ/mfJ9ynYnmZZtIdkldLZj93WRaQpW1B8lNIykxPM/eU7zarzjZJQrpVEkrfPVC6hq7mmOKhouMrGQAnmfPQ7f3KS/+T+PbWZ9rT7ifNWbR0J3LpV/vu9NRnf8Agquk2+rUUu+lYq5aihqXZUkcieXUsY3yVSRm5EHkS/fSrMTP/HV2Mfu6jktv7lXymfOChHpnkVDu2SVN51NNolpM+PllSyj+T79Wov8AV+dcf/s1VghR/wDS5fuL92qN5qDzSfJ9xa5eZyfKvmcnL1NazuN93vf7n8NegeEoHfWbd9it825t38/avJ47h/k2V2vhrULjzER3aLbjd2LHsPfH86vk1uNbnuF5Oj/x1Qazi+/9oZX/ANmqynfYxfeX5fx/E0yKB/vvcN/wFvu/410xZuy8YpYfufMn+1/hSwbHd/4adFBFN992b/gWP5VL9jiT/Vff/wA9zVWFcRoE++6Uz7Ak0D70Wllgl8xN77UVvm2/p+FWVb938/y/59aQznV0W3vYN/8AdYq3pwfSq83hq38zZ5S/d3V0kT7J9iJ8m3csi+vfg9qF2TT/ADv5UqrtVfYHvUcqL5mc7b6JFD8iJt/3eK0hpj/I6PtdfyrXYp86OirTLMyzRuj7di/Lu/vCiwczJLe2dPv/AH/97+VakNv/ALFRwwW8PyJ9+rPnVVrEt3JIY9lXENU0bfVj7lAiWYVWVqsJJUFxH/HSLJAKjkqvDd/wVcWTfQTaxj38W+ufkj2SV113Gnl1zd5vST5NtS0bxkRxzolWEl/jqhl/7n/j1SR+b/crOxobcM6VqwS1gQitG2arRnM24zU9UI22Vbil31oc7I5Yap7XrVqu0HzGlYaZ8aXbPNH9nT7i/erLvoHhrp7XSXupE3v5VdLb+B7fUNn75m2/lWEZJuyM4q6OC0jT7u9kTyoWb+XtXpfhXwgllIlxd/M/3vm9a39O0m30mNE+z/8AAttdJHbedHXVFIOWws0KPY70/h/vVkfaJfM+RGZK6GS32Wnz1jBkeTY77U/2ajdmjVkTQ3m/5ERlf+Jv7taA3wxpsf8A3qrhYtnyJtp8S1diLl+OXzpP7yLVnZE/yfLWfGz/APAKJmdI/wB1TGPuw8Mb+Vt/vLu5+oH4ZqrDN+83/ef7rN2UfWrj3G+D97/n61lZ/wBL8re33fvK33vrWbLRvpDF5bv952/8eqW3TZH8/wDFWZBc/wAH+zU0dw81O4rGoQnmfcqxEUqnD8n33pzTbJKYi8zIlMa4/wBuqb3FV/P/AHm//wBmqWylE3ElqRWR/krKSbf9+pUuNklIdiO9iSGTfSQ3NXJgk0FYCy7JNn/16TLWpvbt8dY+oW7/AH0SrVvcVNMqPHTTC1jl2ldPvw/980onSn3i7J/4f+BLg1WX79S0WmaMUj1o28tZkNaFsUoSFJmqkm+rNvLseqW5EjqP7ciVoc5tian+elYDX3+3TP7R/wBui6Hys8k0bwt+8R7h9z/57V18dnLDGiW6KqVTt1Tz9/8A3ztrTNw8NOFONNWiZociI8bo6VFpsUtlffZ/vRN8y/7NSfa3mj+TbvrQhb9w7un8NE+5cY3ZX1e52QOifNtrj479EneJ3+f/ADxmpvEGrW9lG7vuZ2/h6V5jqniqbz9kSMz7vuq3T/69c6d2dMlZanqsepp9zfWxb3qeWiV4vZePLeF9twjbv4mXkfnXX6V4o0/UP+Pe7iZ/7u7B/I10pnM4o9PikR40qTaj1zNpev8A360Y7mWqIsXZ7T93vhf/AOyrMk0/ZOiJ8u773+zVyGZ/7/8AnNNnuP3if57VDSNItkVtZfv9+/5Oa1BsT7lVLWVP4P8AOKdJP+8+/wDd+9/n86EhN3LDz/1pslwn8b/PWNca5FD/AMB+9XOXfiiJ5H2P86/w0mXFXOxkvE/v/wDAqptq9vD/AMtVrzi/8Uu8jp5v/AaybjW3+TzfuN96sXLsdCh3PXB4ht3+Tzd1Wo9Uim+RK8SEzvJvilZf7vzZrT0vXru1u0ilfd/tdqnmZpyRPcLLUH+471DqSIknmp9xv51iaDfJcwVs3fz2jo/+8tUncyasyOCatGCeuXtrnZJs3t/wKte3uf8AbqkxNF29tkmSsYjZ8nzVuLNvjqjcBPM+er3IvYrgf3Kmh3pJ/sVWaZEqaO7R4/v0JEtlqS+T+/8AOtZt7qf9x6y7y+/ePWTcXafJ89Eioo3kvpad9olrLhuf3e+pPtD1Ni7kKq8PyJ8zr/ng1din+55u3e38NUBKif7XX/69Vjfp/rdjM+7aq9Dj154rpaORMuzRfvN/zf7O1vu1es7jZ8nms3+81ZEk/wDzyf52Xcqr1Yf0qN1lSPen3/yrKSujSLszjvGs8qX0v3m/ur0FcItjcTb3RPvfek/wPp9K7vxJqMX2tIni8+7/AIV3fd+prk9W1O4T/R/s6qir91W4/wDr1hBNaG82nqZTWEUP333PUkKonzxOyuvzKytgqaihne5k2JtV/wCFWwM/Q1E0r+Zs/j/3f8/yrSxldHp3hXxJM8n2e7fdKq/K398Dv9fWu8tr/fHvf+9XgmnzukiXCfLtb+XUH6ivUrG5d402P8nH/wBariyJI7cXKeW+96pT3H7jf93c3y/lWe8+/f8A7oovLxIYPn+/VNCRbstaiSD5327fvbvrWDrPjLyZHitH3St825v4etcPr2tPNqz2lo7bFx5jL/e7/Xrj/PFKKf7L8/8AHz97n+VS3YtK5ui8uJv3t3cfJ/d3Vnahq++PZFuX9T+lVp7x5o0T7qfe9P51n3R//Z61la+5tzWWhHNd/vN+/wCfbtqJb3f/AH/7u3jHFRStUO393/wL+fSqsRc3bGT78X/Al/8A1V0djCj7H/u/xLWFpFm82z/d/GussIvssib/ALn+etZNam8XodXo9z9ikT+41dHLqf7h0/jX+Fv6GuPMqJs/uf8AoP8A9apIi97JsfdspoUjWt5XuZ9iJ/hXQ2lm/wDcqtpVtFDGiV0MLJ/BWiiZSn2IBA6R1m3srw/3q6HelUbm2eb7j1aRjzHFT6onmffqpLqv39j11Mvh2KaTfKnz01PDVv5n3F/75qlETmjgLjUN8n8VZ817/cRmr1F9At0+/Erbv9mnp4etE+fyl/75o5B+2PM7PVJU+R0bZ/u1P/aUv9xv++TXpH9iW/8AzyX/AL5FS/2Tb/8APJf++aFBC9qzjVt/91vzH9elTiLZB86L/vcZx+dOWOL/AGd/93zD/KhIv7+3f/dXOOw4z9K0M0wC/u3+f/Cs6WF/L2Sv97+7lR785yT9KnnWW9n2W8u3a22STb932Udz/tdB9eivpEX/ACyi3O33pJG3M3tk8ge3Sk0NM8g8Qah9i8SXD+V86tt/DoD+VYd3c75/3v71OP4sFq9E8WeCNT1O7+0Wlou9cbvmADDsPqK5O48CeI02+VpUrL/F86de/f1rJRaNJTTMSHYl38nzJu+XdgH8fQ06QbJP9S2z/e7+1dHD8PteeT/j08p2b92sjqN3GeME5710Vp8NdYeD/Tkg/u7l3FsfgKfKxcyOQ0yyd5H2fxLtX0ya67RbfULKBEfayKoX73pXWaX4Ht7KPyn+Z1+98x79M8+1b8Ph6JI9mz/x41pGFiJTTOQZrh5EfZ8n93d7dqoanJfXsbpEjK6tt3bfbqD0NejLoaf3KeNFh/ufd+nvTaEpHz7JoGp6Zvd7eWVNx+ZVyfxqAXf7zY6Mr/7WR+nWvolfD1v5m/Ztf+9UNx4P0y6+SW3ib/eUf4VDplKpY+fJb1P79RNMj/PXvM3wy8P3P3tPi/4CoFUm+Dfhzfv8qdf9nzWxS9mP2x4c+x4/kf8A/VVy2ton+/8A3t34CvbIvg74cT/l3l/4FKf8a1LT4caDbSfubGDf935lDfnmjkBVEeSabv8ALdIkdnVvl2qTXR22gate/ci2p/004r0+Hw6kP/Hu8UX+6gq1HYXaf8vETf8AAP8A6/0qfZov6wzjrHwnceWiXFwv/Af8a3LPw3Fbfcdm/Ot4Wj/f3pUwgqkkiXNvqZiafs/2f91alS3dPvyt/wACWtD7PQYKZOpVAf8Av7qlTf5f/wATUqw09Yn8ygkYC/l/cqCeXyfnf5U/vbT/AEFXJC6bPk/8dPb8OPxpm7/vv/a/OgCJYkfY/wB7+7+NK67Pv0/Df3KaN/z7/m/kvA4Hrzn86YAsO+T5Ks+Q/wDcWi3nRPk8pt/4VZ3f7H/jy/40gPL1iRNib1837u3rt9z7VOkKfxuzP+X6Vm6b/wAg1P8AdFbMf8FaCFSJP8sf5Uog+5sRf9r6fX1pzffq7H/q6gZXW3/2/wCdSpaJ/tf8BqQ/+y1JDTuKxH9iT+/L/wB9Uq2X/TWWpov9Z/wKrC/6v/gNO4rFVbJ/L/1rLUzWb+X8j7X/ABP86tR/6v8AKp0oGZos5f79OFtcf89f/HR/KtJv9ZTH/wDZhQBSMFx5f+t/8dp6RXFaB/joP8dAinsuKXdKn/7Jqyf9ZQKAIM3D/wB3+VPXzalk/wBWlNFSMgy7/wB2lg3wxoiIsSKo2qq8KBwBjtxTYv4/x/nVhv8AV0DE3PTwz/3KQ0i/x0gJfO2fwU9pv49jVCf4KeP9WlADllR/nTd/wJSP0NLGyJ/e/wCBU0U80AJLN/3xUEkbzbE+6m75t38Q9APrjrTb7/j0f/eX/wBCFW6AGfIkdWbWL93vf77fw/3f/r1Rn++n+9UhoAvFUpvkxf3F/wC+RTIqfQB//9k=')]")
    screenshot = ManyWebElements()

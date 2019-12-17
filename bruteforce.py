import requests
import json
from collections import Counter
from colorama import init, Fore, Back, Style
# You must enter your resourceID in the code to make it work
# To find the resource ID you have to click on the frosty keypad and get the ID from the URL
start = 0
end = 99999
for num in range(start, end + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            # If the number is not a prime number
            if (num % i) == 0:
                break
        else:
            c = Counter(str(num))
            if any(value > 1 for value in c.values()):
                request_response = send_request(num)
                if not request_response["success"]:
                    #If the code is not valid
                    print(Fore.RED + "Check: ", request_response["success"], " - Checked number: ", str(num),
                          " - Response: ", request_response["message"])
                else:
                    #If the code is valid
                    print(Fore.GREEN + "Check: ", request_response["success"], "- Checked number: ", str(num),
                          " - Response: ", request_response["message"])
                    break
            else:
                print(Fore.YELLOW + "Not a prime number", num)


    def send_request(number):
        r = requests.get(
            "https://keypad.elfu.org/checkpass.php?i=" + str(num) + '&resourceId=RESOURCE ID HERE')
        data = r.json()
        return data

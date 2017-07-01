import json
import requests

def findcard(args):
    print(args)
    url = "https://api.gwentapi.com/v0/cards?name="+args[0]
    #print(url)
    r = requests.get(url, verify=True)
    if(r.status_code == 200):
        jdata = r.json()
    else:
        print("Status code = " + str(r.status_code))
        return str("Sorry! That didnt work BibleThump")

    if jdata["count"] == 0:
        return str("No results found BibleThump")

    results = jdata["results"]
    print(results)
    response = ""
    if jdata["count"] <= 3:
        for x in range(0,jdata["count"]):
            card_url = results[x]["href"]
            print(card_url)
            r2 = requests.get(card_url, verify=True)
            if r2.status_code == 200:
                card_json = r2.json()
                if 'positions' in card_json and len(card_json["positions"]) == 3:
                    card_json["positions"][0] = "Agile"
                if 'strength' in card_json and 'positions' in card_json:
                    response += (card_json["name"].encode("ascii", "ignore")) + " - " + (card_json["group"]["name"].encode("ascii", "ignore")) + " - " + (card_json["faction"]["name"].encode("ascii", "ignore")) + " | Str:" + str(card_json["strength"]).encode("ascii", "ignore") +  " - " + (card_json["positions"][0].encode("ascii", "ignore"))+ " | " + (card_json["info"].encode("ascii", "ignore"))
                else:
                    response += (card_json["name"].encode("ascii", "ignore")) + " - " + (card_json["group"]["name"].encode("ascii", "ignore")) + " - " + (card_json["faction"]["name"].encode("ascii", "ignore")) + " | " + (card_json["info"].encode("ascii", "ignore"))
                #response.encode('ascii', 'ignore')
                response += " :) "
            else:
                print("Status code = " + str(r2.status_code))
                return str("Sorry its broken BibleThump")
        return response
    else:
        return str("Sorry! Too many responses. Try narrowing the search")

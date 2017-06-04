'''
EECS 349 Project
Script used for obtaining the number of likes of directors and actors on facebook pages to use as a feature instead of their names. 
'''


import json
import csv
import requests

app_id = ""
app_secret = ""
access_token = app_id + "|" + app_secret

def countFacebookLike(name, access_token):
    base = "https://graph.facebook.com/v2.9"
    node = "/search?type=page&q={}&type=page&fields=fan_count".format(name)
    parameters = "&limit={}&access_token={}".format(100, access_token)
    base_url = base + node + parameters
    #print base_url
    r = requests.request("GET", base_url)
    data = r.json()['data']
    #print status
    if len(data) <= 0 or not "fan_count" in data[0]:
        print ("failed")
        return -1
    like = data[0]["fan_count"]
    print ("like = {}".format(like))
    return like

def scrapeFacebookPageFeedStatus(name_list, access_token):

    with open('actor3_likes1.csv', 'w') as file:
        w = csv.writer(file)
        w.writerow(["actor3_name","actor3_likes"])
        count = 1
        for name in name_list:
            count = count + 1
            if len(name) == 0:
                w.writerow([-1, -1])
                continue
            print("Scraping likes of {} count = {}".format(name[0], count))
            like = countFacebookLike(name[0], access_token)
            w.writerow([name[0], like])


if __name__ == '__main__':
    #read the list of names from csv into name_list
    with open('actor_3.csv', 'rU') as file:
        reader = csv.reader(file)
        name_list = list(reader)
    #find the page id
    scrapeFacebookPageFeedStatus(name_list, access_token)

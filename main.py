import os
import nltk
import webbrowser
import time
import json
import random
import pyautogui
from datetime import datetime

number_of_search = 0

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_directory, "config.json")

# Function to create a new configuration file
def create_new(config_path):
    current_datetime = datetime.now()
    date_only = current_datetime.date()
    data = {
        "last_run": str(date_only)
    }
    with open(config_path, "w+") as json_file:
        json.dump(data, json_file, indent=4)

# Function to perform a web search
def search():
    global number_of_search
    nltk.download("words")
    from nltk.corpus import words
    english_words = words.words()
    # Generate a random meaningful word
    query = random.choice(english_words)
    url = 'https://www.bing.com/search?q=' + query
    webbrowser.get('edge').open(url)

# Main script function
def script():
    global number_of_search
    edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    number_of_search = int(input("Enter Number of Searches: "))
    for _ in range(1, number_of_search + 1):
        search()
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(3)

# Check if the config file exists
if os.path.exists(config_path):
    with open(config_path, "r") as json_file:
        data = json.load(json_file)
    current_datetime = datetime.now()
    date = current_datetime.date()
    if str(date) == data["last_run"]:
        check = input("Script already ran today. Do you want to run it again? ")
        if check.lower() == "y" or check.lower() == "yes":
            script()
            create_new(config_path)
    else:
        script()
        create_new(config_path)
else:
    create_new(config_path)
    script()

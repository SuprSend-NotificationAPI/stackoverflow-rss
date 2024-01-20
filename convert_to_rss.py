import requests

# Replace the API URL with the actual Stack Exchange API URL
api_url = "https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=activity&q=smtp%20451&site=stackoverflow"
response = requests.get(api_url)
json_data = response.json()

import xml.etree.ElementTree as ET
import requests

def convert_to_rss(json_data):
    # Create the root element for the RSS feed
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    # Loop through each item in the JSON data
    for item in json_data["items"]:
        # Create an item element for each question
        rss_item = ET.SubElement(channel, "item")

        # Extract and add relevant information to the RSS item
        title = ET.SubElement(rss_item, "title")
        title.text = item.get("title", "")

        link = ET.SubElement(rss_item, "link")
        link.text = item.get("link", "")

        # Check if the "body" key exists before accessing it
        if "body" in item:
            description = ET.SubElement(rss_item, "description")
            description.text = item["body"]

    # Create an ElementTree object and convert it to a string
    tree = ET.ElementTree(rss)
    xml_str = ET.tostring(rss, encoding="utf-8").decode("utf-8")

    return xml_str

# Convert JSON data to RSS
rss_feed = convert_to_rss(json_data)

# Print or save the RSS feed
print(rss_feed)

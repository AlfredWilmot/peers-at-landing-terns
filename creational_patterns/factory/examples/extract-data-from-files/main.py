import parsing_human_readable_files as parse

def main():

    # Read *.sq3 file, dispay info
    sqlite_factory = parse.extract_data_from('./parsing_human_readable_files/sample.sq3')
    print()

    # Read *.json file, display info
    json_factory = parse.extract_data_from('./parsing_human_readable_files/sample.json')
    json_data    = json_factory.parsed_data

    print("JSON feed...")

    date = ""
    output_str = ""

    # iterate through each news item
    for story in json_data["items"]:

        # catpure the date and title of the news item
        current_date = story['date_published'].split('T')[0]
        title = story['title']

        # Only print the news item's date if it is different from the previous item's date
        if date != current_date:
            date = current_date
            output_str += f'\n{date:_^100}\n'

        output_str += f'>> {title}\n'

    print(output_str)


    # Read *.xml file, print info
    xml_factory = parse.extract_data_from('./parsing_human_readable_files/sample.xml')
    xml_data    = xml_factory.parsed_data

    print("RSS feed (XML)...")

    print(xml_data['rss']['channel'].keys())
    stories = xml_data['rss']['channel']['item']

    for item in stories:
        print(item.keys())
        break

if __name__ == "__main__":
    main()

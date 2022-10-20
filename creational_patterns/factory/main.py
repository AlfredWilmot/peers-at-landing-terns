import parsing_human_readable_files as parse

def main():

    # Read *.sq3 file, dispay info
    sqlite_factory = parse.extract_data_from('./parsing_human_readable_files/sample.sq3')
    print()

    # Read *.json file, display info
    json_factory = parse.extract_data_from('./parsing_human_readable_files/sample.json')
    json_data = json_factory.parsed_data

    print("JSON feed...")

    date = ""
    output_str = ""

    for story in json_data["items"]:
        current_date = story['date_published'].split('T')[0]
        title = story['title']

        if date != current_date:
            date = current_date
            output_str += f'\n{date:_^100}\n'

        output_str += f'>> {title}\n'

    print(output_str)





if __name__ == "__main__":
    main()

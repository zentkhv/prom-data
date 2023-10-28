import pandas
import json


def process_dict(input_dict):
    formatted_data = []
    for element in input_dict:
        tags = []
        for tag in element["metric"]:
            tags.append(element["metric"][tag])
        tags.append(element['value'][1])
        formatted_data.append(tags)
    return formatted_data


if __name__ == "__main__":
    with open("data.json", 'r') as json_file:
        data = json.load(json_file)
        # data = json.dumps(data)  # Переводит в <class 'str'>

    result_list = data["data"]["result"]
    new_list = process_dict(result_list)
    print(f"new_list = {new_list}")
    list_keys = list(result_list[0]['metric'].keys()) + ['value']

    print()
    df = pandas.DataFrame(new_list, columns=list_keys)
    print(df)

    # pivot_df = df.pivot_table(index='resource', columns='type', values='value', aggfunc='first').reset_index()
    # pivot_df.columns.name = None
    # print(pivot_df)

import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    data = load_json('data/properties.json')
    for property in data:
        print(property)

def get_investor_profile():
    investor_profile = {
        'investment_type': input('Enter risk appetite (core, core-plus, opportunistic, value-add): '),
        'size': float(input('Enter min asset size: ')),
        'min_cap': float(input('Enter min cap rate (0.00 - 1.00): ')),
    }
    return investor_profile


if __name__ == "__main__":
    data = load_json('data/properties.json')
    investor_profile = get_investor_profile()
import requests


def check_json(text):
    try:
        json_text = text.json()
        return json_text
    except:
        print("Invalid quote resource!")


def main():
    print("Input the URL:")
    url = input()
    try:
        response = requests.get(url)
    except requests.RequestException:
        print("Invalid quote resource!")
    else:
        if response:
            try:
                json_text = check_json(response)
                print(json_text["content"])
            except KeyError or TypeError:
                print("Invalid quote resource!")
        else:
            print("Invalid quote resource!")


if __name__ == "__main__":
    main()
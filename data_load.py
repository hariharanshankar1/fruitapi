import requests
import json

result = '{}'
fruit_data = requests.get("https://www.fruityvice.com/api/fruit/all")
i = 1
# x = {}
file =[]
x = json.loads(result)
for fruit in fruit_data.json():
    if requests.get("https://passport-media.s3-us-west-1.amazonaws.com/images/eng-intern-interview/" + str(
            fruit["name"]).lower() + ".png").status_code == 403:
        image = ""
    else:
        image = "https://passport-media.s3-us-west-1.amazonaws.com/images/eng-intern-interview/" + str(
            fruit["name"]).lower() + ".png"

    result = {
        "model": "fruit_grid_app.fruit",
        "pk": i,
        "fields": {
            "genus": fruit["genus"],
            "name": fruit["name"],
            "id": fruit["id"],
            "family": fruit["family"],
            "order": fruit["order"],
            "carbohydrates": fruit["nutritions"]["carbohydrates"],
            "protein": fruit["nutritions"]["protein"],
            "fat": fruit["nutritions"]["fat"],
            "calories": fruit["nutritions"]["calories"],
            "sugar": fruit["nutritions"]["sugar"],
            "image": image
        }
    }

    #file.append(result)
    #json_obj = json.dumps(result, indent=4)
    file.append(result)
    i += 1
with open('./fruit_grid_app/fixtures/data.json', 'w') as f:
    json.dump(file[:], f)
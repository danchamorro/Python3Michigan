# Extract the value associated with the key color and assign it to the variable color. Do not hard code this.


info = {'personal_data':
        {'name': 'Lauren',
         'age': 20,
         'major': 'Information Science',
         'physical_features':
         {'color': {'eye': 'blue',
                    'hair': 'brown'},
          'height': "5'8"}
         },
        'other':
        {'favorite_colors': ['purple', 'green', 'blue'],
         'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
        }

color = info["personal_data"]["physical_features"]["color"]

print(color)

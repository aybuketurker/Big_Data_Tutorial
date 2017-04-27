import json
import requests
import csv

# Put your access token here
access_token = 'Ae9lvszDyyNRJzSB7oW_DERsDbSmFDFe5PQB1OFC2b_nzyApHgAAAAA'

class PinterestAPI(object):
    prefix_url = 'https://api.pinterest.com/v1/'
    default_fields = ['creator', 'id', 'image', 'link', 'original_link', 'note', 'url']

    def __init__(self, access_token):
        self.access_token = access_token

    def get_request(self, path, params={}):
        params['access_token'] = self.access_token
        url = self.prefix_url + path
        # Make a request with the given url and parameters 
        # Return the JSON form of the request
        
        

    def get_board_pins(self, board, fields=None):
        # Define the path (i.e., the url)
        # path = 
        
        if not fields:
            fields = PinterestAPI.default_fields
        return self.get_request(path, {'fields': ','.join(fields)})

    def get_all_board_pins(self, board, fields=None):
        j = self.get_board_pins(board, fields)
        data = j['data']
        # Loop while there's still another page
        while j['page']['next']:
            # Use the next URL and perform another GET request
            # j = 
            # Add data from the request to data
            # data += 
            # delete the break statement when you've completed the above
           
            
        return data

def main():
    # Create a PinterestAPI object
    # Perform a request on the board 'bdatascience/ikea-lab' using get_board_pins
    # Take a look at how many pins you found using len(<request JSON>['data'])
    # Now, use get_all_board_pins to get *all* of the board's pins
    # The following will save your pins to a file, assuming your pins are in
    # a variable called pins
    #with open('pins.json', 'w') as f:
    #   json.dump(pins, f)
    
    


   # __name__ == '__main__' when this script is run via `python pinterest.py`
# Unlike some languages, main() isn't automatically called, so we do it ourselves.
if __name__ == '__main__':
    main()

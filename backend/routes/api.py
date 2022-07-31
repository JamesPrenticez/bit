from flask import Blueprint, request, jsonify 

class Api:
    def __init__(self):
        self.api = self.create_api()
        
    def create_api(self):
        api_page = Blueprint("api", __name__)
        @api_page.route("/api", methods=['GET'])
        
        def api():
            customer = request.args.get('customer')

            #result = json.dumps({'request': "invalid"}, indent = 4)
            result = ['one', 'two', 'three']
            
            if customer is not None:
                result = ""

            return jsonify(result)

        return api_page
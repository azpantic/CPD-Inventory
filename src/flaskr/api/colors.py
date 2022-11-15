from flask_restful import Resource, Api, request
from flaskr.app import app

api = Api(app)


LEDS = []


class Colors(Resource):

    def post(self):

        global LEDS

        cell_id = request.form.get("cell_id", default=0)
        color = request.form.get("color", default="#2BF70B")
        LEDS.append({"id": cell_id, "color": color})
        # print(f"post { self.LEDS}")

    def get(self):
        global LEDS
        res = {"colors": LEDS}
        LEDS = []
        return res


api.add_resource(Colors, '/api/colors')

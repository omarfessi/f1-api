from pydoc import Helper
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app=Flask( __name__ )
api=Api(app)


drivers_standings = {

    16:{ 'first_name': 'Charles', 
        'last_name':'Leclerc', 
        'team': 'Scuderia Ferrari',
        'points':126},

    44:{ 'first_name': 'Lewis', 
        'last_name':'Hamilton', 
        'team': 'Mercedes-AMG Petronas',
        'points':77},

    1:{ 'first_name': 'Max', 
        'last_name':'Verstappen', 
        'team': 'Redbull Racing',
        'points':175},
        }

post_args= reqparse.RequestParser()
post_args.add_argument('first_name', type=str, help='First name is mandatory', required=True )
post_args.add_argument('last_name', type=str, help='Last name is mandatory', required=True )
post_args.add_argument('team', type=str, help='team name is mandatory', required=True )
post_args.add_argument('points', type=int, help='First name is mandatory', required=True)


class DriverStandings(Resource):
    def get(self) :
        return {'data': drivers_standings}

class Drivers(Resource):
    def get(self, driver_id):
        if driver_id not in drivers_standings:
            abort(404, description="Driver not found")
        return drivers_standings[driver_id]

    def post(self, driver_id):
        if driver_id in drivers_standings:
            abort(409, description='Driver already exists')
        args=post_args.parse_args()
        drivers_standings[driver_id] = {"first_name":args["first_name"], "last_name": args["last_name"], "team": args["team"], "points":args["points"]}
        return drivers_standings[driver_id]

api.add_resource(DriverStandings, '/driverstandings')
api.add_resource(Drivers, '/drivers/<int:driver_id>')


if __name__=="__main__":
    app.run(debug=True)

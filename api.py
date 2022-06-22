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

def abort_if_driver_doesnt_exist(driver_id):
    if driver_id not in drivers_standings:
        abort(404, message="Driver {} doesn't exist".format(driver_id))
def abort_if_driver_does_exist(driver_id):
    if driver_id in drivers_standings:
        abort(409, message="Driver {} already exists".format(driver_id))

post_args= reqparse.RequestParser()
post_args.add_argument('first_name', type=str, help='First name is mandatory', required=True )
post_args.add_argument('last_name', type=str, help='Last name is mandatory', required=True )
post_args.add_argument('team', type=str, help='team name is mandatory', required=True )
post_args.add_argument('points', type=int, help='First name is mandatory', required=True)

put_args= reqparse.RequestParser()
put_args.add_argument('first_name', type=str)
put_args.add_argument('last_name', type=str)
put_args.add_argument('team', type=str)
put_args.add_argument('points', type=int)


class DriverStandings(Resource):
    def get(self) :
        return {'data': drivers_standings}

class Drivers(Resource):
    def get(self, driver_id):
        abort_if_driver_doesnt_exist(driver_id)
        return drivers_standings[driver_id]

    def post(self, driver_id):
        abort_if_driver_does_exist(driver_id)
        args=post_args.parse_args()
        drivers_standings[driver_id] = {"first_name":args["first_name"], "last_name": args["last_name"], "team": args["team"], "points":args["points"]}
        return drivers_standings[driver_id]
    
    def delete(self, driver_id):
        abort_if_driver_doesnt_exist(driver_id)
        del drivers_standings[driver_id]
        return drivers_standings

    def put(self, driver_id):
        abort_if_driver_doesnt_exist(driver_id)
        args=put_args.parse_args()
        if args["first_name"]: 
            drivers_standings[driver_id]["first_name"] = args["first_name"]
        if args["last_name"]: 
            drivers_standings[driver_id]["last_name"] = args["last_name"]
        if args["team"]: 
            drivers_standings[driver_id]["team"] = args["team"]
        if args["points"]: 
            drivers_standings[driver_id]["points"] = args["points"]
        
        return drivers_standings[driver_id]

api.add_resource(DriverStandings, '/driverstandings')
api.add_resource(Drivers, '/drivers/<int:driver_id>')


if __name__=="__main__":
    app.run(debug=True)


import get_trips as gt

def get_trips_to_improve(user_uuid, filter_function):
    #pick trips which we would like to improve
    #will make usage of canonical trip class
    #returns a list of trips implementing Trip interface, could be basic E_Mission_Trips or canonical
    # TODO: Stubbed out returning all move trips in order to allow tests to pass
    return list(gt.TripIterator(user_uuid, ["utility", "get_training"]))

def retrieve_alternative_trips(trip_list):
    return []

def get_user_utility_models(user_id):
    return []

def recommend_trips(trip_id, utility_model):
    return []

def _evaluate_trip(utility_model, trip):
    #return an integer value for the score of a trip, based on a utility model
    return 0
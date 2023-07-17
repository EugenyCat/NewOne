# Return errors
def get_errors(*aggr):
    list_er = []
    dict_errors = {
        "out": "You go out from system",
        "noaccess": "You don't have access to this area",
        "unknown": "Unknown error",
        "timeout": "System doesn't answer long",
        "robot": "Your activity like a robot's activity"
    }
    for item in aggr:
        list_er.append(dict_errors[item])
    print(list_er)


get_errors('out', 'robot')

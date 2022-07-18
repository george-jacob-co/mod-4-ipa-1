social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):
        
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else: 
        return "no relationship"
            
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    
    horizontal_check = [x for x in board]
    vertical_check = [x for x in zip(*board)]
    updown_diagonal_check = [board[i][i] for i,v in enumerate(board)]
    downup_diagonal_check = [board[len(board)-1-i][i] for i,v in enumerate(board)]
    
    for j,k in enumerate(horizontal_check):
        if j < len(horizontal_check):
            if all([s=="X" for s in k]):
                return "X"
            elif all([s=="O" for s in k]):
                return "O"
            else:
                continue
        else:
            break
                      
    for l,m in enumerate(vertical_check):
        if l < len(vertical_check):
            if all([s=="X" for s in m]):
                return "X"
            elif all([s=="O" for s in m]):
                return "O"
            else:
                continue
        else:
            break
                      
    if all([s=="X" for s in updown_diagonal_check]):
          return "X"
    elif all([s=="O" for s in updown_diagonal_check]):
          return "O"
    elif all([s=="X" for s in downup_diagonal_check]):
          return "X"
    elif all([s=="O" for s in downup_diagonal_check]):
          return "O"
    else:
          return "NO WINNER"

route_map = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

def eta(first_stop, second_stop, route_map):
    destination_routes = route_map.keys()
    j = [x for x,y in enumerate(destination_routes)]
    k = [y for x,y in enumerate(destination_routes)]
    l = [y for y,z in k]
    m = [z for y,z in k]
    recurring_mins = 0
    for o in l:
        p = l.index(o)
        if o == first_stop:
            while(True):
                if m[p] != second_stop:
                    stop_mins = int(route_map[l[p],m[p]]['travel_time_mins'])
                    recurring_mins += stop_mins
                    if p == len(l) - 1:
                        p = 0
                    elif p < len(l):
                        p += 1
                    continue
                elif m[p] == second_stop:
                    first_stop_mins = int(route_map[l[p],m[p]]['travel_time_mins'])
                    return recurring_mins + first_stop_mins

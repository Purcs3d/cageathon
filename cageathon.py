
import random
import sys
import json

class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

        
def listMovies(movies, seen = False):
    for key in movies:
        if movies[key][0] == "seen": 
            if   movies[key][1] == "rewatch"    : print(bcolors.OKGREEN + "{} : {} | {}".format(key, movies[key][2], movies[key][3]) + bcolors.ENDC)
            elif movies[key][1] == "watch"      : print(bcolors.WARNING + "{} : {} | {}".format(key, movies[key][2], movies[key][3]) + bcolors.ENDC)
            elif movies[key][1] == "don't watch": print(bcolors.FAIL    + "{} : {} | {}".format(key, movies[key][2], movies[key][3]) + bcolors.ENDC)
            else                                : print(bcolors.BOLD    + "{} : {} | {}".format(key, movies[key][2], movies[key][3]) + bcolors.ENDC)

        elif not seen: print(bcolors.OKCYAN + "{} : {} | {}".format(key, movies[key][2], movies[key][3]) + bcolors.ENDC)



cageFile = open("cageathon.json")
movies = json.load(cageFile)["movies"]

if len(sys.argv) > 2:
    if sys.argv[1] == "list":
        if sys.argv[2] == "seen":
            listMovies(movies, True)

    if sys.argv[1] == "name":
        if movies[sys.argv[2]][0] == "seen": 
            if   movies[sys.argv[2]][1] == "rewatch"    : print(bcolors.OKGREEN + "{} : {} | {}".format(sys.argv[2], movies[sys.argv[2]][2], movies[sys.argv[2]][3]) + bcolors.ENDC)
            elif movies[sys.argv[2]][1] == "watch"      : print(bcolors.WARNING + "{} : {} | {}".format(sys.argv[2], movies[sys.argv[2]][2], movies[sys.argv[2]][3]) + bcolors.ENDC)
            elif movies[sys.argv[2]][1] == "don't watch": print(bcolors.FAIL    + "{} : {} | {}".format(sys.argv[2], movies[sys.argv[2]][2], movies[sys.argv[2]][3]) + bcolors.ENDC)
            else                                        : print(bcolors.BOLD    + "{} : {} | {}".format(sys.argv[2], movies[sys.argv[2]][2], movies[sys.argv[2]][3]) + bcolors.ENDC)

        else: print(bcolors.OKCYAN + "{} : {} | {}".format(sys.argv[2], movies[sys.argv[2]][2], movies[sys.argv[2]][3]) + bcolors.ENDC)
        

elif len(sys.argv) > 1:
    if sys.argv[1] == "list":
        listMovies(movies)

    if sys.argv[1] == "rand":
        movieList = []
        for key in movies:
            if movies[key][0] != "seen":
                movieList.append(key)

        print(bcolors.HEADER + "------------------------------------")
        print(bcolors.BOLD   + "Ye shall watch '{}'".format(movieList[random.randrange(len(movieList))]))
        print(                 "------------------------------------"  + bcolors.ENDC)

else:
    listMovies(movies)

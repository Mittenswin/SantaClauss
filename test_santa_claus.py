from santa_claus import dictionary_cities, distance_cities, tour_length, closest_city, tour_from_closest_city, best_tour_from_closest_city, reverse_part_tour, inversion_length_diff, better_inversion, best_obtained_with_inversions
#from santa_claus import *

def test_dictionary_cities():
    dico = {'Paris': {'Lyon': 394.5056834297657, 'Marseille': 661.8616554466852, 'Lille': 203.67224282542662},
     'Lyon': {'Paris': 394.5056834297657, 'Marseille': 275.87965367431525, 'Lille': 558.5472363339595}, 
     'Marseille': {'Paris': 661.8616554466852, 'Lyon': 275.87965367431525, 'Lille': 834.0220261600157}, 
     'Lille': {'Paris': 203.67224282542662, 'Lyon': 558.5472363339595, 'Marseille': 834.0220261600157}}

    villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]

    assert dictionary_cities(villes) == dico

def test_distance_cities():
    villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    assert distance_cities("Paris", "Marseille", dictionary_cities(villes)) == 661.8616554466852
    assert distance_cities("Marseille", "LazyTown", dictionary_cities(villes)) == -1

def test_tour_length():
    villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    tour = ["Paris", "Lyon", "Marseille", "Lille"]
    assert tour_length(tour, dictionary_cities(villes)) == 1708.0796060895232

def test_closest_city():
    villes = villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    cities = ["Marseille","Lyon", "Lille"]
    assert closest_city("Paris", cities, dictionary_cities(villes)) == 2

def test_tour_from_closest_city():
    villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    dicoo = dictionary_cities(villes)

    assert tour_from_closest_city("Lyon", dicoo) == ['Lyon', 'Marseille', 'Paris', 'Lille']

def test_best_tour_from_closest_city():
    villes =  ["Paris", 2.33, 48.86, "Lyon", 4.85,45.75, "Marseille", 5.40, 43.30, 
          "Lille", 3.06, 50.63, "Strasbourg", 7.75, 48.57, "Rennes", -1.66, 48.11, 
          "Clermont-Ferrand",3.08, 45.77, "Bordeaux", -0.57, 44.83, "Toulouse", 1.43, 43.60, 
          "Grenoble", 5.72, 45.18 ]
    dicooo = dictionary_cities(villes)

    assert best_tour_from_closest_city(dicooo) == ['Clermont-Ferrand', 'Lyon', 'Grenoble', 'Marseille', 'Toulouse', 'Bordeaux', 'Rennes', 'Paris', 'Lille', 'Strasbourg']

def test_reverse_part_tour():
    tour = ["Agen", "Belfort", "Cahors", "Dijon", "Épinay", "Fréjus", "Grenoble", "Hyères"]
    assert reverse_part_tour(tour, 4, 7) == ['Agen', 'Belfort', 'Cahors', 'Dijon', 'Hyères', 'Grenoble', 'Fréjus', 'Épinay']

def test_inversion_length_diff():
    villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    dicoo = dictionary_cities(villes)
    cities = ["Marseille","Lyon", "Paris", "Lille"]

    assert inversion_length_diff(dicoo, cities, 1, 2) == -740.856995280903

def test_better_inversion():
    villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    dicooo = dictionary_cities(villes)
    tour = ["Marseille", "Lyon", "Lille", "Paris"]

    assert better_inversion(tour, dicooo) == False

def test_best_obtained_with_inversions():
    villes = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]
    tour =  ["Marseille", "Lyon", "Lille", "Paris"]
    dicoo = dictionary_cities(villes)
    
    assert best_obtained_with_inversions(tour, dicoo) == 0

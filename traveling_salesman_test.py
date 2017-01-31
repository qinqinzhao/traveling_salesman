import unittest
from traveling_salesman import *


class TestTravelingSalesmanProblem(unittest.TestCase):
    
    def test_compute_total_distance(self):
        road_map1 = [('Alabama', 'Montgomery', '32.361538', '-86.279118'), \
                     ('Alaska', 'Juneau', '58.301935', '-134.41974'), \
                     ('Arizona', 'Phoenix', '33.448457', '-112.073844')]
        self.assertAlmostEqual(compute_total_distance(road_map1), \
                               distance(32.361538, -86.279118, 58.301935, -134.41974) + \
                               distance(58.301935, -134.41974, 33.448457, -112.073844) + \
                               distance(33.448457, -112.073844, 32.361538, -86.279118))
        road_map2 = [('New Mexico', 'Santa Fe', '35.667231', '-105.964575'), \
                     ('New York', 'Albany', '42.659829', '-73.781339'),\
                     ('North Carolina', 'Raleigh', '35.771', '-78.638'), \
                     ('North Dakota', 'Bismarck', '48.813343', '-100.779004'), \
                     ('Ohio', 'Columbus', '39.962245', '-83.000647')]
        self.assertAlmostEqual(compute_total_distance(road_map2), \
                               distance(35.667231, -105.964575, 42.659829, -73.781339) + \
                               distance(42.659829, -73.781339, 35.771, -78.638) + \
                               distance(35.771, -78.638, 48.813343, -100.779004) + \
                               distance(48.813343, -100.779004, 39.962245, -83.000647) + \
                               distance(39.962245, -83.000647, 35.667231, -105.964575))

    def test_swap_adjacent_cities(self):
        road_map1 = [('Indiana', 'Indianapolis', '39.790942', '-86.147685'), \
                    ('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
                    ('Kansas', 'Topeka', '39.04', '-95.69')]
        new_road_map1 = [('Kansas', 'Topeka', '39.04', '-95.69'), \
                        ('Iowa', 'Des Moines', '41.590939', '-93.620866'),\
                        ('Indiana', 'Indianapolis', '39.790942', '-86.147685')]
        new_total_distance1 = compute_total_distance(new_road_map1)
        self.assertEqual(swap_adjacent_cities(road_map1, 2),\
                         (new_road_map1, new_total_distance1))
        road_map2 = [('Virginia', 'Richmond', '37.54', '-77.46'), \
                     ('Washington', 'Olympia', '47.042418', '-122.893077'), \
                     ('West Virginia', 'Charleston', '38.349497', '-81.633294'),\
                     ('Wisconsin', 'Madison', '43.074722', '-89.384444'), \
                     ('Wyoming', 'Cheyenne', '41.145548', '-104.802042')]
        new_road_map2 = [('Virginia', 'Richmond', '37.54', '-77.46'), \
                         ('Washington', 'Olympia', '47.042418', '-122.893077'), \
                         ('West Virginia', 'Charleston', '38.349497', '-81.633294'),\
                         ('Wyoming', 'Cheyenne', '41.145548', '-104.802042'), \
                         ('Wisconsin', 'Madison', '43.074722', '-89.384444')]
        new_total_distance2 = compute_total_distance(new_road_map2)
        self.assertEqual(swap_adjacent_cities(road_map2, 3),\
                         (new_road_map2, new_total_distance2))

    def test_swap_cities(self):
        road_map1 = [ ('Colorado', 'Denver', '39.7391667', '-104.984167'),\
                      ('Connecticut', 'Hartford', '41.767', '-72.677'),\
                      ('Delaware', 'Dover', '39.161921', '-75.526755'),\
                      ('Florida', 'Tallahassee', '30.4518', '-84.27277')]
        new_road_map1 = [('Colorado', 'Denver', '39.7391667', '-104.984167'),\
                         ('Florida', 'Tallahassee', '30.4518', '-84.27277'),\
                         ('Delaware', 'Dover', '39.161921', '-75.526755'),\
                         ('Connecticut', 'Hartford', '41.767', '-72.677')]
        new_total_distance1 = compute_total_distance(new_road_map1)
        self.assertEqual(swap_cities(road_map1, 1, 3),\
                         (new_road_map1, new_total_distance1))
        road_map2 = [('Missouri', 'Jefferson City', '38.572954', '-92.189283'),
                     ('Montana', 'Helana', '46.595805', '-112.027031'), \
                     ('Nebraska', 'Lincoln', '40.809868', '-96.675345'), \
                     ('Nevada', 'Carson City', '39.160949', '-119.753877'),\
                     ('New Hampshire', 'Concord', '43.220093', '-71.549127'), \
                     ('New Jersey', 'Trenton', '40.221741', '-74.756138')]
        new_road_map2 = [('New Hampshire', 'Concord', '43.220093', '-71.549127'),
                         ('Montana', 'Helana', '46.595805', '-112.027031'), \
                         ('Nebraska', 'Lincoln', '40.809868', '-96.675345'), \
                         ('Nevada', 'Carson City', '39.160949', '-119.753877'),\
                         ('Missouri', 'Jefferson City', '38.572954', '-92.189283'),\
                         ('New Jersey', 'Trenton', '40.221741', '-74.756138')]
        new_total_distance2 = compute_total_distance(new_road_map2)
        self.assertEqual(swap_cities(road_map2, 0, 4),\
                         (new_road_map2, new_total_distance2))
        new_road_map3 = [('Missouri', 'Jefferson City', '38.572954', '-92.189283'),
                         ('Montana', 'Helana', '46.595805', '-112.027031'), \
                         ('Nebraska', 'Lincoln', '40.809868', '-96.675345'), \
                         ('Nevada', 'Carson City', '39.160949', '-119.753877'),\
                         ('New Hampshire', 'Concord', '43.220093', '-71.549127'), \
                         ('New Jersey', 'Trenton', '40.221741', '-74.756138')]
        new_total_distance3 = compute_total_distance(new_road_map3)
        self.assertEqual(swap_cities(road_map2, 5, 5),\
                         (new_road_map3, new_total_distance3))

    def test_find_best_cycle(self):
        road_map = read_cities("city_data.txt")
        road_map_set = set(road_map)
        best_cycle = find_best_cycle(road_map) 
        best_cycle_set = set(best_cycle)
        self.assertEqual(road_map_set, best_cycle_set)
        self.assertTrue(compute_total_distance(best_cycle) < 30000)
                         
        
unittest.main()

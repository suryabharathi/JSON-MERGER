##TESTING CODE

import unittest
import json
import os
import util
import copy
from main import json_merge_recursive


class SimpleTest(unittest.TestCase):
    def test1(self):
        data1={"id":1}
        data2={"id":2}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)       
        print(jsonstring)
        self.assertEqual(jsonstring,'{"id": [1, 2]}')
        
    def test2(self):
        data1={"id":1}
        data2={"name":"freshworks"}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)
        print(jsonstring)
        self.assertEqual(jsonstring,'{"name": "freshworks", "id": 1}')
        
    def test3(self):
        data1={"StudentID":1}
        data2={"Subject Codes":[101,102,103]}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)
        print(jsonstring)
        self.assertEqual(jsonstring,'{"Subject Codes": [101, 102, 103], "StudentID": 1}')

    def test4(self):
        data1={"StudentID":1}
        data2={"Course":{"CourseID":2, "CourseName": "B Tech"}}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)
        print(jsonstring)
        self.assertEqual(jsonstring,'{"Course": {"CourseID": 2, "CourseName": "B Tech"}, "StudentID": 1}')
        
    def test4(self):
        data1={"name":"freshworks"}
        data2={"name":"freshdesk"}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)
        print(jsonstring)
        self.assertEqual(jsonstring,'{"name": ["freshworks", "freshdesk"]}')

    def test5(self):
        data1={"products":"freshservice"}
        data2={"products":["freshsales","freshdesk","freshchat"]}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)
        print(jsonstring)
        self.assertEqual(jsonstring,'{"products": ["freshsales", "freshdesk", "freshchat", "freshservice"]}')



    def test6(self):
        data1={"title":"Joker"}
        data2={"title":{"title1":"Black Mirror","title2":"Stranger Things"}}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)
        print(jsonstring)
        self.assertEqual(jsonstring,'{"title": {"title1": "Black Mirror", "title2": "Stranger Things", "0": "Joker"}}')

    def test7(self):
        data1={"name":"name4"}
        data2={"name":["name0","name1","name2","name3"]}
        json_merge_recursive(data1,data2)
        jsonstring=json.dumps(data2)
        print(jsonstring)
        self.assertEqual(jsonstring,'{"name": ["name0", "name1", "name2", "name3", "name4"]}')


    
 


if __name__ == '__main__':
    unittest.main()








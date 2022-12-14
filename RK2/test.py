from unittest import TestCase, main
from main import task1, task2, task3
 
class testrk2(TestCase):
    def test_task1(self):
        self.assertEqual(task1(
            [('PyCharm', 550000, 'Python', '3.10', 0),
            ('NetBeans', 120000, 'Java', 'v18', 1),
            ('VS Code', 530000, 'C++', '17.2.0', 2),
            ('WebStorm', 115000, 'JavaScript', '1.8.5', 3),
            ('Xcode', 150000, 'Swift', '5.6', 4),
            ('Visual Studio', 1450000, 'C#', '5.6', 5),
            ('Eclipse', 224000, 'C#', '5.6', 5)]),
 
            [('Visual Studio', 1450000, 'C#', '5.6', 5),
            ('PyCharm', 550000, 'Python', '3.10', 0),
            ('VS Code', 530000, 'C++', '17.2.0', 2),
            ('Eclipse', 224000, 'C#', '5.6', 5),
            ('Xcode', 150000, 'Swift', '5.6', 4),
            ('NetBeans', 120000, 'Java', 'v18', 1),
            ('WebStorm', 115000, 'JavaScript', '1.8.5', 3)])
 
    def test_task2(self):
        self.assertEqual(task2(
            [('PyCharm', 550000, 'Python', '3.10', 0),
            ('NetBeans', 120000, 'Java', 'v18', 1),
            ('VS Code', 530000, 'C++', '17.2.0', 2),
            ('WebStorm', 115000, 'JavaScript', '1.8.5', 3),
            ('Xcode', 150000, 'Swift', '5.6', 4),
            ('Visual Studio', 1450000, 'C#', '5.6', 5),
            ('Eclipse', 224000, 'C#', '5.6', 5)]),
 
            [('Python', 1),
            ('Java', 1),
            ('C++', 1),
            ('JavaScript', 1),
            ('Swift', 1),
            ('C#', 2)])
 
    def test_task3(self):
        self.assertEqual(task3(
            [('Python', 0, 'Visual Studio'),
            ('C#', 5, 'Visual Studio'),
            ('C', 6, 'Visual Studio'),
            ('F#', 8, 'Visual Studio'),
            ('Python', 0, 'VS Code'),
            ('C++', 2, 'VS Code'),
            ('JavaScript', 3, 'VS Code'),
            ('HTML', 7, 'VS Code'),
            ('F#', 8, 'VS Code'),
            ('JavaScript', 3, 'WebStorm'),
            ('Python', 0, 'PyCharm'),
            ('Swift', 4, 'Xcode'),
            ('Java', 1, 'NetBeans'),
            ('C++', 2, 'NetBeans'), 
            ('C++', 2, 'Eclipse'),
            ('C#', 5, 'Eclipse'),
            ('C', 6, 'Eclipse')]),
 
            {'C++': ['VS Code', 'NetBeans', 'Eclipse'],
            'C#': ['Visual Studio', 'Eclipse'],
            'C': ['Visual Studio', 'Eclipse']})
 
if __name__ == "__main__":
    main()
student = {'name': 'Shravani', 'age': 21, 'branch': 'CSE'}
print(student)
student2 = dict(name='Kiran', age=21, branch='CSE')
print(student2)
student3 = dict([('name', 'Sandhya'), ('age', 21), ('branch', 'CSE')])
print(student3)

student4 = {
    'name': 'Shravani',
    'marks': {'APC': 90, 'CC': 95}
}
print(student4)

empty_dict = {}
empty_dict2 = dict()
print(empty_dict)
print(empty_dict2)

print(student['name']) 
print(student.get('age'))   
student['city'] = 'Kolhapur'  
student['age'] = 22  
print(student)           
student.pop('age')   
print(student)        
student.popitem()   
print(student)            
del student['branch'] 
print(student)
copy_dict = student.copy()
print(copy_dict)               
print(student.keys())   
print(student.values())       
print(student.items())       
print('name' in student)         
student.setdefault('grade', 'A')  
print(student)               
student.update({'name': 'Shravani Mali', 'age': 22})
print(student)  
student.clear() 
print(student)            

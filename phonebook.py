# enter values of 'add' or 'delete' or 'search'



import sys

def fetch_details(name):
    print(f'search for: {name}')
    for key, value in my_dict[name.lower()].items():
        print(f'{key}: {value}')
    return


def delete_item(name):
  if name.lower() in my_dict:
    del my_dict[name.lower()]
    print("Updated Dictionary :", my_dict)
  else:
    print("name not found")
  return
      
def insert_item():
  new={}
  name =input("enter name: ")
  new['name:']=name
  name=name.split(' ')
  email =input("enter Email: ")
  new['Email']=email
  phone =str(input("enter phone: "))
  new['phone']=phone
  my_dict[name[0]]=new
  f=open('phonebook.txt','w')
  f.write(str(my_dict))
  print(my_dict)
  #string=',name :'+'{'+'name:'+name+',Email:'+email+',phone:'+phone+'}'
  #
  f.close()
  return
  
def phonebook():
  while True:
    name =input('enter a name:  ')
    print("\n enter 1 for search 2 for delete 3 for insert")
    temp =str(input())
    if temp == '1':
      fetch_details(name)
    elif temp == '2':
      delete_item(name)
    elif temp == '3':
        insert_item()


if __name__ == "__main__": 
  if len(sys.argv)>=2:
    f=open("phonebook.txt",'r+')
    my_dict=eval(f.readline())
    f.close()
    if sys.argv[1] == 'search':
      name =input('enter a name:  ')
      fetch_details(name)
    elif sys.argv[1] == 'add':
      insert_item()
    elif sys.argv[1] == 'delete':
      name =input('enter a name:  ')
      delete_item(name)
    else:
      print(r"'enter values of 'add' or 'delete' of 'search'")
  else:
    None
    
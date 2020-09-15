import requests

username = input("Enter the github username:")

request = requests.get('https://api.github.com/users/'+username+'/repos?page=1')
json = request.json()

for i in range(0,len(json)):
  repository_url = json[i]['svn_url']
  repository_name = repository_url.replace('https://github.com/', '', )
  print(repository_name)
  
  # print("Project Number:",i+1)
  # print("Project Name:",json[i]['name'])
  # print("Project URL:",json[i]['svn_url'],"\n")

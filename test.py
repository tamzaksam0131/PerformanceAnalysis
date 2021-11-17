import yaml

a_yaml_file = open('sql_config.yml')
a = yaml.load(a_yaml_file, Loader = yaml.FullLoader)
SQL_Sentence = a['Standard_Value_1'] 

print(SQL_Sentence)
print(type(SQL_Sentence))
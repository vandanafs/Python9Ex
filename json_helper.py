import json
import os
import pickle
from os import path
#from typing import BinaryIO

#partA



def read_json(file_path):  # provide json file path
    with open(file_path) as json_file: # open as json file  # not working
        json_dict=json.load(json_file)   # pass the json file
        return json.dumps(json_dict)  # key value json object returned

file_path=read_json("/Users/vandana/PycharmProjects/Python9Ex/data/super_smash_bros")

#partB
def read_all_files(json_files_path):  # path directory
    json_files=[]  # returning json file
    for file_name in os.listdir(os.getcwd() + path):
        path_to_json=os.getcwd() +path +'/' + file_name  #  path
        json_obj=read_json(path_to_json) #read json
        json_obj.append(json_obj)
    return json_obj  # list of json_files


read_all_files(file_path)


#PartC
def write_pickle(pickle_file_path,file_name):
    json_obj=read_all_files(pickle_file_path)
    #with open(f'{file_name}.pickle','wb') as pickle_file:
    pickle_file=open(file_name,"wb")  # type:
    pickle.dump(json_obj,pickle_file)  # write list of json formatted strings to pickle file
    pickle_file.close()

write_pickle("/Users/vandana/PycharmProjects/Python9Ex/data/super_smash_bros/super_smash_characters.pickle","/Users/vandana/PycharmProjects/Python9Ex/data/super_smash_bros/mario.json")
def load_pickle(pickle_file_path) :
    data=None
   # with open(f'{pickle_file_name}.pickle', 'rb') as pickle_file:
    pickle_file=open(pickle_file_path,"rb")
    data=pickle.load(pickle_file) # data will be list of json strings
    return data


load_pickle()
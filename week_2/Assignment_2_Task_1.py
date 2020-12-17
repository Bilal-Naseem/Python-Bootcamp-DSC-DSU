import os
import math
import csv

def write_result_to_csv(FList):
    with open('SortedFileList.csv', mode='a+') as File:
        filePointer = csv.DictWriter(File,fieldnames=['FileSize','FileName','FileDir'])
        filePointer.writeheader()
        for eachDict in FList:
            Print_size = math.floor(eachDict['FileSize']/(1024*1024))
            if Print_size == 0 :
                Print_size = math.floor(eachDict['FileSize']/(1024))
                eachDict['FileSize'] = f"{Print_size} KBs"
            else:
                eachDict['FileSize'] = f"{Print_size} MBs"
            filePointer.writerow(eachDict)

def Sort(File_List):
    File_List_Sorted = sorted(File_List, key=lambda k: k['FileSize'], reverse=True)
    write_result_to_csv(File_List_Sorted)

def get_ls(path):
    File_List = []
    for folders, subfolders, files in os.walk(path):

        for filename in files:

            file_path = folders[len(path):]
            if len(file_path) == 0 : 
                file_path = '.\\'

            file_size = os.path.getsize(folders+"\\"+filename)

            file_dict = {'FileName' : filename, 'FileSize' : file_size, 'FileDir' : file_path}
            File_List.append(file_dict)
    Sort(File_List)

def main():
    user_input = input("Enter Path to Folder:")
    get_ls(user_input)

if __name__ == "__main__":
    main()
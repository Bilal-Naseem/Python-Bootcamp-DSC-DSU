import requests
import csv
def ExportDataIntoCSV(DataDictList):
    with open('SchoolData.csv',mode="a") as DataFile:
        FilePointer = csv.DictWriter(DataFile,fieldnames=['SchoolName','SchoolAddress','Principal','Position','Email','Telephone'])
        FilePointer.writeheader()
        for SingleSchool in DataDictList:
            FilePointer.writerow(SingleSchool)

def GetSingleSchool(School_Code):
    ApiUrl = f"https://directory.ntschools.net/api/System/GetSchool?itSchoolCode={School_Code}"
    response = requests.get(ApiUrl)
    School_Info = response.json()

    SchoolData = {
        'SchoolName':School_Info['name'],
        'SchoolAddress': School_Info['physicalAddress']['displayAddress'],
        'Telephone' : School_Info['telephoneNumber']
        }
    for SchoolManagement in School_Info['schoolManagement']:
        if(SchoolManagement['position'] == 'Principal'):
            SchoolData.update(Principal = (SchoolManagement['firstName'] + SchoolManagement['lastName']) )
            SchoolData.update(Position = SchoolManagement['position'])
            SchoolData.update(Email = SchoolManagement['email'])
    return SchoolData

def GetAllSchools():
    ApiUrl = "https://directory.ntschools.net/api/System/GetAllSchools"
    response = requests.get(ApiUrl)
    School_List = response.json()
    SchoolScrapped = []
    for i in range (len(School_List)):
        School = GetSingleSchool(School_List[i]['itSchoolCode'])
        SchoolScrapped.append(School)
        if i == 50:
            break
    ExportDataIntoCSV(SchoolScrapped)

def main():
    GetAllSchools()

if __name__ == "__main__":
    main()
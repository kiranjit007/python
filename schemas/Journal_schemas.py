#  from models.Journal_models import iRef_Author


def iRef_Data1_serializer(iRef_Data1) -> dict:
    return {
            #"id": str(iRef_Data1["_id"]),
            "type": str(iRef_Data1["type"]),
            "authors": list(iRef_Data1["authors"]),
            "groups": str(iRef_Data1["groups"]),
            "firstPage": str(iRef_Data1["firstPage"]),
            "lastPage": str(iRef_Data1["lastPage"]),
            "issue": str(iRef_Data1["issue"]),
            "journalTitle": str(iRef_Data1["journalTitle"]),
            "articleTitle": iRef_Data1["articleTitle"],
            "url": str(iRef_Data1["url"]),
            "volume": str(iRef_Data1["volume"]),
            "year": str(iRef_Data1["year"])
        }


def Journal_serializer(Journal) -> list:
    return [iRef_Data1_serializer(iRef_Data1) for iRef_Data1 in Journal]

# def iRef_Data_serializer1(iRef_Data) -> dict:
#     return {
#         "id": str(iRef_Data["_id"]),
#         "type": str(iRef_Data["type"]),
#         "authors": list(iRef_Data[{"firstname": "", "lastname": ""}]),
#         "groups": str(iRef_Data["groups"]),
#         "firstPage": str(iRef_Data["firstPage"]),
#         "lastPage": str(iRef_Data["lastPage"]),
#         "issue": str(iRef_Data["issue"]),
#         "journalTitle": str(iRef_Data["journalTitle"]),
#         "articleTitle": iRef_Data["articleTitle"],
#         "url": str(iRef_Data["url"]),
#         "volume": str(iRef_Data["volume"]),
#         "year": str(iRef_Data["year"])
#     }
#
# def Journal_serializer1(Journal) -> list:
#     return [iRef_Data_serializer1(iRef_Data) for iRef_Data in Journal]


def Db0_serializer(Db0data) -> dict:
    return {
            "id": str(Db0data["Identity Number"]),
            "reference": str(Db0data["ReferenceString"]),
            'Status': str(Db0data['Status']),
            "Doi": str(Db0data['doi'])


        }


def Db0db_serializer(string) -> list:
    return [Db0_serializer(Db0data) for Db0data in string]

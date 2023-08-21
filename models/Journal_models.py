from pydantic import BaseModel
from typing import List,Optional



# class iRef_Author(BaseModel):
#     firstname: str = ""
#     lastname: str = ""


class iRef_Journal(BaseModel):
    id: str = ""
    type: str = ""
#    authors: list[iRef_Author]
    authors: list = [{"firstname": "", "lastname": ""}]
    groups: list = [{'groupname':""}]
    firstPage: str = ""
    lastPage: str = ""
    issue: str = ""
    journalTitle: str = ""
    articleTitle: str = ""
    url: str = ""
    volume: str = ""
    year: str = ""

class iRef_Book(BaseModel):
    id: str = ""
    type: str = ""
    authors: list = [{"firstname": "", "lastname": ""}]
    groups: list = [{'groupname': ""}]
    editors: list = [{"givenname": "", "familyname": ""}]
    firstPage: str = ""
    lastPage: str = ""
    issue: str = ""
    bookTitle: str = ""
    chapterTitle: str = ""
    url: str = ""
    volume: str = ""
    year: str = ""
    edition: str = ""
    PubLocation: str = ""
    PublisherName: str = ""

class Reference(BaseModel):
    reference: list = [{"id": "", "refstring": ""}]
    referenceStyle: str = ""







def journaldo(pq,reference):
    dict01 = {}
    if pq.get("type".lower()) == 'journal':

        mongoninsertlist = []  # just a list to insert to mongodb

        if pq.get("authors") is not None:
            author1 = []
            sm = pq.get("authors")
            for sa in sm:
                dict_2 = {}
                if sa.get("lastname") is not None:
                    dict_2["lastname"] = sa.get("lastname")
                else:
                    dict_2["lastname"] = ""
                if sa.get("firstname") is not None:
                    dict_2["firstname"] = sa.get("firstname")
                else:
                    dict_2["firstname"] = ""
                author1.append(dict_2)
                dict01["authors"] = author1
        else:
            dict01["authors"] = []

        if pq.get("groups") is not None:
            groups1 = []
            nm = pq.get("groups")
            dict_3 = {}
            for np in nm:
                if np.get("lastname") is not None:
                    dict_3["lastname"] = np.get("lastname")
                else:
                    dict_3["lastname"] = ""
                if np.get("firstname") is not None:
                    dict_3["firstname"] = np.get("firstname")
                else:
                    dict_3["firstname"] = ""
                groups1.append(dict_3)
                dict01["groups"] = groups1

        else:
            dict01["groups"] = []

        if pq.get("firstPage") is not None:
            dict01["firstPage"] = pq.get("firstPage")
        else:
            dict01["firstPage"] = ""
        if pq.get("lastPage") is not None:
            dict01["lastPage"] = pq.get("lastPage")
        else:
            dict01["lastPage"] = ""
        if pq.get("issue") is not None:
            dict01["issue"] = pq.get("issue")
        else:
            dict01["issue"] = ""





        if pq.get("journalTitle") is not None:
            dict01["journalTitle"] = pq.get("journalTitle")
        else:
            dict01["journalTitle"] = ""
        if pq.get("articleTitle") is not None:
            dict01["articleTitle"] = pq.get("articleTitle")
        else:
            dict01["articleTitle"] = ""
        dict01["type"] = pq.get("type")

        if pq.get("Doi".lower()) is not None:
            dict01["doi"] = pq.get("Doi".lower())[5::]
        else:
            dict01["doi"] = ""
        if pq.get("volume") is not None:
            dict01["volume"] = pq.get("volume")
        else:
            dict01["volume"] = ""
        if pq.get("elocator") is not None:
            dict01["elocator"] = pq.get("elocator")
        else:
            dict01["elocator"] = ""
        if pq.get("year") is not None:
            dict01["year"] = pq.get("year")
        dict01["referencestyle"] = reference.referenceStyle

    return dict01
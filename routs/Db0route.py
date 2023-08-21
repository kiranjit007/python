


def db0(pq,internalbibid,coldata,final_output):
    dictdb0 = {}
    if pq.get('CompleteReference').lower() == 'false' and pq.get('InternalBibId') != internalbibid:
        dictdb0['Id'] = pq.get('InternalBibId')
        dictdb0['ReferenceString'] = pq.get('FullReferenceString')
        coldata.insert_one(dictdb0)
        final_output.append({'status':'Incomplete','ref':dictdb0})
        return 00



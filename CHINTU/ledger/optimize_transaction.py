class optimize_transaction:

    def __init__(self,transaction_list):
        self.transaction_list=transaction_list

    def resolve(self):

        participants_list = set({})

        [participants_list.add(participant[0])
         for participant in self.transaction_list]

        [participants_list.add(participant[2])
         for participant in self.transaction_list]

        participants_summary = {}

        for participant in participants_list:
            participants_summary[participant] = 0

        for transaction in self.transaction_list:
            participants_summary[transaction[0]] += transaction[1]
            participants_summary[transaction[2]] -= transaction[1]

        owe=[]
        ewo=[]

        for key,value in participants_summary.items():
            if value<0:
                owe.append([key,value])
            if value>0:
                ewo.append([key,value])

        owe=sorted(owe,key=lambda l:l[1])
        ewo=sorted(ewo,key=lambda l:l[1], reverse=True)

        final_summary=[]
        c_iter_owe=0
        d_iter_ewo=0

        while c_iter_owe<len(owe):
            count=False
            while d_iter_ewo<len(ewo):
                if(abs(owe[c_iter_owe][1])==ewo[d_iter_ewo][1]):
                    final_summary.append([ewo[d_iter_ewo][0],ewo[d_iter_ewo][1],owe[c_iter_owe][0]])
                    ewo.pop(d_iter_ewo)
                    count=True
                    break
                d_iter_ewo=d_iter_ewo+1
            if count==True:
                owe.pop(c_iter_owe)
            else:
                c_iter_owe=c_iter_owe+1

        c_iter_owe=0
        d_iter_ewo=0
        while c_iter_owe<len(owe):
            if abs(owe[c_iter_owe][1])<ewo[d_iter_ewo][1]:
                final_summary.append([ewo[d_iter_ewo][0],abs(owe[c_iter_owe][1]),owe[c_iter_owe][0]])
                ewo[d_iter_ewo][1]+=owe[c_iter_owe][1]
                c_iter_owe=c_iter_owe+1
            elif abs(owe[c_iter_owe][1])==ewo[d_iter_ewo][1]:
                final_summary.append([ewo[d_iter_ewo][0],abs(owe[c_iter_owe][1]),owe[c_iter_owe][0]])
                c_iter_owe=c_iter_owe+1
                d_iter_ewo=d_iter_ewo+1
            else:
                final_summary.append([ewo[d_iter_ewo][0],ewo[d_iter_ewo][1],owe[c_iter_owe][0]])
                owe[c_iter_owe][1]+=ewo[d_iter_ewo][1]
                d_iter_ewo=d_iter_ewo+1

        print(final_summary)
li=[["abhishek",400,"mayank"],["mayank",1000,"varad"],["abhishek",400,"S"],["D",1000,"mayank"],["varad",200,"F"]]
op=optimize_transaction(li)

op.resolve()

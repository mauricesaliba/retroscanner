import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# open text file team 01
file_team_01 = open("C:/Users/maurice.saliba/Downloads/DELETE DEC/team_01.txt", "r")
text_team_01 = file_team_01.read()
file_team_01.close()


# open text file team 02
file_team_02 = open("C:/Users/maurice.saliba/Downloads/DELETE DEC/team_02.txt", "r")
text_team_02 = file_team_02.read()
file_team_02.close()


# open text file team 03
file_team_03 = open("C:/Users/maurice.saliba/Downloads/DELETE DEC/team_03.txt", "r")
text_team_03 = file_team_03.read()
file_team_03.close()


# open text file team 04
file_team_04 = open("C:/Users/maurice.saliba/Downloads/DELETE DEC/team_04.txt", "r")
text_team_04 = file_team_04.read()
file_team_04.close()

# open text file team 05
file_team_05 = open("C:/Users/maurice.saliba/Downloads/DELETE DEC/team_05.txt", "r")
text_team_05 = file_team_05.read()
file_team_05.close()

# open text file team DE
file_team_DE = open("C:/Users/maurice.saliba/Downloads/DELETE DEC/team_DE.txt", "r")
text_team_DE = file_team_DE.read()
file_team_DE.close()
print(text_team_DE)

for word, replacement in {"2021 Participants Anna Maria Cassola":"", "Samantha Catania":"","Magdalena Kosmala":"", "Sandy Farrugia":"","Alexander Vella":"","Maria Aquilina":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_01 = text_team_01.replace(word, replacement)

for word, replacement in {"Norbert Debono":"", "Alison Zammit":"","Unknown User (olivier.sin)":"", "Patrick S":"","Etienne A. Vella":"","Minakshee Kumari":"","Gerald Sammut":"","Atmanand Ballea":"","2021 Participants":"","Paul Buttigieg":"","Nadeem M. Korumtallea":"", "Binalfew K Mekonnen":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_02 = text_team_02.replace(word, replacement)

for word, replacement in {"2021 Participants":"", "Norbert Grech":"","Nick Scerri":"", "Sagar MT":"","Unknown User (manojdeep.sn)":"","Ingrid Gatt":"","Deepeentee Jhoomuck":"","Unknown User (olivier.sin)":"","Martin Degiorgio":"","Ashvin Brijmohun":"", "Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_03 = text_team_03.replace(word, replacement)

for word, replacement in {"2021 Participants":"", "Frankie Tanti":"","Unknown User (massimo.saliba)":"", "Martin Degiorgio":"","Ingrid Gatt":"","Charlie Farrugia":"", "Unknown User (joseph.bonnici)":"","Unknown User (donald.debono)":"","Geoffrey Farrugia":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_04 = text_team_04.replace(word, replacement)

for word, replacement in {"2021 Participants":"", "Lyndsey Gatt":"","Unknown User (raja.sekhar)":"", "Sean Galea":"","Jurgen Camilleri":"","Stephanie Aquilina":"","Hanumantha Rao":"","Ashvin Brijmohun":"","Caroline Zahra":"","Maria Cassar":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_05 = text_team_05.replace(word, replacement)

for word, replacement in {"2021 Participants Gilbert Micallef":"", "Daniel Fenech":"","Getter Fernandes":"", "Unknown User (philip.mifsud)":"","Mark E. Farrugia":"","Luke Duca":"","Zack Spiteri":"","Sandro Pace":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_DE = text_team_DE.replace(word, replacement)

#code found in https://www.mygreatlearning.com/blog/bag-of-words/

CountVec = CountVectorizer(ngram_range=(2,2),  # to use bigrams ngram_range=(2,2)
                           stop_words='english',
                           min_df=2,
                           max_df=4)
# transform
Count_data = CountVec.fit_transform([text_team_01, text_team_02,text_team_03,text_team_04,text_team_05,text_team_DE])

# create dataframe
cv_dataframe = pd.DataFrame(Count_data.toarray(), columns=CountVec.get_feature_names_out())
cv_dataframe_tx =cv_dataframe.transpose()
cv_dataframe_tx.columns=['team_01','team_02','team_03','team_04','team_05','team_DE']
cv_dataframe_tx=cv_dataframe_tx.sort_values(by=['team_02'],ascending=False)
print(cv_dataframe_tx)
cv_dataframe_tx.to_csv("C:/Users/maurice.saliba/Downloads/DELETE DEC/BoW.csv")
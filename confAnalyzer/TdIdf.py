import pandas as pd
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud


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

for word, replacement in {"2021 Participants":"", "Anna Maria Cassola":"", "Samantha Catania":"","Magdalena Kosmala":"", "Sandy Farrugia":"","Unknown User (olivier.sin)":"","Alexander Vella":"","Maria Aquilina":"","Ashvin Brijmohun":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_01 = text_team_01.replace(word, replacement)

for word, replacement in {"Norbert Debono":"", "Alison Zammit":"","Unknown User (olivier.sin)":"", "Patrick S":"","Etienne A. Vella":"","Minakshee Kumari":"","Gerald Sammut":"","Atmanand Ballea":"","2021 Participants":"","Paul Buttigieg":"","Nadeem M. Korumtallea":"", "Binalfew K Mekonnen":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_02 = text_team_02.replace(word, replacement)

for word, replacement in {"2021 Participants":"", "Norbert Grech":"","Nick Scerri":"", "Sagar MT":"","Unknown User (manojdeep.sn)":"","Ingrid Gatt":"","Deepeentee Jhoomuck":"","Unknown User (olivier.sin)":"","Martin Degiorgio":"","Ashvin Brijmohun":"", "Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_03 = text_team_03.replace(word, replacement)

for word, replacement in {"2021 Participants":"", "Frankie Tanti":"","Unknown User (massimo.saliba)":"", "Martin Degiorgio":"","Ingrid Gatt":"","Charlie Farrugia":"", "Unknown User (joseph.bonnici)":"","Unknown User (donald.debono)":"","Geoffrey Farrugia":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_04 = text_team_04.replace(word, replacement)

for word, replacement in {"2021 Participants":"", "Lyndsey Gatt":"","Unknown User (raja.sekhar)":"", "Sean Galea":"","Jurgen Camilleri":"","Stephanie Aquilina":"","Hanumantha Rao":"","Ashvin Brijmohun":"","Caroline Zahra":"","Maria Cassar":"","David Vella":"", "Unknown User (rama.gollapalli)":"", "Unknown User (zahhir.ebrahim)":"", "Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_05 = text_team_05.replace(word, replacement)


for word, replacement in {"2021 Participants":"", "Daniel Fenech":"","Gilbert Micallef":"", "Getter Fernandes":"", "Unknown User (philip.mifsud)":"","Mark E. Farrugia":"","Luke Duca":"","Zack Spiteri":"","Sandro Pace":"","Unknown User (deepak.giri)":"", "Unknown User (dmitrijs.berezins)":"","Retrospective":"", "retrospective":"","What did we do well?":"", "What should we have done better?":"","Actions":""}.items():
    text_team_DE = text_team_DE.replace(word, replacement)

#code found in https://www.mygreatlearning.com/blog/bag-of-words/

my_stop_words = text.ENGLISH_STOP_WORDS.union(["sprint","tasks","date"])

# without smooth IDF
print("Without Smoothing:")
# define tf-idf
tf_idf_vec = TfidfVectorizer(use_idf=True,
                             smooth_idf=False,
                             ngram_range=(2, 2), stop_words=my_stop_words)  # to use only  bigrams ngram_range=(2,2)
# transform
tf_idf_data = tf_idf_vec.fit_transform([text_team_01, text_team_02,text_team_03,text_team_04,text_team_05,text_team_DE])

# create dataframe
team_dataframe_columns=['team_01', 'team_02', 'team_03', 'team_04', 'team_05', 'team_DE']
tf_idf_dataframe = pd.DataFrame(tf_idf_data.toarray(), columns=tf_idf_vec.get_feature_names_out()).transpose()
tf_idf_dataframe.columns=team_dataframe_columns
print(tf_idf_dataframe)
print("\n")

# with smooth
tf_idf_vec_smooth = TfidfVectorizer(use_idf=True,
                                    smooth_idf=True,
                                    ngram_range=(3, 3), stop_words=my_stop_words)

tf_idf_data_smooth = tf_idf_vec_smooth.fit_transform([text_team_01, text_team_02,text_team_03,text_team_04,text_team_05,text_team_DE])

print("With Smoothing:")
tf_idf_dataframe_smooth = pd.DataFrame(tf_idf_data_smooth.toarray(), columns=tf_idf_vec_smooth.get_feature_names_out()).transpose()
tf_idf_dataframe_smooth.columns=team_dataframe_columns
print(tf_idf_dataframe_smooth)

# change the value to black
def black_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl(0,100%, 1%)")
# set the wordcloud background color to white
# set max_words to 1000
# set width and height to higher quality, 3000 x 2000
wordcloud = WordCloud(background_color="white", width=3000, height=2000, max_words=500).generate_from_frequencies(tf_idf_dataframe_smooth['team_01'])
# set the word color to black
wordcloud.recolor(color_func = black_color_func)
# set the figsize
plt.figure(figsize=[15,10])
# plot the wordcloud
plt.imshow(wordcloud, interpolation="bilinear")
# remove plot axes
plt.axis("off")


#wordcloud = WordCloud().generate_from_frequencies(tf_idf_dataframe_smooth['team_02'])
#plt.imshow(wordcloud)

plt.show()
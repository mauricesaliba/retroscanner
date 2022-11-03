import requests
import pandas as pd
from getpass import getpass
import removehtmlcode
import re
from datetime import datetime

#TODO - To create a methdd and return a dataframe that contains retrospectives data. Each row would have  retrospective


def parse_title(title):

    title=title[0:19].strip()
    elements = title.split('-')

    sprint = elements[0]
    team = elements[1]

    sprint_start_date_str = elements[2] + " 2021"
    sprint_end_date_str = elements[3] + " 2021"

    sprint_start_date = datetime.strptime(sprint_start_date_str, '%b%d %Y')
    sprint_end_date = datetime.strptime(sprint_end_date_str, '%b%d %Y')
    parsed_elements = [sprint, team, sprint_start_date, sprint_end_date]
    return parsed_elements


contentApiUrl = '/rest/api/content'


# Change these based on your instance
confluenceBaseUrl = 'http://confluence.corporate.intra:8080'
pageId_retro_pages_top = '109910250'

username = 'maurice.saliba'
password = getpass('Input password:')

#TODO = make the below dynamically built and not hard coded by using the next link in returned response
#requestUrl_get_retro_page = '{confluenceBaseUrl}{contentApiUrl}/{pageId}?expand=body.view.value'.format(confluenceBaseUrl = confluenceBaseUrl, contentApiUrl = contentApiUrl, pageId = pageId_retro_page_example)
requestUrl_get_retro_pages_all_01 = '{confluenceBaseUrl}{contentApiUrl}/search?cql=parent={pageId}&expand=body.view.value&limit=50'.format(confluenceBaseUrl = confluenceBaseUrl, contentApiUrl = contentApiUrl, pageId = pageId_retro_pages_top)
requestUrl_get_retro_pages_all_02 = '{confluenceBaseUrl}{contentApiUrl}/search?cql=parent={pageId}&expand=body.view.value&limit=50&start=50'.format(confluenceBaseUrl = confluenceBaseUrl, contentApiUrl = contentApiUrl, pageId = pageId_retro_pages_top)
requestUrl_get_retro_pages_all_03 = '{confluenceBaseUrl}{contentApiUrl}/search?cql=parent={pageId}&expand=body.view.value&limit=50&start=100'.format(confluenceBaseUrl = confluenceBaseUrl, contentApiUrl = contentApiUrl, pageId = pageId_retro_pages_top)


request_response_retro_page_get_all_01=requests.get(requestUrl_get_retro_pages_all_01, auth=(username, password))
request_response_retro_page_get_all_02=requests.get(requestUrl_get_retro_pages_all_02, auth=(username, password))
request_response_retro_page_get_all_03=requests.get(requestUrl_get_retro_pages_all_03, auth=(username, password))

#request_response_retro_page_get_all=request_response_retro_page_get_all_01.join(request_response_retro_page_get_all_02).join(requestUrl_get_retro_pages_all_03)
#print(requestUrl_get_retro_pages_all)
#print(request_response_retro_page_get_all_01.json())

json_out_01=request_response_retro_page_get_all_01.json()
json_out_02=request_response_retro_page_get_all_02.json()
json_out_03=request_response_retro_page_get_all_03.json()

results_01=json_out_01["results"]
results_02=json_out_02["results"]
results_03=json_out_03["results"]


results_all=[]
results_all.extend(results_01)
results_all.extend(results_02)
results_all.extend(results_03)

df = pd.DataFrame(results_all)

df['body_words'] = df['body'].astype(str).str.replace("{'view': {'value': '",'',regex=True)

df['body_words'] =  df['body_words'].map(lambda x: re.sub(r"</div>', 'representation': 'storage', '_expandable': {'webresource': '', 'content': '/rest/api/content/\d+'}}, '_expandable': {'editor': '', 'export_view': '', 'styled_view': '', 'storage': '', 'anonymous_export_view': ''}}", '', x))
df['body_words'] =  df['body_words'].map(lambda x: re.sub(r"\\n", '', x))
df['body_words'] =  df['body_words'].map(lambda x: re.sub(r"\\xa0", ' ', x))


df['body_words'] = df["body_words"].map(lambda x: removehtmlcode.remove_html_code(x))


parsed_title_series=df['title'].map(lambda x: parse_title(x))
df_sprint_info=pd.DataFrame(parsed_title_series)
df_sprint_info[['Sprint_no','Team','sprint_start_date','sprint_end_date']]=pd.DataFrame(df_sprint_info.title.tolist(), index= df_sprint_info.index)
df_sprint_info=df_sprint_info.drop(['title'], axis=1)


frames=[df,df_sprint_info]
df_retros=pd.concat(frames,axis=1)
df_retros.to_csv("C:/Users/maurice.saliba/Downloads/DELETE DEC/delete.csv")



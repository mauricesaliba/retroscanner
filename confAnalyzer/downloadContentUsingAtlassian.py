from getpass import getpass
from atlassian import Confluence
from removehtmlcode import remove_html_code

password = getpass('Input password:')

confluence = Confluence(
    url='http://confluence.corporate.intra:8080/',
    username='maurice.saliba',
    password=password)


#confluence.get_page_id(space, title)
#space=confluence.get_page_space("109910250")
#spaces = confluence.get_all_spaces(start=0, limit=2, expand=None)



# Returns the word content of a page
out = confluence.get_page_by_title('ITDev', '059-T05-JUL26-AUG06-Retrospective', start=None, limit=None, expand="body.view")
htmlout=out["body"]["view"]["value"]
#TODO - extract fron panels related to 'what we have done well' and 'what we should improve' and 'actions'
print(remove_html_code(htmlout))
#90574796


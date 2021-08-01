import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('evocative-tower-300912-dc0f7ff590fb.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Bröllopsplanering").worksheets()[-1]

# Extract and print all of the values
list_of_guests = sheet.get_all_values()

texed_list_of_guests = []

for i, (id, name, desc) in enumerate(list_of_guests):
    texed_list_of_guests.append('    \\noindent\\scriptsize %s %s \\tiny \\\\ \\emph{%s} \\newline \\par \n' % (id.replace('#', '\#'), name, desc.replace('#', '\#')))


with open('preamble.tex') as f:
    preamble = f.readlines()

with open('postamble.tex') as f:
    postamble = f.readlines()

with open('menu_to_print.tex', 'w') as f:
    f.writelines(preamble+texed_list_of_guests+postamble)



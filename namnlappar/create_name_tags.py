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
texed_list_of_guests.append('\\vspace{3cm}\n')
texed_list_of_guests.append('\\begin{Row}\n')

for i, (id, name, desc, table) in enumerate(list_of_guests):
    if i > 0 and i % 2 == 0:
        texed_list_of_guests.append('\\end{Row}\\\\\n')
        texed_list_of_guests.append('\\vfill\n')
        texed_list_of_guests.append('\\begin{Row}\n')
    texed_list_of_guests.append('    \\begin{Cell}{1}\n')
    texed_list_of_guests.append('        \\begin{overpic}[angle=-90,width=0.5\\paperwidth]{leaf.png}\n')
    texed_list_of_guests.append('            \\put(20,10){\\raisebox{\\depth}{\\scalebox{-1}[-1]{%s}}}\n' % (name))
    texed_list_of_guests.append('        \\end{overpic}\\\\\n')
    texed_list_of_guests.append('        \\begin{overpic}[angle=90,width=0.5\\paperwidth]{leaf.png}\n')
    texed_list_of_guests.append('            \\put(10,25){%s}\n' % (name))
    texed_list_of_guests.append('        \\end{overpic}\n')
    texed_list_of_guests.append('    \\end{Cell}\n')

texed_list_of_guests.append('\\end{Row}\n')

with open('tag_preamble.tex') as f:
    preamble = f.readlines()

with open('tag_postamble.tex') as f:
    postamble = f.readlines()

with open('tags.tex', 'w') as f:
    f.writelines(preamble+texed_list_of_guests+postamble)




import os


open_api_key = os.environ.get('OPENAI_API_KEY')


####!!!!!!!!!remember to change to relative path later!!!!!!!!!!!!!!
local_directory = os.getcwd()
### please note that we have not included any params from the data-processing stage
### only included as of "ml_logic"


persist_directory = local_directory +'/askandrew/chroma/' #setting the location of the local directory

### ML_LOGIC

#

import os
import time
import re
import shutil

user = '1001c'
character_name = 'Wister'

save_dir = 'C:/Users/' + user +'/AppData/Local/Larian Studios/Baldur\'s Gate 3/PlayerProfiles/Public/Savegames/Story/'

saves = []
reg_compile = re.compile(character_name + '.*')
for dirpath, dirnames, filenames in os.walk(save_dir):
    saves = saves + [dirname for dirname in dirnames if  reg_compile.match(dirname)]


for save in saves:
    save_path = save_dir + save
    save_timestamp = os.path.getmtime(save_path)
    unformatted_time = time.ctime(save_timestamp)
    time_obj = time.strptime(unformatted_time)
    output_timestamp = time.strftime("%Y%m%d_%H%M%S", time_obj)
    output_name = save + '_' + output_timestamp

    shutil.make_archive('./saves/' + output_name, 'zip', save_path)
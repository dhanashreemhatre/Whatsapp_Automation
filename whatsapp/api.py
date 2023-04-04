from flask import Flask,render_template,request,Response
from datetime import datetime
import pywhatkit as pwt
import pandas as pd


app = Flask(__name__, template_folder='./templates')

def send_whatsapp(data_file_excel,message_file_text):
    df=pd.read_excel(data_file_excel,dtype={"Contact":str})
    name=df['Name'].values
    contact=df['Contact'].values
    files=message_file_text

    with open (files) as f:
        file_data=f.read()
    zipped=zip(name,contact)

    now=datetime.now()
    

    current_minute = int(now.strftime("%M")) # the next upcoming minute
    upcoming_minute = (current_minute + 1) % 60

    for (a,b) in zipped:
        msg = file_data.format(a)
        contact_no = b
        current_hour = int(now.strftime("%H"))
        wait_time = 10 # time to wait before sending the message (minute)
        close_tab = True # close the browser tab
        close_time = 3 # time to close the tab (minute)

        pwt.sendwhatmsg(contact_no, msg, current_hour,
                          upcoming_minute, wait_time, close_tab, close_time)
        upcoming_minute += 1
      


@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/send',methods=['POST'])
def send():
   excel_file=request.files["exl_file"]
   text_file=request.files["txt_file"]
   ex_file_path = excel_file.filename
   txt_file_path=text_file.filename
   send_whatsapp(ex_file_path,txt_file_path)
   return "done..."



if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)


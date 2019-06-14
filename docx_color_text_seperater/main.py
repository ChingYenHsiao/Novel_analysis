import sys
from PyQt5.QtWidgets import QDialog, QApplication,QFileDialog
from docx_color_seperate import Ui_Docx_color_seperate
#from GenericThread  import GenericThread
#from PyQt5.QtCore import *

import docx

import numpy as np
import matplotlib.pyplot as plt


#https://moon-half.info/p/2327
#pyinstaller -F hello.py
    
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Docx_color_seperate()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.selectFile)
        self.ui.buttonBox.clicked.connect(self.color_seperate)
        self.show()
        self.filename = ''
    def color_seperate(self):
        if self.filename[-5:] == ".docx": 
            doc = docx.Document(self.filename)
                   
            color_dic = {}
            color_rgb_dic = {}
            color_sentence = {}
            for index,Paragraph  in enumerate( doc.paragraphs):
                if len(Paragraph.text)==0:
                        continue
                color_rgb_str = Paragraph.runs[0].font.color.rgb.__str__()

                if color_rgb_str not in color_dic:
                    color_dic[color_rgb_str] = 1
                    color_sentence[color_rgb_str] = [ ]
                    color_sentence[color_rgb_str].append( Paragraph.text )
                else:
                    color_sentence[color_rgb_str].append( Paragraph.text )

            for k in  color_dic.keys():
                if k != "None":
                    color_rgb_dic[k] = [ int(k[:2]  , 16) , int(k[2:4]  , 16) , int(k[4:6]  , 16)  ]
                    
            sorted_color_sen_length = sorted(color_rgb_dic.items(), key=lambda d: len( color_sentence[d[0]]))[::-1]
            #print (sorted_color_sen_length)


            col_number = len(color_rgb_dic) 
            limit = 9
            if col_number > limit:
                col_number = limit
                
            #plt.clf()
            plt.figure(figsize=(25,25)) 

            no = 1
            for index, k in enumerate( sorted_color_sen_length[:col_number])  :
                #[('274E13', [39, 78, 19]) > '274E13'
                k = k[0]
     
                plt.subplot(1,col_number,no)
                no+=1
                plt.title(k)

                print( 'Color ',k ,[color_rgb_dic[k]])
                plt.imshow(  [[  (  color_rgb_dic[k][0] , color_rgb_dic[k][1] , color_rgb_dic[k][2]  ) ]] )

            plt.savefig(self.filename.split("/")[-1][:-5]+'.png')

            count = 0

            fp = open('./None_black.txt','w',encoding="utf-8")
            fp_wc = open('./Word_count.txt','w',encoding="utf-8")
            fp_wc.write('統計最多10種顏色的字\n')
            for s in color_sentence['None']:
                count+=len(s)
                fp.write(s+'\n')
            #print('Color None(black) has ',len(color_sentence['None']), 'sentences.\t',count,' characters.')
            fp_wc.write('Color None(black) has '+str ( len(color_sentence['None']) ) + ' sentences.\t'+str(count)+' characters.\n')
            
            
            for index, k in enumerate( sorted_color_sen_length[:col_number])  :
                #[('274E13', [39, 78, 19]) > '274E13'           
                    k = k[0]
                    count = 0
                    fp = open('./'+k+'.txt','w',encoding="utf-8")
                    for s in color_sentence[k]:
                        count+=len(s)
                        fp.write(s+'\n')
                    print('Color ',k,'has ',len(color_sentence[k]), 'sentences.\t',count,' characters.')
                    fp_wc.write('Color '+k+' has '+str ( len(color_sentence[k]) ) + ' sentences.\t'+str(count)+' characters.\n')
                    
            fp.close()
            fp_wc.close()

    def selectFile(self):
        self.ui.lineEdit.setText('')
        self.filename = QFileDialog.getOpenFileName()[0]
        if ".docx" == self.filename.split("/")[-1][-5:]:
            self.ui.lineEdit.setText(self.filename)

        
def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
# coding=gbk
from tkinter import *
from tkinter import ttk
import os
import time
import tkinter.font as tkFont
import threading

def showWelcome():
	 sw = root.winfo_screenwidth()
	 #�õ���Ļ���
	 sh = root.winfo_screenheight()
	 #�õ���Ļ�߶�
	root.overrideredirect(True)
	 root.attributes("-alpha", 1)#����͸���ȣ�1Ϊ��͸����0Ϊȫ͸����
	 x=(sw-475)/2
	 y=(sh-200)/2
	 #���ô���λ����Ļ�в�
	 root.geometry("475x200+%d+%d" %(x,y))
	 root['bg']='black'
	 #���뻶ӭͼƬ��������logo
	 if os.path.exists('./Lib/img/welcome.png'):
		  print("Lib/img exist")
		  bm = PhotoImage(file = './Lib/img/welcome.png')
		  lb_welcomelogo = Label(root, image = bm,bg='black')
		  lb_welcomelogo.bm = bm
		  lb_welcomelogo.place(x=0, y=10,)
	#�������֣�������ʾ�����߻����
	lb_welcometext = Label(root, text = 'Welcome to use Long_xu application',
     		 fg='lightgray',bg='black',font=('��������', 22))
	 lb_welcometext.place(x=0, y=91,width=475,height=100)

def closeWelcome():
	#���û�ӭҳͣ��ʱ��
	 for i in range(2):
		  rootMSCT.attributes("-alpha", 0)#����͸����
		  time.sleep(1)
	 rootMSCT.attributes("-alpha", 1)#����͸����
	 root.destroy()
rootMSCT= Tk()  #����Ӧ�ó���������
rootMSCT.title("Long_xu welcome v1.0");
rootMSCT.attributes("-alpha", 0) #͸��״̬�¼���������

msw = rootMSCT.winfo_screenwidth()
msh = rootMSCT.winfo_screenheight()
m_x=(msw-600)/2
m_y=(msh-430)/2
rootMSCT.geometry("600x430+%d+%d" %(m_x,m_y))
global root
#������ӭ���洰��
root = Toplevel()
tMain=threading.Thread(target=showWelcome)
tMain.start();
t1=threading.Thread(target=closeWelcome)
t1.start();
'''
�����ڳ������
'''
rootMSCT.mainloop()
��������������������������������
��Ȩ����������ΪCSDN������Long_xu����ԭ�����£���ѭ CC 4.0 BY-SA ��ȨЭ�飬ת���븽��ԭ�ĳ������Ӽ���������
ԭ�����ӣ�https://blog.csdn.net/Long_xu/article/details/86538310
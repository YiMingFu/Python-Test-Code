                                                                                                                                                                                                                  # -*- coding: utf-8 -*-
from PIL import Image
import os  
import time
import json
#每秒53像素
# a = os.popen("adb devices") 
# print(a.read())
# os.popen('adb shell screencap -p /sdcard/autojump.png') 
# os.popen("adb pull /sdcard/autojump.png .")
# while 1:	
# 	os.popen('adb shell input tap 870 1540')#重现开始游戏按钮
# 	time.sleep(3)
# 	os.popen('adb shell input tap 500 1540')#开始游戏
# 	print "3!"
# 	time.sleep(1)
# 	print "2!"
# 	time.sleep(1)
# 	print "1!"
# 	print "发射！"
# 	time.sleep(2.54)
# 	os.popen('adb shell input tap 500 1540')
# 	print "脱离一级火箭"
# 	time.sleep(1.8)
# 	os.popen('adb shell input tap 500 1540')
# 	print "脱离二级火箭"
# 	time.sleep(1.56)
# 	os.popen('adb shell input tap 500 1540')
# 	print "脱离三级火箭"
# 	time.sleep(1)
# 	os.popen('adb shell input tap 500 1540')
# 	print "脱离四级火箭"
# 	time.sleep(0.1)
# 	os.popen('adb shell input tap 500 1540')
# 	print "脱离五级火箭"
# time.sleep(0.3)
# os.popen('adb shell input tap 500 1540')
# print "脱离六级火箭"
# time.sleep(1.5)



 # adb shell dumpsys package>package.txt
# a = os.popen("adb devices")  
# print(a.read())


# b = os.popen('adb shell dumpsys package com.xiaozhu.xzdz')#  查  看  包  名
# b = os.popen('adb shell am start com.xiaozhu.xzdz/.splash.activity.XZStartupPicActivity')# 打 开 小 猪


XiaozhuPage_1 = (255,69,128,255)#主界面锚点
XiaozhuPage_2 = (255,64,129,255)#消息界面锚点
XiaozhuPage_3 = (33,33,33,255)#消息界面锚点
XiaozhuPage_4 = (230, 219, 189, 255)#房间（1）东木园  
XiaozhuPage_4_1 = (255, 64, 129, 255)#房间（1）东木园  
isXiaozhu = True
def CutImage(x,y):
	time.sleep(1)#安全时间
	os.popen('adb shell screencap -p /sdcard/autojump.png') 
	os.popen("adb pull /sdcard/autojump.png .")
	im = Image.open("/Users/Frozen/Desktop/autojump.png")
	pixel = im.getpixel((x,y))
	print pixel
	return pixel


def Xiaozhu():
	devices = os.popen("adb devices")
	print(json.dumps('开始检测小猪日期，连接程序成功！\n').decode("unicode-escape")+devices.read())
	os.popen('adb shell am start com.xiaozhu.xzdz/.splash.activity.XZStartupPicActivity')# 打 开 小 猪
	print(json.dumps('成功打开程序！').decode("unicode-escape"))
	time.sleep(12)
	pixel = CutImage(540,143)
	if XiaozhuPage_1 == pixel:
		print(json.dumps('成功打开消息界面！').decode("unicode-escape"))
		os.popen('adb shell input tap 670 1800')#进入小猪程序后点消息  X Y 
		pixel = CutImage(670,1787)
		if XiaozhuPage_2 == pixel:
			print(json.dumps('成功打开聊天窗口！').decode("unicode-escape"))
			os.popen('adb shell input tap 120 330')#进入小猪程序后点消息  X Y
			pixel = CutImage(1000,130)
			if XiaozhuPage_3 == pixel:
				print(json.dumps('成功打开Cindy个人界面！').decode("unicode-escape"))
				os.popen('adb shell input tap 1000 130')#进入小猪程序后点消息  X Y
				time.sleep(3)
				os.popen('adb shell input swipe 540 590 540 0 100 ')
				pixel = CutImage(200,600)
				if XiaozhuPage_4 == pixel:
					print(json.dumps('成功打开东木园界面！').decode("unicode-escape"))
					os.popen('adb shell input tap 200 600')#进入小猪程序后点消息  X Y
					time.sleep(8)#等待加载界面
					os.popen('adb shell input swipe 540 1000 540 0 100 ')
					pixel = CutImage(930,1850)


	# time.sleep(1)
	# os.popen('adb shell input tap 120 330')#进入Cindy聊天界面
	# time.sleep(1)
	# os.popen('adb shell input tap 100 450')#找到Cindy个人信息


Xiaozhu()




























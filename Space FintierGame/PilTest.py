# -*- coding: utf-8 -*-
import os  
import time
from PIL import Image
from PIL import ImageEnhance
# im = Image.open("/Users/Frozen/Desktop/autojump.png")
# print(im.format, im.size, im.mode)
# im = ImageEnhance.Contrast(im)
# im.enhance(2).show("100% more contrast")
# width = im.width
# height = im.height
# image_list = []
# for x in range(height):
#     scanline_list = []
#     for y in range(width):
#         pixel = im.getpixel((y, x))
#         scanline_list.append(pixel)
#     image_list.append(scanline_list)
# print(image_list[])

# a = os.popen("adb devices") 
# print(a.read())



im = None
RocketDownMax = (95, 90, 90, 255)
RocketDownMin = (90, 80, 80, 255)
RocketDetachMax = (100, 65, 55, 255)
RocketDetachMin = (20, 20, 20, 255)
x = 400
y = 0
w = 250
h = 1920
tempH = [0]
pixelSize = [0]
def CutImage():
	global im
	os.popen('adb shell screencap -p /sdcard/autojump.png') 
	os.popen("adb pull /sdcard/autojump.png .")
	im = Image.open("/Users/Frozen/Desktop/autojump.png")
	region = im.crop((x, y, x+w, y+h))
	region.save("/Users/Frozen/Desktop/autojump.png")
	im = Image.open("/Users/Frozen/Desktop/autojump.png")
def Analysis():
	global im
	height = 1700
	tempHeight = height
	tempIgnore = True
	for i in range(height):
		height=height-1
		pixel = im.getpixel((140,height))
		# print height
		# print pixel
		if pixel < RocketDownMax and pixel > RocketDownMin and height >1500:
			# print '可以认定为火箭底部'
			tempH.append(height)
		# if tempIgnore :
		# 	if pixel < RocketDetachMax and pixel > RocketDetachMin and height <1500 and height >500:
		if pixel < RocketDetachMax and pixel > RocketDetachMin and tempIgnore==True and height <1600 and height >300:
			# print '找到了'
			tempIgnore = False
			tempHeight = height-10
			tempH.append(height)
			# os.popen('adb shell input tap 870 1540')
		if tempHeight == height:
		 	tempIgnore = True
		 	tempHeight = 0
 	# print tempH
	a = len(tempH)
	for j in range(a):
		try:
			pixelSize.append((tempH[j+1]-tempH[j+2]))
		except:
			print pixelSize
			break
def Click():
	os.popen('adb shell input tap 500 1540')#开始游戏
	print "------------------------------------------------3!"
	time.sleep(1)
	print "-------------------------------------2!"
	time.sleep(0.5)
	print "--------------------------1!"
	time.sleep(0.5)
	print "------------ 发射！"
	temp = len(pixelSize)
	for i in range(temp):
		print('i' , i)
		if i<(temp-0):
			print ("pixelSize",pixelSize[i])
			print ("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=",pixelSize[i]/50.0)
			time.sleep(pixelSize[i]/50.0) 
			os.popen('adb shell input tap 500 1540')#开始游戏
		if i>15:
			break
    # print pixelSize
	# print im.getpixel((540,540))
# image_list = []
# for x in range(height):
# 	print im.getpixel((height,height))
# 	print '/n'
# if __name__ == '__main__':
# while 1:
# 	print 'run'
# 	Click()

# Analysis()
while 1:
# 	Click().
	tempH = []
	pixelSize = []
	time.sleep(3)
	os.popen('adb shell input tap 870 1540')#重现开始游戏按钮
	time.sleep(3)
	CutImage()
	Analysis()
	time.sleep(1)
	Click()







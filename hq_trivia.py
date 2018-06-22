#googlesearch
from googlesearch import search
#read image
from PIL import Image
from pytesseract import image_to_string
#take a screenshot
import pyautogui
#get a html
import urllib3

def main():
	text_list = list()
	url_list = list()

	screenshot()
	text_list = get_text_from_image()
	url_list = get_url(text_list)
	html_text = get_html(url_list)
	size = len(text_list)
	for n in range(1,size):
		result1 = count_num_of_question(html_text, text_list[n])
		print(text_list[n] + " : " + str(result1))
	

#take a screenshot
def screenshot():
	im = pyautogui.screenshot(region=(1720, 330, 816, 780))
	im.save('/Users/fujishimareo/Desktop/HQtrivia/screan_shots/image.png')

#get text from a screenshot
def get_text_from_image():	
	WD = "/Users/fujishimareo/Desktop/HQtrivia/screan_shots/image.png"
	img = Image.open(WD)
	#reading text
	text = image_to_string(img, lang = 'eng')
	#split text to question and answers
	line = text.split("\n\n") 
	img.close()

	#printout to check
	line_num = 0
	for n in line:
		print(str(line_num) + " : " + n)
		line_num +=1
	print("********Finish to get text***********")

	return line

#get url from the text
def get_url(line):
	query = line[0]
	url_list = list()
	# for j in search(query, tld="co.in", num=5, stop=1, pause=2):
	for j in search(query, tld="co.in", num=3, stop=1, pause=1.0):
		url_list.append(j)

	#printout to check
	url_num = 0
	for n in url_list:
		print(str(url_num) + " url_list : " + n)
		url_num +=1
	print("********Finish to get url***********")

	return url_list

#get html from the url
def get_html(url_list):
	size = len(url_list)
	html_text = list()

	for n in range(0,size):
		url = url_list[n]
		http_pool = urllib3.connection_from_url(url)
		r = http_pool.urlopen('GET',url)
		html_text.append(r.data.decode('utf-8'))

	print("************ Finish to get html text **************")
	# print("size : " + str(len(html_text)))
	return html_text

def count_num_of_question(html_text, question):
	sum = 0
	for n in html_text:
		result = n.count(question)
		print(str(result))
		sum += result
	return sum

main()







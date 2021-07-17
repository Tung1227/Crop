import cv2 


origin_IMG = cv2.imread("tung.jpg") 
image=cv2.cvtColor(origin_IMG,cv2.COLOR_BGR2GRAY) 
cv2.imshow("",image)
cv2.waitKey(0)
edged = cv2.Canny(image, 10, 250) 
cv2.imshow("Edges", edged) 
cv2.waitKey(0) 
 
 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)) 
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel) 

 
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
 
for c in cnts: 
	peri = cv2.arcLength(c, True) 
	approx = cv2.approxPolyDP(c, 0.02 * peri, True) 
	cv2.drawContours(image, [approx], -1, (0, 255, 0), 2) 
idx = 2 
for c in cnts: 
	x,y,w,h = cv2.boundingRect(c) 
	if w>50 and h>50: 
		idx+=1 
		new_img=origin_IMG[y:y+h,x:x+w] 
		cv2.imwrite(str(idx) + '.png', new_img) 
		cv2.imshow("img",new_img)
cv2.waitKey(0) 
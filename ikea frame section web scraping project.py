#!/usr/bin/env python
# coding: utf-8

# In[33]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = "https://www.ikea.com/in/en/cat/frames-pictures-10757/"
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,"html.parser")
#print(soup)
soup.prettify


# In[34]:


import requests
r = requests.get(URL)
htmlcontent = r.content
print(htmlcontent)


# In[35]:


title=soup.title
print(title)


# In[36]:


soup = BeautifulSoup(htmlcontent,"html.parser")
print(soup)


# In[37]:


maindiv = soup.find_all("div",class_="plp-product-list__products")
print(maindiv)


# In[ ]:





# In[38]:


frame_main = soup.find_all(class_="plp-product-list__fragment")
print(frame_main)


# In[39]:


frame_name = soup.find_all(class_="pip-header-section__title--small notranslate")
print(frame_name)


# In[40]:


frame_size = soup.find_all(class_="pip-header-section__description-measurement")
print(frame_size)


# In[ ]:





# In[41]:


frame_price = soup.find_all(class_="pip-price")
print(frame_price)


# In[42]:


frame_rating = soup.find_all(class_="pip-rating pip-rating--small")
print(frame_rating)


# In[43]:


list1=[]
for i in range(0,11):
    list1.append(frame_name[i].get_text())
print(list1)
print(len(list1))


# In[44]:


list2=[]
for i in range((len(frame_size))):
    list2.append(frame_size[i].get_text())
print(list2)
print(len(list2))


# In[45]:


list3=[]
for i in range(0,11):
    list3.append(frame_price[i].get_text())
print(list3)
print(len(list3))


# In[46]:


list4=[]
for i in range(0,11):
    list4.append(frame_rating[i].get_text())
print(list4)
print(len(list4))


# In[47]:


import pandas as pd
Frame = pd.DataFrame({
"Frame Name": list1,
"Frame Size": list2,
"Frame Price":list3,
"Frame Rating":list4

})
Frame


# In[31]:


Frame.to_csv("ikea_frame_Section.csv",index= False)


# In[48]:


frame = pd.read_csv("ikea_frame_Section.csv")
frame


# In[ ]:


# second page for frame section 


# In[17]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
URL = "https://www.ikea.com/in/en/cat/frames-pictures-10757/"
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,"html.parser")
#print(soup)
soup.prettify


# In[49]:


import requests
r = requests.get(URL)
htmlcontent = r.content
print(htmlcontent)


# In[19]:


title1=soup.title
print(title1)


# In[20]:


maindiv1 = soup.find_all("div",class_="plp-product-list")
print(maindiv1)


# In[50]:


frame_main1 = soup.find_all(class_="plp-product-list__fragment")
print(frame_main1)


# In[51]:


frame_name1 = soup.find_all(class_="pip-header-section__title--small notranslate")
print(frame_name1)


# In[52]:


frame_size1 = soup.find_all(class_="pip-header-section__description")
print(frame_size1)


# In[53]:


frame_price1 = soup.find_all(class_="pip-price")
print(frame_price1)


# In[54]:


frame_rating1 = soup.find_all(class_="pip-rating pip-rating--small")
print(frame_rating1)


# In[55]:


list11=[]
for i in range((len(frame_name1))):
    list11.append(frame_name1[i].get_text())
print(list11)
print(len(list11))


# In[56]:


list12=[]
for i in range((len(frame_size1))):
    list12.append(frame_size1[i].get_text())
print(list12)
print(len(list12))


# In[57]:


list13=[]
for i in range((len(frame_price1))):
    list13.append(frame_price1[i].get_text())
print(list13)
print(len(list13))


# In[58]:


list14=[]
for i in range((len(frame_rating1))):
    list14.append(frame_rating1[i].get_text())
print(list14)
print(len(list14))


# In[59]:


import pandas as pd
Frame1 = pd.DataFrame({
"Frame Name": list11,
"Frame Size": list12,
"Frame Price":list13,
"Frame Rating":list14

})
Frame1


# In[ ]:


import os
os.getcwd()


# In[ ]:


Frame1.to_csv("ikea_frame_Section1.csv",index= False)


# In[60]:


frame1 = pd.read_csv("ikea_frame_Section1.csv")
frame1


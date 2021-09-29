from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv',encoding='latin1')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['new delhi', 'gurgaon', 'noida', 'faridabad', 'allahabad', 'bhubaneshwar', 'mangalore', 'mumbai', 'ranchi', 'patna', 'mysore', 'aurangabad', 'amritsar', 'puducherry', 'varanasi', 'nagpur', 'vadodara', 'dehradun', 'vizag', 'agra', 'ludhiana', 'kanpur', 'lucknow', 'surat', 'kochi', 'indore', 'ahmedabad', 'coimbatore', 'chennai', 'guwahati', 'jaipur', 'hyderabad', 'bangalore', 'nashik', 'pune', 'kolkata', 'bhopal', 'goa', 'chandigarh', 'ghaziabad', 'ooty', 'gangtok', 'shimla','mohali','panchkula','secunderabad']

location_text = ""
def price_range(price_range_text):
	dict_price = {'lesser than 300':300,'300 to 700':700,'More than 700':701}
	for key in dict_price:
		if key == price_range_text:
			return (dict_price.get(key))
def RestaurantSearch(City,Cuisine,Price): 
	price_range_number = price_range(Price)
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Average Cost for two'].apply(lambda x: x < price_range_number if price_range_number == 300 else (x <= price_range_number and x >= 300 ) if price_range_number == 700 else x >700 ))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def sendmail(MailID,dispatcher):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	
	global location_text
	mail_content = location_text
	dispatcher.utter_message("Email sent with message"+location_text)
	#The mail addresses and password
	sender_address = 'rrkk08041989@gmail.com'
	sender_pass = 'maxima89'
	receiver_address = MailID
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'Please find your restaurant search result.'   #The subject line
	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		sorted_results = results.sort_values('Aggregate rating',ascending=False)
		response=""
		mailresponse=""
		restaurant_exist = False
		if len(sorted_results) == 0:
			restaurant_exist = False
			response= "Sorry, no results found :("+ "\n"
			mailresponse=response
		else:
			sorted_results_top5 = sorted_results[:5]
			for restaurant in sorted_results_top5.iterrows():
				restaurant = restaurant[1]
				restaurant_exist = True
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"
			
			sorted_results_top10 = sorted_results[:10]
			for result1 in sorted_results_top10.iterrows():
				result1 = result1[1]
				mailresponse=mailresponse + F"Found {result1['Restaurant Name']} in {result1['Address']} has been rated {result1['Aggregate rating']} with avg cost {result1['Average Cost for two']} \n\n"
        
		dispatcher.utter_message("-----"+response)
		global location_text
		location_text = mailresponse
		return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		sendmail(MailID,dispatcher)
		dispatcher.utter_message("Email sent")
		return [SlotSet('mail_id',MailID)]
		
class VerifyLocation(Action):

    def name(self):
        return "verify_location"
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if not (self.verify_location(loc)):
            dispatcher.utter_message(
                "We do not operate in " + loc + " yet. Please try some other city.")
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        else:
            return [SlotSet('location', loc), SlotSet("location_ok", True)]

    def verify_location(self, loc):
        return loc.lower() in WeOperate	
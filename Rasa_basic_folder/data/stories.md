## interactive_story_1

* greet
   - utter_greet
* restaurant_search
   - utter_ask_location
* restaurant_search{"location": "New Delhi"}
   - slot{"location": "New Delhi"}
   - verify_location
   - slot{"location": "New Delhi"}
   - slot{"location_ok": true}
   - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
   - slot{"cuisine": "american"}
   - utter_ask_price
* restaurant_search{"price": "300 to 700"}
   - slot{"price": "300 to 700"}
   - action_search_restaurants
   - slot{"location": "New Delhi"}
   - slot{"restaurant_exist": true}
   - utter_ask_email_response
* email_response{"mail_response":"Yes"}
   - slot{"mail_response": "Yes"}
   - utter_ask_email
* email{"mail_id":"rakeshranjan0max89@gmail.com"}   
   - slot{"mail_id": "rakeshranjan0max89@gmail.com"}
   - action_send_mail
* goodbye
   - utter_goodbye
   - export
   

## interactive_story_2   
* greet
   - utter_greet
* restaurant_search{"location": "bikaner"}
   - slot{"location": "bikaner"}
   - verify_location
   - slot{"location": null}
   - slot{"location_ok": false}
   - utter_ask_location
* restaurant_search{"location": "mumbai"}
   - slot{"location": "mumbai"}
   - verify_location
   - slot{"location": "mumbai"}
   - slot{"location_ok": true}
   - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
   - slot{"cuisine": "american"}
   - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
   - slot{"price": "lesser than 300"}
   - action_search_restaurants
   - slot{"location": "mumbai"}
   - slot{"restaurant_exist": true}
   - utter_ask_email_response
* email_response{"mail_response":"Yes"}
   - slot{"mail_response": "Yes"}
   - utter_ask_email
* email{"mail_id":"rakeshranjan0max89@gmail.com"}   
   - slot{"mail_id": "rakeshranjan0max89@gmail.com"}
   - action_send_mail
   - utter_goodbye
   
## interactive_story_3   
* greet
   - utter_greet
* restaurant_search{"location": "bikaner"}
   - slot{"location": "bikaner"}
   - verify_location
   - slot{"location": null}
   - slot{"location_ok": false}
   - utter_ask_location
* restaurant_search{"location": "mumbai"}
   - slot{"location": "mumbai"}
   - verify_location
   - slot{"location": "mumbai"}
   - slot{"location_ok": true}
   - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
   - slot{"cuisine": "american"}
   - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
   - slot{"price": "lesser than 300"}
   - action_search_restaurants
   - slot{"location": "mumbai"}
   - slot{"restaurant_exist": true}
   - utter_ask_email_response
* email_response{"mail_response":"No"}
   - slot{"mail_response": "No"}
   - utter_goodbye   
   
## interactive_story_4   
* greet
   - utter_greet
* restaurant_search{"location": "bikaner"}
   - slot{"location": "bikaner"}
   - verify_location
   - slot{"location": null}
   - slot{"location_ok": false}
   - utter_ask_location
* restaurant_search{"location": "kolkata"}
   - slot{"location": "kolkata"}
   - verify_location
   - slot{"location": "kolkata"}
   - slot{"location_ok": true}
   - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
   - slot{"cuisine": "north indian"}
   - utter_ask_price
* restaurant_search{"price": "more than 700"}
   - slot{"price": "more than 700"}
   - action_search_restaurants
   - slot{"location": "kolkata"}
   - slot{"restaurant_exist": true}
   - utter_ask_email_response
* email_response{"mail_response":"No"}
   - slot{"mail_response": "No"}
   - utter_goodbye    
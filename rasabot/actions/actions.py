# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import os
import json
import argostranslate.package, argostranslate.translate


# Default Language is English
to_code = 'en'
def lang(text):
    from_code='en'

    if to_code=='en':
        return text
    elif to_code == 'hi':
        #    installed_languages1 = translate.get_installed_languages()
        available_packages = argostranslate.package.get_available_packages()
        available_package = list(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            )
        )[0]
        download_path = available_package.download()
        argostranslate.package.install_from_path(download_path)
    
        installed_languages = argostranslate.translate.get_installed_languages()
        from_lang = list(filter(
            lambda x: x.code == from_code,
            installed_languages))[0]
        to_lang = list(filter(
            lambda x: x.code == to_code,
            installed_languages))[0]
        translation = from_lang.get_translation(to_lang)
        tran_text = translation.translate(text)
#        translation_e = installed_languages1[0].get_translation(installed_languages1[1])
#        tran_text = translation_e.translate(text)
    elif to_code == 'ar':
        #    installed_languages1 = translate.get_installed_languages()
        available_packages = argostranslate.package.get_available_packages()
        available_package = list(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            )
        )[0]
        download_path = available_package.download()
        argostranslate.package.install_from_path(download_path)
    
        installed_languages = argostranslate.translate.get_installed_languages()
        from_lang = list(filter(
            lambda x: x.code == from_code,
            installed_languages))[0]
        to_lang = list(filter(
            lambda x: x.code == to_code,
            installed_languages))[0]
        translation = from_lang.get_translation(to_lang)
        tran_text = translation.translate(text)
        
#        translation_e = installed_languages1[0].get_translation(installed_languages1[2])
#        tran_text = translation_e.translate(text)
    return tran_text


class ActionGreetUser(Action):
    def name(self) -> Text:
        return "action_greet_user"

    def run(self,dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        text='''Hello, Welcome to Novagenie\n\n\nPlease Select One Language'''
        buttons=[
            {"payload":"/english","title":"English"},
            {"payload":"/hindi","title":"Hindi"},
            {"payload":"/arabic","title":"Arabic"}
        ]
        dispatcher.utter_message(text=text,buttons=buttons)
        return []

class ActionHindiLang(Action):

    def name(self) -> Text:
        return "action_hindi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global to_code
        to_code = 'hi'
        text= lang("You have chosen Hindi language,\n\n\n\nExplore The Novagenie")
        buttons=[
            {"payload":"/explore","title":lang("Explore")}
        ]
        dispatcher.utter_message(text=text,buttons=buttons)

        return []

class ActionEnglishLanguage(Action):
    
    def name(self) -> Text:
        return "action_english"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global to_code
        to_code = 'en'
        text= lang(" You have chosen English language,\n\n\n\nExplore The Novagenie")
        buttons=[
            {"payload":"/explore","title":lang("Explore")}
        ]
        dispatcher.utter_message(text=text,buttons=buttons)

        return []

class ActionArabicLanguage(Action):
    

    def name(self) -> Text:
        return "action_arabic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global to_code
        to_code = 'ar'
        text= lang(" You have chosen Arabic language,\n\n\n\nExplore The Novagenie")
        buttons=[
            {"payload":"/explore","title":lang("Explore")}
        ]
        dispatcher.utter_message(text=text,buttons=buttons)

        return []

#class ActionMenu(Action):
#    def name(self) -> Text:
#        return "action_menu"

#    def run(self,dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
#        text=lang("Explore The Novagenie")
#        buttons=[
#            {"payload":"/explore","title":lang("Explore")}
#        ]
#        dispatcher.utter_message(text=text,buttons=buttons)

class ActionExploreBot(Action):
    def name(self) -> Text:
        return "action_explore"

    def run(self,dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        text=lang("What would you like to know about?")
        buttons=[
            {"payload":"/popular_tours","title":lang("Most Popular Tours")},
            {"payload":"/popular_tours","title":lang("Things To DO in Abu Dhabi")},
            {"payload":"/popular_tours","title":lang("Things To DO in Dubai")},
            {"payload":"/popular_tours","title":lang("Choose the Destination")}
        ]
        dispatcher.utter_message(text=text,buttons=buttons)

class ActionTours(Action):
    def name(self) -> Text:
        return "action_tours"

    def run(self,dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        text=lang("These are the most relevant places for travelling")
        buttons=[
            {"payload":"/booking","title":lang("Book Now")},
            {"payload":"/call_agent","title":lang("Call Now")}
        ]
        dispatcher.utter_message(text=text,buttons=buttons)

class ActionFeedback(Action):
    def name(self) -> Text:
        return "action_feedback"

    def run(self,dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        text=lang("Would you like to give us a feedback?")
        buttons=[
                {"payload":"/comment","title":lang("very bad 😠")},
                {"payload":"/comment","title":lang("bad 😞")},
                {"payload":"/comment","title":lang("average 🙂")},
                {"payload":"/comment","title":lang("good 😊")},
                {"payload":"/comment","title":lang("very good 😁")},
                {"payload":"/comment","title":lang("No thank you")}
            ]
        
        dispatcher.utter_message(text=text,buttons=buttons)

class ActionAskComment(Action):

    def name(self) -> Text:
        return "action_ask_comment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            text=lang('Would you like to provide comments?')
            buttons=[
                {'payload':'/write','title':lang('Yes')},
                {'payload':'/deny','title':lang('No')}
            ]

            dispatcher.utter_message(text=text,buttons=buttons)

            return []

class ActionComment(Action):

    def name(self) -> Text:
        return "action_comment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=lang("Please add your experience in a few words."))

        return []
        
class ActionCommentResponse(Action):

    def name(self) -> Text:
        return "action_comment_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            text=lang('Thank you for your Response')

            dispatcher.utter_message(text=text)

            return []

class ActionAskTranscript(Action):

    def name(self) -> Text:
        return "action_ask_transcript"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            text=lang('Do you want a transcript of this conversation?')
            buttons=[
                {'payload':'/transcript','title':'Yes'},
                {'payload':'/no_transcript','title':'No'}
            ]

            dispatcher.utter_message(text=text,buttons=buttons)

            return []

class ActionNoTrancript(Action):

    def name(self) -> Text:
        return "action_transcript_no"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=lang("Okay,thank you\n\n\nGoodbye!!"))

        return []

class ActionYesTrancript(Action):

    def name(self) -> Text:
        return "action_transcript_yes"
    def emoji(self,add):
        string_unicode = add
        string_encode = string_unicode.encode("ascii", "ignore")
        add = string_encode.decode()
        return add
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        from fpdf import FPDF

        conv_id = 'Transcript ID - '+tracker.sender_id
        conv = tracker.events
        current_directory = os.getcwd()
        current_directory = current_directory.replace('\\','/')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)

        b = 'n'
        for i in conv:
            
            if i['event'] == 'user':

                if b == 'y':
                    for j in b_data:
                        if j['payload'] == i['text']:
                            add = j['title']+' :User      '
                            pdf.multi_cell(200, 10, txt = self.emoji(add), align = 'R')
                            break
                    b = 'n'

                else:
                    user = i['text']+' :User      '
                    pdf.multi_cell(200, 10, txt = self.emoji(user), align = 'R')

            if i['event'] == 'bot':

                if i['data']['buttons'] != None:
                    button = 'Bot:  '+i['text']
                    pdf.cell(200, 10, txt = self.emoji(button), ln = 1, align = 'L')
                    for j in range(len(i['data']['buttons'])):
                        button = '          '+i['data']['buttons'][j]['title']
                        pdf.multi_cell(200, 10, txt = self.emoji(button), align = 'L')
                    b = 'y'
                    b_data = i['data']['buttons']
                    
                else:
                    bot = 'Bot:  '+i['text']
                    pdf.multi_cell(200, 10, txt = self.emoji(bot), align = 'L')
                
                if i['data']['attachment'] != None:
                    pdf.multi_cell(200, 10, txt = self.emoji('         '+i['data']['attachment']), align = 'L')

        pdf.output(current_directory+'/'+conv_id+".pdf")
        
        dispatcher.utter_message(text=f"All the chats are saved. You can download the file using link\n file:///{current_directory}/{conv_id}.pdf\n\nThank you, Goodbye!")
        return []

def call_to_fixedline(phone_no):
    agent_no = 916266340992
    url = "https://cbw.vivacommunication.com:8901/cgi/web/callback_uat.pl"

    payload=f"First_Phone_Number={agent_no}&Second_Phone_Number={phone_no}&security_key=KgNjRnTqWtYv2y5AgNkRnTqWtYv2y5A7qWtYv2y5A7DaFcHfNkRnTqWtYv3y5A7D&billing_username=443332423832&billing_password=mjp%4044wns%237oql"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

class ActionCallBotGreet(Action):

    def name(self) -> Text:
        return "action_call_bot_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            text= lang("Please provide your Phone number with your international code and without the plus sign(+)")

            dispatcher.utter_message(text=text)

            return []

class ActionCallBotNumber(Action):

    def name(self) -> Text:
        return "action_call_bot_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        latest_message = tracker.latest_message
        phone_no = latest_message["text"]
        ret = call_to_fixedline(phone_no)
        out_text = lang(f"calling ... {phone_no} status:{ret}")
        dispatcher.utter_message(text=out_text)
        return []

#class ActionCallBotNumber(Action):

#    def name(self) -> Text:
#        return "action_call_project_manager"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # latest_message = tracker.latest_message
        # phone_no = latest_message["text"]
        # ret = call_to_fixedline(phone_no)
        # out_text = f"calling ... {phone_no} status:{ret}"
        # dispatcher.utter_message(text=out_text)
#        phone_no = 919894519141
#        ret = call_to_fixedline(phone_no)
#        out_text = lang(f"Connecting you with the project manager. You will now receive a call")
#        # image = 'https://i.ibb.co/N9hSK05/MyAvatar.png'
#        image ='https://i.ibb.co/L1Hh7FG/MyAvatar.png'
#        dispatcher.utter_message(text=out_text,image=image)
#        return []


class ActionIambot(Action):


    def name(self) -> Text:
        return "action_iamabot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            text= lang("I am a chatbot")

            dispatcher.utter_message(text=text)

            return []

class ActionPleasure(Action):

    def name(self) -> Text:
        return "action_thanks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            text= lang("I'm honoured to serve")

            dispatcher.utter_message(text=text)

            return [] 

class ActionFallback(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            msg = tracker.latest_message["text"]
            url = "https://uat.ml.novacept.io/query/gts?q="+msg
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.request("GET", url, headers=headers).json()
            out = json.loads(response['answers'][0]['answer'])
            if type(out) is list:
                carousel = {
                    "type": "Carousel",
                    "payload": {
                        "template_type": "generic",
                        "elements": []
                    }
                }
                for i in out:
                    card = {}
                    card["type"]=i["type"]
                    val = {}
                    for j in i:
                        if j!= "type":
                            val[j] = i[j]
                    card["payload"] = val
                    carousel['payload']['elements'].append(card)
                dispatcher.utter_message(attachment=carousel)
            else:
                try:
                    card = {}
                    card["type"]=out["type"]
                    val = {}
                    for i in out:
                        if i!= "type":
                            val[i] = out[i]
                    card["payload"] = val
                    dispatcher.utter_message(attachment=card)
                except:
                    dispatcher.utter_message(text=out)

            return []

class ActionAttachment(Action):

    def name(self) -> Text:
        return "action_attachment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thank you, Your attachment is saved")
        return []


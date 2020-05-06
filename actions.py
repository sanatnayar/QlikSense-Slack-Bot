# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import os
import subprocess
from typing import Any, Text, Dict, List
import requests
import re
import datetime
from rasa_sdk.events import ReminderScheduled
from rasa_sdk.events import ReminderCancelled
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
API_KEY = #SLACK API KEY HERE
channel = "D010ZGDGNBU"
API_ENDPOINT = "https://slack.com/api/chat.postMessage"
count = 0
class ActionHello(Action):
    def name(self) -> Text:
        return "helloAction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
  
        # your API key here 
        
        
        block ="""[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Welcome to the _QlikSense on Kubernetes Bot_* :tada:"
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "To get started, make sure your organization has gone through the neccessary onboarding steps and has `QlikSense CLI` installed. Use the buttons bellow for product information and/or a link to clone and install the CLI."
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "QlikSense CLI Repository"
                                },
                                "url": "https://github.com/qlik-oss/sense-installer"
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Product Information"
                                },
                                "url": "https://www.qlik.com/us/products/qlik-sense"
                            }
                        ]
                    }
                ]
            """    
     
        # data to be sent to api 
        data = {
                "token": API_KEY,
                "channel": channel,
                "text": "Error",
                "blocks": block
               } 
  
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data)
        
        # extracting response text  
        pastebin_url = r.text 
        print("The pastebin URL is:%s"%pastebin_url)  
        

class ActionShowCR(Action):

    def name(self) -> Text:
        return "actionInsight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        schema = tracker.get_slot("cluster_element")
        print(schema)
        if schema != None:
            schema = schema.lower()
        if schema == "cr":
            result = subprocess.run(['qliksense','config','view'] , stdout=subprocess.PIPE)
            message = result.stdout.decode("unicode_escape")
            dispatcher.utter_message(message)
            return [SlotSet("cluster_element", None)]   
        elif schema == "crd":
            result = subprocess.run(['qliksense','operator','crd'] , stdout=subprocess.PIPE)
            message = result.stdout.decode("unicode_escape")
            dispatcher.utter_message(message)
            return [SlotSet("cluster_element", None)]
        elif schema=="all":
            result = subprocess.run(['qliksense','config','list-contexts'] , stdout=subprocess.PIPE)
            message = result.stdout.decode("unicode_escape")
        else:
            message = "Sorry I could not understand what you mean"
            dispatcher.utter_message(message)
            return [SlotSet("cluster_element", None)]
        
       

        result = decode(message)
        print(result)

        text = """[
                    {{
                        "type": "section",
                        "text": {{
                            "type": "mrkdwn",
                            "text": "```{}```"
                        }}
                    }}
                ]
            """.format(result)
        print(type(message))
        # data to be sent to api 
        data = {
                "token": API_KEY,
                "channel": channel,
                "text": "Error",
                "blocks": text
               } 
  
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data)
        
        # extracting response text  
        pastebin_url = r.text 
        print("The pastebin URL is:%s"%pastebin_url)  

        return [SlotSet("cluster_element", None)]


class SetAttributeForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "attribute_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["key", "value"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"key": self.from_entity(entity="key",
                                                  intent="inputKey"),
                "value": self.from_entity(entity="value",
                                             intent="inputValue")}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        key = tracker.get_slot('key')
        value = tracker.get_slot('value')
        if type(value) is list:
            value=value[0]
        print(key, value)
        setCommand = key+'='+value
        print(setCommand)
        result = subprocess.run(['qliksense','config','set', setCommand] , stdout=subprocess.PIPE)
        message = result.stdout.decode("unicode_escape")
        message = decode(message)
        dispatcher.utter_message("```"+message+"```")

        

        return[SlotSet("key", None), SlotSet("value", None)]


class ActionPeformPreflight(Action):

    def name(self) -> Text:
        return "preflightChecks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        schema = tracker.get_slot("preflight")
        print(schema)
        if schema != None:
            schema = schema.lower()
            if schema == "deployments":
                result = subprocess.run(['qliksense','preflight','deployment'] , stdout=subprocess.PIPE)
                
        else:
            result = subprocess.run(['qliksense','preflight','all'] , stdout=subprocess.PIPE)
        message = result.stdout.decode('utf-8')
        message = decode(message)
        print(message)
        text = """[
                    {{
                        "type": "section",
                        "text": {{
                            "type": "mrkdwn",
                            "text": "{}"
                        }}
                    }}
                ]
            """.format(message)
        print(text)
        data = {
            "token": API_KEY,
            "channel": channel,
            "text": "Error",
            "blocks": text
        } 

        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data)
        
        # extracting response text  
        pastebin_url = r.text 
        print("The pastebin URL is:%s"%pastebin_url)  
            
       
        return [SlotSet("preflight", None)]

    

def decode (stri):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', stri)


class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        print("hi")
        global count
        if count == 0:
            name = tracker.get_slot("name")
            print(name)
            dispatcher.utter_message("I will send you cluster updates every "+''.join(name)+" minute(s) !")
            name = int(float("".join(name)))
        count = count + 1
        date = datetime.datetime.now() + datetime.timedelta(minutes=name)
        entities = tracker.latest_message.get("entities")
        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]

class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:


        result = subprocess.run(['kubectl','get','pods'] , stdout=subprocess.PIPE)
        message = result.stdout.decode("unicode_escape")
        message = decode(message)
        print(message)
        # subprocess.run(['kubectl','proxy','--www=.'])

        block ="""[
                    {{
                        "type": "section",
                        "text": {{
                            "type": "mrkdwn",
                            "text": "*QlikSense Cluster Information*"
                        }}
                    }},
                    {{
                        "type": "divider"
                    }},
                    {{
                        "type": "section",
                        "text": {{
                            "type": "mrkdwn",
                            "text": "```{}```"
                        }}
                    }},
                    {{
                        "type": "actions",
                        "elements": [
                            {{
                                "type": "button",
                                "text": {{
                                    "type": "plain_text",
                                    "text": "Cluster Visualization"
                                }},
                                "url": "http://localhost:8001/static"
                            }}
                        ]
                    }}
                ]
            """.format(message)
     
        # data to be sent to api 
        data = {
                "token": API_KEY,
                "channel": channel,
                "text": "Error",
                "blocks": block
               } 
  
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data)
        
        # extracting response text  
        pastebin_url = r.text 
        print("The pastebin URL is:%s"%pastebin_url)  



        name = tracker.get_slot("name")
        print(name)
        name = int(float("".join(name)))
        date = datetime.datetime.now() + datetime.timedelta(minutes=name)
        entities = tracker.latest_message.get("entities")
        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities=entities,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]

class ForgetReminders(Action):
    """Cancels all reminders."""

    def name(self) -> Text:
        return "action_forget_reminders"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(f"Okay, I'll cancel all your scheduled log updates.")

        # Cancel all reminders
        return [ReminderCancelled()]

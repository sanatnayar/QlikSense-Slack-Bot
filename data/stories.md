## insight path
* greet
  - helloAction
* retrieve
  - actionInsight

## addition path
* greet
  - helloAction
* setConfig
  - utter_ask_key
* inputKey{"key": "profile"}
  - attribute_form
  - form{"name": "attribute_form"}
  - form{"name": null}
  
## preflight path
* greet
  - helloAction
* doPreflight
  - preflightChecks

## sad path 2
* greet
  - helloAction
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## reminderPath
* greet
  - helloAction
* notifications{"name": "3"}
  - slot{"name": "3"}
  - action_set_reminder
* EXTERNAL_reminder
  - action_react_to_reminder
* cancel_notif
  - action_forget_reminders

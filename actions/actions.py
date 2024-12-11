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

# Running Coaching Chatbot Project

## Directory Structure

# running_coaching_chatbot/
# ├── actions.py
# ├── data/
# │   ├── nlu.yml
# │   ├── domain.yml
# │   ├── stories.yml
# ├── config.yml
# ├── credentials.yml
# ├── endpoints.yml
# ├── README.md
# ├── tests/
# │   └── test_stories.yml

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class ActionRecommendWorkout(Action):
    def name(self) -> Text:
        return "action_recommend_workout"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Fetch user goal from the slot
        user_goal = tracker.get_slot('goal')
        distance = tracker.get_slot('distance')
        pace = tracker.get_slot('pace')

        # Recommendation logic
        if user_goal == "5k race":
            recommendation = f"Try 5 x 800m intervals at a pace of {pace}, with 2 minutes rest."
        elif user_goal == "marathon":
            recommendation = f"Include a 15-mile long run at an easy pace this weekend."
        elif user_goal == "general fitness":
            recommendation = "Focus on consistent 3-4 mile runs at a conversational pace."
        else:
            recommendation = "Set clear running goals to get the best advice!"

        # Send response
        dispatcher.utter_message(text=f"Here's your workout: {recommendation}")
        return []
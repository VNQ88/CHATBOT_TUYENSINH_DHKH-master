from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleTuyenSinh(Action):

    def name(self) -> Text:
        return "action_handle_tuyen_sinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lấy giá trị của slot 'year'
        year = tracker.get_slot("year")

        # Xử lý logic dựa trên giá trị của 'year'
        if year == "2021":
            dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2021 là...")
        elif year == "2022":
            dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2022 là...")
        elif year == "2023":
            dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2023 là...")
        elif year == "2024":
            dispatcher.utter_message(text="Thông tin tuyển sinh cho năm 2024 là...")
        else:
            dispatcher.utter_message(text="Xin lỗi, tôi không có thông tin cho năm này.")

        return []

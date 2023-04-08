import asyncio
import inspect
from sanic import Sanic, Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse
from typing import Text, Dict, Any, Optional, Callable, Awaitable, NoReturn
import messagebird
from messagebird.conversation_message import MESSAGE_TYPE_TEXT

import rasa.utils.endpoints
from rasa.core.channels.channel import (
    InputChannel,
    CollectingOutputChannel,
    UserMessage,
    OutputChannel
)

# class birdout(OutputChannel):
#     @classmethod
#     def name(cls) -> Text:
#         return "bird"
#     def __init__(self) -> None:
#         self.birdclient = messagebird.Client("NiISB45Y1FMxZUkrQVniv10H0")
#     async def send_text_message(self, recipient_id: Text, text: Text, **kwargs: Any) -> None:
#         # print(text)
#         try:
#             # client = messagebird.Client("NiISB45Y1FMxZUkrQVniv10H0")

#             msg = self.birdclient.conversation_create_message("7ca5061c8ab94971bc8de1c3dd02d02e",
#                                                     {'channelId': "2a6ca10b711c4e7daec27556739ad213", 'type': MESSAGE_TYPE_TEXT,
#                                                     'content': {'text': text}})
#             # print('The following information was returned as a Conversation List object:')
#             print(msg)

#         except:
#             print('An error occured while requesting a Message object:')
#         return text

class chatroom(InputChannel):
    @classmethod
    def name(cls) -> Text:
        """Name of your custom channel."""
        return "chatroom"
    
    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[None]]
    ) -> Blueprint:

        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            inspect.getmodule(self).__name__,
        )

        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request) -> HTTPResponse:
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request: Request) -> HTTPResponse:
            sender_id = request.json.get("sender") # method to get sender_id
            text = request.json["message"]["content"]["text"] # method to fetch text
            conv = request.json["message"]["conversationId"]
            # print(conv)
            input_channel = self.name() # method to fetch input channel
            metadata = self.get_metadata(request) # method to get metadata
            print('')
            print('')
            print('')
            print(text)
            print('')
            print('')
            print('')
            collector = CollectingOutputChannel()
            # collector = self.get_output_channel()
            
            # include exception handling

            await on_new_message(
                UserMessage(
                    text,
                    collector,
                    sender_id,
                    input_channel=input_channel,
                    metadata=metadata,
                )
            )
            sendmsg = ''
            for i in collector.messages:
                sendmsg = i['text']
                try:
                    for j in i['buttons']:
                        sendmsg += '\n'+j['title']
                except:
                    pass
            
            if sendmsg != 'Sorry, I am not able to answer':
                try:
                    client = messagebird.Client("NiISB45Y1FMxZUkrQVniv10H0")

                    msg = client.conversation_create_message(conv,
                                                            {'channelId': "2a6ca10b711c4e7daec27556739ad213", 'type': MESSAGE_TYPE_TEXT,
                                                            'content': {'text': sendmsg}})
                    print('The following information was returned as a Conversation List object:')
                    print(msg)

                except:
                    print('An error occured while requesting a Message object:')

                    # for error in e.errors:
                    #     print('  code        : %d' % error.code)
                    #     print('  description : %s' % error.description)
                    #     print('  parameter   : %s\n' % error.parameter)
                # url = f"https://conversations.messagebird.com/v1/conversations/{text_all['conversationId']}/messages"

                # payload = json.dumps({
                # "type": "text",
                # "content": {
                #     "text": sendmsg
                # },
                # "source": {
                #     "foo": "var"
                # }
                # })
                # headers = {
                # 'Authorization': 'AccessKey NiISB45Y1FMxZUkrQVniv10H0',
                # 'Content-Type': 'application/json'
                # }

                # responsebird = requests.request("POST", url, headers=headers, data=payload)

                # print(responsebird.text)
            # for i in collector.messages:
            #     print(i)
            # return response.json(collector.messages)
            return response.json({"status": "ok"})

        return custom_webhook
    # def get_output_channel(self) -> OutputChannel:
    #     return birdout()
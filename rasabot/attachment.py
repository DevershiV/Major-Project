from typing import Dict, Text, Any, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.nlu.tokenizers.tokenizer import Token
from rasa.nlu.classifiers.classifier import IntentClassifier
import os.path
import os
import base64

# TODO: Correctly register your component with its type
@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.INTENT_CLASSIFIER], is_trainable=True
)
class CustomNLUComponent(GraphComponent, IntentClassifier):
    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> GraphComponent:
        # TODO: Implement this
        ...

    def train(self, training_data: TrainingData) -> Resource:
        # TODO: Implement this if your component requires training
        ...

    def process_training_data(self, training_data: TrainingData) -> TrainingData:
        # TODO: Implement this if your component augments the training data with
        #       tokens or message features which are used by other components
        #       during training.
        ...

        return training_data

    def process(self, messages: List[Message]) -> List[Message]:
        # TODO: This is the method which Rasa Open Source will call during inference.
        for message in messages:
            try:
                msg=message.data["text"]
                s=msg.find(',')
                msg_type=msg[:s+1]
                en_string=msg.replace(msg_type,"")
                f1=msg_type.find('=')
                f2=msg_type.find(' ')
                file_name=msg_type[f1+1:f2]
                doc_type=msg_type[msg_type.index(':')+1:msg_type.index(';')]
                if doc_type in msg_type:
                    decodeit = open(file_name, 'wb')
                    decodeit.write(base64.b64decode((en_string)))
                    decodeit.close()
                    message.data["text"]='shared an attachment'
            except:
                pass
            
            # msg= base64.b64encode(base64.b64decode(message))
            # if msg==message:
            #     if 'image' in message:
            #         decodeit = open('file.jpeg', 'wb')
            #         decodeit.write(base64.b64decode((message)))
            #         decodeit.close()
            #     elif 'text' in message:
            #         decodeit = open('file.txt', 'wb')
            #         decodeit.write(base64.b64decode((message)))
            #         decodeit.close()
            #     elif 'pdf' in message:
            #         decodeit = open('file.pdf', 'wb')
            #         decodeit.write(base64.b64decode((message)))
            #         decodeit.close()
            #     elif 'docx' in message:
            #         decodeit = open('file.docx', 'wb')
            #         decodeit.write(base64.b64decode((message)))
            #         decodeit.close()
                
            
        return messages
    
#    def process(self, message: Message, **kwargs: Any) -> None:
#        print(message.data["text"])

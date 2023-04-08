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
            if os.path.exists('trigger.txt'):
                message.data['text'] = 'Say Thank you for your response'
                os.remove("trigger.txt")
            #print(message.data)
            try:
                if message.data['intent']['name'] == 'write':
                    x = open('trigger.txt',"w+")
            except:
                pass

        for message in messages:
            if os.path.exists('trigger_attach.txt'):
                attach = open('attachments.txt',"a")
                attach.write(message.data['text']+'\n')
                attach.close()
                message.data['text'] = 'Say Your file is saved'
                os.remove("trigger_attach.txt")
            try:
                if message.data['intent']['name'] == 'attach':
                    x = open('trigger_attach.txt',"w+")
            except:
                pass
            
        return messages
    
#    def process(self, message: Message, **kwargs: Any) -> None:
#        print(message.data["text"])

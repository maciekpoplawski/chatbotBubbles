import json
import datetime
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer





class ChatterBotAppView(TemplateView):
    template_name = 'app.html'

class ChatterBotTest(TemplateView):
    template_name = 'bestchat.html'


    def get_context_data(self, **kwargs):
        """
        Overridden context data.
        """

        context = super(ChatterBotTest, self).get_context_data(**kwargs)

        context["current_date"] = datetime.datetime.now().strftime("%d %B %Y")
        context["current_time"] = datetime.datetime.now().strftime("%H:%M")

        return context




class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    #trainer = ChatterBotCorpusTrainer(chatterbot)

    #trainer.train('chatterbot.corpus.english')

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })

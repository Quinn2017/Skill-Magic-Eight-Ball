# Copyright 2018 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.


# Visit https://docs.mycroft.ai/skill.creation for more detailed information
# on the structure of this skill and its containing folder, as well as
# instructions for designing your own skill based on this template.


# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os import listdir
from os.path import dirname, isfile, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger


import random

__author__ = 'Charles'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class EightBallSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(EightBallSkill, self).__init__(name="EightBallSkill")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):

        ball_intent = IntentBuilder("BallIntent").\
            require("BallKeyword").build()
        self.register_intent(ball_intent, self.handle_ball_intent)

        question_intent = IntentBuilder("QuestionIntent").\
            require("BallKeyword").require("QuestionKeyword").build()
        self.register_intent(question_intent, self.handle_question_intent)

        done_intent = IntentBuilder("DoneIntent").\
            require("DoneKeyword").require("BallKeyword").build()
        self.register_intent(done_intent, self.handle_done_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.

    def handle_ball_intent(self, message):
        self.speak('I have retrieved your magic eight ball. What do you want to ask it?', expect_response=True)

    def handle_question_intent(self, message):
        answer = ['as I see it yes', 'ask again later', 'better not tell you now', 'cannot predict now', 'concentrate and ask again', 'dont count on it', 'it is certain', 'it is decidedly so', 'most likely', 'my reply is no', 'my sources say no', 'outlook good', 'outlook not so good', 'reply hazy, try again', 'signs point to yes', 'very doubtful', 'without a doubt', 'yes definitely', 'yes', 'you may rely on it']
        self.speak(random.choice(answer))

    def handle_done_intent(self, message):
        self.speak('Alright, lets put the magic eight ball away.')

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return EightBallSkill()
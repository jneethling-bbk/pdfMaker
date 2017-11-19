"""
This file defines and encapsulates all the custom colors that are used in the project
It can be used in any report type by simply importing the ReportColors class and calling the static methods (i.e.
the class is never meant to be instantiated, hence is static state with no instance methods)
Any additional custom colors that may be required in future should be defined here together with appropriate
static accessor methods (or getters)
"""

from reportlab.lib import colors

myBlue = colors.Color(red=(51.0 / 255), green=(122.0 / 255), blue=(183.0 / 255))
customDarkBlue = colors.Color(red=(91.0 / 255), green=(155.0 / 255), blue=(213.0 / 255))
customMediumBlue = colors.Color(red=(189.0 / 255), green=(215.0 / 255), blue=(238.0 / 255))
customLightBlue = colors.Color(red=(221.0 / 255), green=(235.0 / 255), blue=(247.0 / 255))
customGrey = colors.Color(red=(160.0 / 255), green=(160.0 / 255), blue=(160.0 / 255))
customLightGrey = colors.Color(red=(210.0 / 255), green=(210.0 / 255), blue=(210.0 / 255))
customRed = colors.Color(red=(255.0 / 255), green=(199.0 / 255), blue=(206.0 / 255))
customYellow = colors.Color(red=(255.0 / 255), green=(235.0 / 255), blue=(156.0 / 255))
customGreen = colors.Color(red=(198.0 / 255), green=(239.0 / 255), blue=(206.0 / 255))


class ReportColors(object):

    @staticmethod
    def get_my_blue():
        return myBlue

    @staticmethod
    def get_dark_blue():
        return customDarkBlue

    @staticmethod
    def get_light_blue():
        return customLightBlue

    @staticmethod
    def get_medium_blue():
        return customMediumBlue

    @staticmethod
    def get_grey():
        return customGrey

    @staticmethod
    def get_light_grey():
        return customLightGrey

    @staticmethod
    def get_green():
        return customGreen

    @staticmethod
    def get_red():
        return customRed

    @staticmethod
    def get_yellow():
        return customYellow

"""
This file defines and encapsulates all the custom font styles that are used in the project
It can be used in any report type by simply importing the ReportStylesheet class and calling the static methods (i.e.
the class is never meant to be instantiated, hence is static state with no instance methods)
Any additional custom styles that may be required in future should be defined here together with appropriate
static accessor methods (getters)
"""

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT, TA_CENTER

from generic_colors import ReportColors

# Defining fonts and custom colours
pdfmetrics.registerFont(TTFont("Lato-regular", "Lato-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Lato-bold", "Lato-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Lato-italic", "Lato-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("Lato-bolditalic", "Lato-BoldItalic.ttf"))

# Defining styles
heading1_style = ParagraphStyle(
    name='head1',
    fontName='Lato-bold',
    fontSize=16,
    spaceAfter=10,
    textColor=ReportColors.get_my_blue()
)

heading2_style = ParagraphStyle(
    name='head2',
    fontName='Lato-regular',
    fontSize=14,
    spaceAfter=8,
    textColor=ReportColors.get_my_blue()
)

heading3_style = ParagraphStyle(
    name='head3',
    fontName='Lato-regular',
    fontSize=12,
    spaceAfter=6,
    textColor=ReportColors.get_my_blue()
)

para_style = ParagraphStyle(
    name='para',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=10
)

para_bold_style = ParagraphStyle(
    name='para-bold',
    fontName='Lato-bold',
    fontSize=10,
    spaceAfter=10
)

list_style = ParagraphStyle(
    name='list',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    bulletIndent=15
)

sublist_style = ParagraphStyle(
    name='sublist',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    bulletIndent=30
)

header_style = ParagraphStyle(
    name='header',
    fontName='Lato-regular',
    fontSize=8,
    textColor=ReportColors.get_my_blue()
)

footer_style = ParagraphStyle(
    name='footer',
    fontName='Lato-regular',
    fontSize=8,
    spaceAfter=0,
    textColor=ReportColors.get_grey()
)

toc_special_style = ParagraphStyle(
    name='toc_special',
    fontName='Lato-bold',
    fontSize=16,
    spaceAfter=10,
    textColor=ReportColors.get_my_blue()
)

cover_style_large = ParagraphStyle(
    name='cover-large',
    fontName='Lato-bold',
    fontSize=30,
    alignment=1,
    spaceAfter=20
)

cover_style_italic = ParagraphStyle(
    name='cover-italic',
    fontName='Lato-italic',
    fontSize=16,
    alignment=1,
    spaceAfter=10
)

cover_style_bolditalic = ParagraphStyle(
    name='cover-bolditalic',
    fontName='Lato-bolditalic',
    fontSize=16,
    alignment=1,
    spaceAfter=10
)

tab_style = ParagraphStyle(
    name='table',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    textColor=colors.white
)

tab_center_style = ParagraphStyle(
    name='table-center',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    textColor=colors.white,
    alignment=TA_CENTER
)

graph_style = ParagraphStyle(
    name='graph',
    fontName='Lato-regular',
    fontSize=12,
    spaceAfter=8,
    textColor=ReportColors.get_grey(),
    alignment=TA_CENTER
)

graph_alt_style = ParagraphStyle(
    name='graph-alt',
    fontName='Lato-regular',
    fontSize=12,
    spaceAfter=8,
    textColor=ReportColors.get_grey(),
    leftIndent=140
)

right_style = ParagraphStyle(
    name='right',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=10,
    alignment=TA_RIGHT
)

center_style = ParagraphStyle(
    name='center',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=10,
    alignment=TA_CENTER
)

bold_right_style = ParagraphStyle(
    name='para-bold-right',
    fontName='Lato-bold',
    fontSize=10,
    spaceAfter=10,
    alignment=TA_RIGHT
)

hl_right_style = ParagraphStyle(
    name='hl_right',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=10,
    alignment=TA_RIGHT,
    backColor=colors.yellow
)

hl_para_style = ParagraphStyle(
    name='hl_para',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=10,
    backColor=colors.yellow
)

green_style = ParagraphStyle(
    name='green-style',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    textColor=colors.green,
    alignment=TA_CENTER
)

red_style = ParagraphStyle(
    name='red-style',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    textColor=colors.red,
    alignment=TA_CENTER
)

red_style_left = ParagraphStyle(
    name='red-style-left',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    textColor=colors.red,
)

red_style_right = ParagraphStyle(
    name='red-style-right',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=0,
    textColor=colors.red,
    alignment=TA_RIGHT
)

indent_style = ParagraphStyle(
    name='indent',
    fontName='Lato-regular',
    fontSize=10,
    spaceAfter=10,
    bulletIndent=10
)


class ReportStylesheet(object):
    @staticmethod
    def get_heading1_style():
        return heading1_style

    @staticmethod
    def get_heading2_style():
        return heading2_style

    @staticmethod
    def get_heading3_style():
        return heading3_style

    @staticmethod
    def get_para_style():
        return para_style

    @staticmethod
    def get_para_bold_style():
        return para_bold_style

    @staticmethod
    def get_list_style():
        return list_style

    @staticmethod
    def get_sublist_style():
        return sublist_style

    @staticmethod
    def get_header_style():
        return header_style

    @staticmethod
    def get_footer_style():
        return footer_style

    @staticmethod
    def get_toc_special_style():
        return toc_special_style

    @staticmethod
    def get_cover_style_large():
        return cover_style_large

    @staticmethod
    def get_cover_style_italic():
        return cover_style_italic

    @staticmethod
    def get_cover_style_bolditalic():
        return cover_style_bolditalic

    @staticmethod
    def get_tab_style():
        return tab_style

    @staticmethod
    def get_tab_center_style():
        return tab_center_style

    @staticmethod
    def get_graph_style():
        return graph_style

    @staticmethod
    def get_graph_alt_style():
        return graph_alt_style

    @staticmethod
    def get_right_style():
        return right_style

    @staticmethod
    def get_center_style():
        return center_style

    @staticmethod
    def get_bold_right_style():
        return bold_right_style

    @staticmethod
    def get_hl_right_style():
        return hl_right_style

    @staticmethod
    def get_hl_para_style():
        return hl_para_style

    @staticmethod
    def get_green_style():
        return green_style

    @staticmethod
    def get_red_style():
        return red_style

    @staticmethod
    def get_red_style_left():
        return red_style_left

    @staticmethod
    def get_red_style_right():
        return red_style_right

    @staticmethod
    def get_indent_style():
        return indent_style

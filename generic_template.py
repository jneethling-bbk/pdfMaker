"""
The class in this file is responsible for providing a consistent approach to constructing all the basic elements of
reports including management of the page layouts (portrait and landscape), cover page, table of content,
headers and footers. It sub-classes the ReportLab BaseDocTemplate and as such it must adhere to the contract for that
super-class.
"""

from reportlab.platypus import *
from reportlab.lib.pagesizes import A4, landscape, cm
from reportlab.graphics.shapes import Drawing, Line

from generic_colors import ReportColors
from generic_styles import ReportStylesheet


class ReportTemplate(BaseDocTemplate):

    def __init__(self, filename, **kw):
        """
        :param filename:    The filename of the pdf output
        :param kw:          A dictionary of keywords as per super-class contract; in this case it is used to bring in additional data
        """
        self.allowSplitting = 0

        self.logo = kw['logo']
        self.emblem1 = kw['emblem1']
        self.emblem2 = kw['emblem2']
        self.header_line = kw['header']
        self.footer_line = kw['footer']
        self.cover_graphic = kw['cover_graphic']

        BaseDocTemplate.__init__(self, filename, **kw)

        p_frame = Frame(self.leftMargin - 20, self.bottomMargin, self.width + 40, self.height,
                        leftPadding=0, rightPadding=0,
                        topPadding=-20, bottomPadding=-20,
                        id='portrait_frame')

        l_frame = Frame(self.leftMargin - 20, self.bottomMargin, self.height + 40, self.width,
                        leftPadding=0, rightPadding=0,
                        topPadding=-20, bottomPadding=-20,
                        id='landscape_frame')

        ctemplate = PageTemplate(id='cover', frames=[p_frame], pagesize=A4, onPage=self.set_cover,
                                 onPageEnd=self.p_footer)
        ptemplate = PageTemplate(id='portrait', frames=[p_frame], pagesize=A4, onPage=self.p_header,
                                 onPageEnd=self.p_footer)
        ltemplate = PageTemplate(id='landscape', frames=[l_frame], pagesize=landscape(A4), onPage=self.l_header,
                                 onPageEnd=self.l_footer)

        self.addPageTemplates([ctemplate, ptemplate, ltemplate])

    def afterFlowable(self, flowable):
        """Registers TOC entries."""
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'head1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'head2':
                self.notify('TOCEntry', (1, text, self.page))
            if style == 'head3':
                self.notify('TOCEntry', (2, text, self.page))

    def set_cover(self, canvas, ldoc):
        """Set up the cover page."""
        self.emblem2.drawHeight = 5.7 * cm
        self.emblem2.drawWidth = 4 * cm
        self.emblem2.drawOn(canvas, ldoc.width/2, ldoc.height/3)
        self.cover_graphic.drawOn(canvas, ldoc.rightMargin, ldoc.bottomMargin - 80)
        self.p_header(canvas, ldoc)

    def p_header(self, canvas, ldoc):
        """Set up the header for all portrait pages"""
        canvas.saveState()
        self.header_line.wrap(ldoc.width, ldoc.topMargin)
        self.header_line.drawOn(canvas, ldoc.leftMargin + 40, ldoc.height + ldoc.topMargin + 40)
        self.logo.drawHeight = 0.6 * cm
        self.logo.drawWidth = 1.9 * cm
        self.logo.drawOn(canvas, ldoc.leftMargin - 20, ldoc.height + ldoc.topMargin + 45)
        self.emblem1.drawHeight = 0.6 * cm
        self.emblem1.drawWidth = 0.6 * cm
        self.emblem1.drawOn(canvas, ldoc.width + 75, ldoc.height + ldoc.topMargin + 45)
        d = Drawing(ldoc.width, 1)
        d.add(Line(0, 0, ldoc.width + 40, 0, strokeWidth=0.1, strokeColor=ReportColors.get_my_blue()))
        d.drawOn(canvas, ldoc.leftMargin - 20, ldoc.height + ldoc.topMargin + 40)
        canvas.restoreState()

    def l_header(self, canvas, ldoc):
        """Set up the header for all landscape pages"""
        canvas.saveState()
        self.header_line.wrap(ldoc.width, ldoc.topMargin)
        self.header_line.drawOn(canvas, ldoc.leftMargin + 40, ldoc.height + ldoc.topMargin - 210)
        self.logo.drawHeight = 0.6 * cm
        self.logo.drawWidth = 1.9 * cm
        self.logo.drawOn(canvas, ldoc.leftMargin - 20, ldoc.height + ldoc.topMargin - 205)
        self.emblem1.drawHeight = 0.6 * cm
        self.emblem1.drawWidth = 0.6 * cm
        self.emblem1.drawOn(canvas, ldoc.width + 280, ldoc.height + ldoc.topMargin - 205)
        d = Drawing(ldoc.height, 1)
        d.add(Line(0, 0, ldoc.height, 0, strokeWidth=0.1, strokeColor=ReportColors.get_my_blue()))
        d.drawOn(canvas, ldoc.leftMargin - 20, ldoc.height + ldoc.topMargin - 210)
        canvas.restoreState()

    def p_footer(self, canvas, ldoc):
        """Set up the footer for all portrait pages"""
        canvas.saveState()
        page_num = Paragraph(str(canvas.getPageNumber()), ReportStylesheet.get_footer_style())
        footer_data = [[self.footer_line, page_num]]
        ff = Table(footer_data, ldoc.width)
        ff.setStyle(TableStyle([('ALIGN', (0, 1), (0, -1), "RIGHT")]))
        w, h = ff.wrap(ldoc.width, ldoc.bottomMargin)
        ff.drawOn(canvas, ldoc.leftMargin - 20, h)
        canvas.restoreState()

    def l_footer(self, canvas, ldoc):
        """Set up the footer for all landscape pages"""
        canvas.saveState()
        page_num = Paragraph(str(canvas.getPageNumber()), ReportStylesheet.get_footer_style())
        footer_data = [[self.footer_line, page_num]]
        ff = Table(footer_data, ldoc.height)
        ff.setStyle(TableStyle([('ALIGN', (0, 1), (0, -1), "RIGHT")]))
        w, h = ff.wrap(ldoc.width, ldoc.bottomMargin)
        ff.drawOn(canvas, ldoc.leftMargin - 20, h)
        canvas.restoreState()

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.layout.viewlets import common
from Acquisition import aq_base, aq_inner
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName

class LogoViewlet(common.LogoViewlet):
    index = ViewPageTemplateFile('templates/logo.pt')
    def update(self):
        super(LogoViewlet, self).update()

class FooterViewlet(common.FooterViewlet):
    index = ViewPageTemplateFile('templates/footer.pt')

    def update(self):
        super(FooterViewlet, self).update()

class PersonalBarViewlet(common.PersonalBarViewlet):

    index = ViewPageTemplateFile('templates/personal_bar.pt')

    def update(self):
        super(PersonalBarViewlet, self).update()
        self.about = '/'.join([self.portal_state.navigation_root_url(), "info"])
        self.help = '/'.join([self.portal_state.navigation_root_url(), "help"])        
        self.logout = '/'.join([self.portal_state.navigation_root_url(), "logout"])     

class ProductVersionViewlet(common.ViewletBase):
    """A viewlet which informs about the Product versions
    """
    def get_version(self):
        qi = getToolByName(self.context, 'portal_quickinstaller')
        return '-'.join([qi.getProductVersion("esdrt.content"), qi.getProductVersion("esdrt.theme")])



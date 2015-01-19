from plone import api
from plone.app.layout.viewlets import common
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


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

        if hasattr(self, 'user_name'):
            self.user_name += ' (%s)' % self.get_groupnames()

    def get_groupnames(self):
        groupnames = []
        user = api.user.get_current()
        groups = user.getGroups()
        for group in groups:
            if group.startswith('extranet-esd-ghginv-sr-'):
                groupitem = api.group.get(group)
                name = groupitem.getProperty('title')
                if name.strip():
                    groupnames.append(name)
                else:
                    new_name = group.replace('extranet-esd-ghginv-sr-', '')
                    splitted_name = new_name.split('-')
                    if len(splitted_name) == 2:
                        groupnames.append('Sector Expert - %s - %s' % (
                            splitted_name[0], splitted_name[1].upper())
                        )
            elif group.startswith('extranet-esd-ghginv-qualityexpert-'):
                groupitem = api.group.get(group)
                name = groupitem.getProperty('title')
                if name.strip():
                    groupnames.append(name)
                else:
                    new_name = group.replace('extranet-esd-ghginv-qualityexpert-', '')
                    if new_name.strip():
                        groupnames.append('Quality Expert - %s' % new_name)

            elif group.startswith('extranet-esd-esdreview-reviewexp-'):
                groupitem = api.group.get(group)
                name = groupitem.getProperty('title')
                if name.strip():
                    groupnames.append(name)
                else:
                    new_name = group.replace('extranet-esd-esdreview-reviewexp-', '')
                    splitted_name = new_name.split('-')
                    if len(splitted_name) == 2:
                        groupnames.append('Review Expert - %s - %s' % (
                            splitted_name[0], splitted_name[1].upper())
                        )

            elif group.startswith('extranet-esd-esdreview-leadreview-'):
                groupitem = api.group.get(group)
                name = groupitem.getProperty('title')
                if name.strip():
                    groupnames.append(name)
                else:
                    new_name = group.replace('extranet-esd-esdreview-leadreview-', '')
                    if new_name.strip():
                        groupnames.append('Quality Expert - %s' % new_name.upper())

            elif group.startswith('extranet-esd-countries-msa-'):
                groupitem = api.group.get(group)
                name = groupitem.getProperty('title')
                if name.strip():
                    groupnames.append(name)
                else:
                    new_name = group.replace('extranet-esd-countries-msa-', '')
                    if new_name.strip():
                        groupnames.append('MS Coordinator - %s' % new_name.upper())

            elif group.startswith('extranet-esd-countries-msexpert-'):
                groupitem = api.group.get(group)
                name = groupitem.getProperty('title')
                if name.strip():
                    groupnames.append(name)
                else:
                    new_name = group.replace('extranet-esd-countries-msexpert-', '')
                    if new_name.strip():
                        groupnames.append('MS Expert - %s' % new_name.upper())

        return ', '.join(groupnames)


class ProductVersionViewlet(common.ViewletBase):
    """A viewlet which informs about the Product versions
    """

    def get_version(self):
        qi = getToolByName(self.context, 'portal_quickinstaller')
        return '-'.join([qi.getProductVersion("esdrt.content"), qi.getProductVersion("esdrt.theme")])

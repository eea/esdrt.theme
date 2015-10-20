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
            self.user_roles = self.get_groupnames()

        #if hasattr(self, 'user_name'):
        #    self.user_name += ' (%s)' % self.get_groupnames()
        #    #self.user_name += ' (%s)' % get_category_ldap_from_crf_code("2C4")

    def get_groupnames(self):
        groupnames = {}
        user = api.user.get_current()
        groups = user.getGroups()
        sector_review_roles = []
        quality_expert_roles = []
        review_expert_roles = []
        lead_review_roles = []
        ms_coordinator_roles = []
        ms_expert_roles = []
        for group in groups:
            if group.startswith('extranet-esd-ghginv-sr-'):
                new_name = group.replace('extranet-esd-ghginv-sr-', '')
                splitted_name = new_name.split('-')
                if len(splitted_name) == 2:
                    sector_review_roles.append('%s - %s' % (
                                                    self.get_country_name(splitted_name[1]), splitted_name[0])
                                                )

            elif group.startswith('extranet-esd-ghginv-qualityexpert-'):
                new_name = group.replace('extranet-esd-ghginv-qualityexpert-', '')
                if new_name.strip():
                    quality_expert_roles.append('%s' % new_name)

            elif group.startswith('extranet-esd-esdreview-reviewexp-'):
                new_name = group.replace('extranet-esd-esdreview-reviewexp-', '')
                splitted_name = new_name.split('-')
                if len(splitted_name) == 2:
                    review_expert_roles.append('%s - %s' % (
                        splitted_name[0], self.get_country_name(splitted_name[1]))
                    )

            elif group.startswith('extranet-esd-esdreview-leadreview-'):
                new_name = group.replace('extranet-esd-esdreview-leadreview-', '')
                if new_name.strip():
                    lead_review_roles.append('%s' % self.get_country_name(new_name))

            elif group.startswith('extranet-esd-countries-msa-'):
                new_name = group.replace('extranet-esd-countries-msa-', '')
                if new_name.strip():
                    ms_coordinator_roles.append('%s' % self.get_country_name(new_name))

            elif group.startswith('extranet-esd-countries-msexpert-'):
                new_name = group.replace('extranet-esd-countries-msexpert-', '')
                if new_name.strip():
                    ms_expert_roles.append('%s' % self.get_country_name(new_name))
        sector_review_roles.sort()
        groupnames["sector_review_roles"] = sector_review_roles
        quality_expert_roles.sort()
        groupnames["quality_expert_roles"] = quality_expert_roles
        review_expert_roles.sort()
        groupnames["review_expert_roles"] = review_expert_roles
        lead_review_roles.sort()
        groupnames["lead_review_roles"] = lead_review_roles
        ms_coordinator_roles.sort()
        groupnames["ms_coordinator_roles"] = ms_coordinator_roles
        ms_expert_roles.sort()
        groupnames["ms_expert_roles"] = ms_expert_roles


        return groupnames

    def get_country_name(self, countryCode):
        if countryCode == "at":
            return "Austria"
        elif countryCode == "be":
            return "Belgium"
        elif countryCode == "bg":
            return "Bulgaria"
        elif countryCode == "hr":
            return "Croatia"
        elif countryCode == "cy":
            return "Cyprus"
        elif countryCode == "cz":
            return "Czech Republic"
        elif countryCode == "dk":
            return "Denmark"
        elif countryCode == "ee":
            return "Estonia"
        elif countryCode == "fi":
            return "Finland"
        elif countryCode == "fr":
            return "France"
        elif countryCode == "de":
            return "Germany"
        elif countryCode == "gr":
            return "Greece"
        elif countryCode == "hu":
            return "Hungary"
        elif countryCode == "is":
            return "Iceland"
        elif countryCode == "ie":
            return "Ireland"
        elif countryCode == "it":
            return "Italy"
        elif countryCode == "lv":
            return "Latvia"
        elif countryCode == "lt":
            return "Lithuania"
        elif countryCode == "lu":
            return "Luxembourg"
        elif countryCode == "mt":
            return "Malta"
        elif countryCode == "nl":
            return "Netherlands"
        elif countryCode == "pl":
            return "Poland"
        elif countryCode == "pt":
            return "Portugal"
        elif countryCode == "ro":
            return "Romania"
        elif countryCode == "sk":
            return "Slovakia"
        elif countryCode == "sl":
            return "Slovania"
        elif countryCode == "es":
            return "Spain"
        elif countryCode == "se":
            return "Sweden"
        elif countryCode == "gb":
            return "United Kingdom"
        else:
            return countryCode

#class ProductVersionViewlet(common.ViewletBase):
    #"""A viewlet which informs about the Product versions
    #"""

    #def get_version(self):
        #qi = getToolByName(self.context, 'portal_quickinstaller')
        #return '-'.join([qi.getProductVersion("esdrt.content"), qi.getProductVersion("esdrt.theme")])

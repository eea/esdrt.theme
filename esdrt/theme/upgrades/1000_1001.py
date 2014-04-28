from Products.CMFCore.utils import getToolByName


PROFILE_ID = 'profile-esdrt.theme:default'


def upgrade(context, logger=None):
    if logger is None:
        from logging import getLogger
        logger = getLogger('esdrt.theme.upgrades.1000_1001')

    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'jsregistry')
    logger.info('Reload JS')
    logger.info('Upgrade steps executed')

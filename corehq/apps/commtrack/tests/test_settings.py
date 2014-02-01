from django.test import TestCase
from corehq.apps.commtrack.models import CommtrackConfig, ConsumptionConfig, StockRestoreConfig
from corehq.apps.commtrack.tests.util import bootstrap_domain
from corehq.apps.consumption.shortcuts import set_default_consumption_for_domain


class CommTrackSettingsTest(TestCase):

    def testOTASettings(self):
        domain = bootstrap_domain()
        ct_settings = CommtrackConfig.for_domain(domain.name)
        ct_settings.consumption_config = ConsumptionConfig(
            min_transactions=10,
            min_window=20,
            optimal_window=60,
        )
        ct_settings.ota_restore_config = StockRestoreConfig(
            section_to_consumption_types={'stock': 'consumption'}
        )
        set_default_consumption_for_domain(domain.name, 5)
        restore_settings = ct_settings.get_ota_restore_settings()
        self.assertEqual(1, len(restore_settings.section_to_consumption_types))
        self.assertEqual('consumption', restore_settings.section_to_consumption_types['stock'])
        self.assertEqual(10, restore_settings.consumption_config.min_periods)
        self.assertEqual(20, restore_settings.consumption_config.min_window)
        self.assertEqual(60, restore_settings.consumption_config.max_window)
        self.assertEqual(5, restore_settings.consumption_config.default_consumption_function('foo', 'bar'))

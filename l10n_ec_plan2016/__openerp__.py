# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Plan de Cuentas Ecuador NIFF',
    'version': '1.1',
    'category': 'Localization/Account Charts',
    'description': """
Plan de cuentas para Odoo v9.0. ACTUALIZADO - ESTE MODULO ESTA DESARROLLADO BAJO LICENCIA DE SOFTWARE LIBRE LGPLv3.
==============================================================================

En esta actualización, se ha optimizado las opciones en cuentas particulares
Instala el Plan de Cuentas NIFF
    """,
    'author': 'odoo-group-ecuador',
    'depends': [
        'account',
    ],
    'data': [
        'data/configurable_account_chart.xml',
        'account_chart_template.yml',
        'account.account.csv',
    ],
    'test': [
        '../account/test/account_bank_statement.yml',
        #'../account/test/account_cash_statement.yml',
        '../account/test/account_invoice_state.yml',
    ],
    'demo': [
        '../account/demo/account_bank_statement.yml',
        '../account/demo/account_invoice_demo.yml',
    ],
    'installable': True,
    'website': 'https://www.odoo.com',
}

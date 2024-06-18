# -*- coding: utf-8 -*-
{
    'name': "escuela",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'views/Group_security.xml',
        'security/ir.model.access.csv',
        'views/Alumno_view.xml',
        'views/Asignatura_view.xml',
        'views/Aula_view.xml',
        'views/CicloEscolaridad_view.xml',
        'views/Colegio_view.xml',
        'views/Edificio_view.xml',
        'views/GestionAcademica_view.xml',
        'views/Horario_view.xml',
        'views/Inscripcion_view.xml',
        'views/InstalacionesComunes_view.xml',
        'views/Mensualidad_view.xml',
        'views/NotasAsignatura_view.xml',
        'views/Profesor_view.xml',
        'views/Recurso_view.xml',
        'views/Tutor_view.xml',
        'views/Tags_view.xml',
        'reports/student_report_template_view.xml',
        # 'views/report_notasasignatura_template.xml'
        # 'views/templates.xml',
        # 'views/templates_horario.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'escuela/static/src/css/custom_styles.css',
        ],
        'web.assets_frontend': [
            'escuela/static/src/css/custom_styles.css',
        ],
    },
}

